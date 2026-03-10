import time
from fastapi import FastAPI, Request
from .engine import MyDBSCAN
import numpy as np

app = FastAPI()
traffic_history = []
last_hit = time.time()

@app.middleware("http")
async def monitor(request: Request, call_next):
    global last_hit
    size = int(request.headers.get("content-length", 0))
    gap = time.time() - last_hit
    last_hit = time.time()
    traffic_history.append([float(size), gap])
    return await call_next(request)

@app.get("/")
async def root():
    return {"status": "Live", "msg": "Send traffic to analyze."}

@app.get("/analyze")
async def analyze():
    if len(traffic_history) < 5:
        return {"error": "Need more traffic data."}
    
    # Run the custom engine
    model = MyDBSCAN(eps=5.0, min_pts=3)
    results = model.fit(np.array(traffic_history))
    
    anomalies = [traffic_history[i] for i, lbl in enumerate(results) if lbl == -1]
    return {"total": len(traffic_history), "threats": len(anomalies), "data": anomalies}