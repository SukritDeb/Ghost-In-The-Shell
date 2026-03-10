# 👻 Ghost-In-The-Shell: Autonomous Anomaly Detection

**Ghost-In-The-Shell** is an unsupervised, real-time network security agent designed to detect Zero-Day attacks and DDoS attempts. Unlike traditional firewalls that rely on known signatures, this system uses a **custom-built DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** algorithm to identify malicious traffic patterns as statistical "Noise."



## 🚀 The Core Innovation: Why DBSCAN?
Most security systems use K-Means, which forces every data point into a cluster—potentially hiding a hacker inside "normal" traffic. 
* **Our Approach:** We implemented DBSCAN **from scratch** (zero dependencies on `scikit-learn` for the engine). 
* **Density-Based:** It identifies dense "crowds" of normal user behavior.
* **Noise Discovery:** Anything that doesn't fit the density of the crowd is labeled as `-1` (Noise), triggering an immediate SRE alert.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Backend Framework:** FastAPI (Asynchronous request monitoring)
* **Mathematics:** NumPy (Vectorized Euclidean distance calculations)
* **DevOps:** Middleware-based data ingestion

---

## 📂 Project Structure
```text
GhostInTheShell/
├── app/
│   ├── __init__.py    # Package marker
│   ├── engine.py      # The "Brain": Custom DBSCAN Implementation
│   └── main.py        # The "Sensor": FastAPI Server & Middleware
├── tests/
│   ├── __init__.py    # Package marker
│   └── simulate.py    # The "Attacker": Simulation script for demo
├── .gitignore         # Prevents venv/ and cache from being uploaded
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
⚡ Quick Start (PowerShell)1. Setup EnvironmentPowerShell# Clone the repo
git clone [https://github.com/YOUR_USERNAME/GhostInTheShell.git](https://github.com/YOUR_USERNAME/GhostInTheShell.git)
cd GhostInTheShell

# Create and Activate Virtual Env
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install Dependencies
pip install -r requirements.txt
2. Run the Security MonitorPowerShelluvicorn app.main:app --reload
3. Run the Attack Simulation (Open a New Terminal)PowerShell# Navigate to project folder and activate venv
.\venv\Scripts\Activate.ps1
python -m tests.simulate
4. View ResultsVisit http://127.0.0.1:8000/analyze in your browser to see the AI isolate the hacker in real-time.🧠 How it Works: The MathThe system tracks two primary features for every incoming request:Payload Size ($x$): The length of the request body (Content-Length).Request Frequency ($y$): The time gap since the previous request.The engine calculates the distance between these points using the Euclidean formula:$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$If a point has fewer than min_pts within the radius eps, it is mathematically isolated as Noise (-1). In our system, this represents a traffic pattern that is too large or too frequent to be a standard user.🛡️ SRE & DevOps IntegrationThis project is designed to act as an Autonomous SRE Agent. When an anomaly is detected:Identification: The specific request pattern is logged and flagged in the PowerShell console.Response (Roadmap): Future iterations will include automated Docker container isolation and dynamic IP blacklisting via iptables.
---

### Final Instructions for GitHub
1.  **Save** this code as `README.md`.
2.  **Commit** it: `git add README.md`, `git commit -m "Add professional documentation"`.
3.  **Push** it: `git push origin main`.
