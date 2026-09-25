# ⚓ ColdChain AI: Catch-to-Market Optimization Control Hub

> **Advanced AI-powered predictive logistics framework bridging offshore fishing fleets with mainland supply chains to eliminate post-harvest spoilage and stabilize market pricing.**

Developed as a disruptive prototype submission for the **Dialog Innovation Challenge**, **ColdChain AI** solves a critical structural bottleneck in Sri Lanka's premium marine export sector (Yellowfin Tuna, Skipjack Tuna). By turning unpredictable seafaring metrics into data-driven logistics, the platform tackles the traditional **20% to 40% post-harvest seafood loss** experienced in domestic fisheries.

---

## 🌟 Key Core Capabilities

- **🤖 Dynamic Machine Learning ETA Engine:** Ingests live offshore telemetry alongside global marine data models to predict precise vessel docking times under varying sea weather conditions using **XGBoost Regression**.
- **🌡️ IoT Spoilage Risk Guard:** Evaluates active real-time data streams from cargo hold temperature logs to flag high-risk catch batches for priority processing before arrival.
- **💬 Dialog Infrastructure Synergy:** Deep architectural integration with native **Dialog Axiata Enterprise APIs**, specifically automated pre-emptive routing dispatches through **Dialog Ideamart SMS Gateways** to optimize mainland reefer truck logistics.
- **🗺️ Interactive Geofence Map Tracker:** Unified monitoring interface built for exporters to track fleet positions, live environmental variables, and logistical matching windows.

---

## 🏗️ Technical Architecture & System Flow

[ Offshore Vessels ]
       │  (Vessel Edge Client / VMS GPS Ingestion)
       ▼
( Low-Bandwidth Telemetry )
       │
       ▼
[ AI Yield & Prediction Engine ] 
       │  (XGBoost / LSTM ETA & Spoilage Matrix)
       ▼
[ Smart Logistics Hub ]
       │  (Auto-Allocates Cold Storage / Trucks)
       ▼
( Dialog Ideamart SMS Dispatches )

1. **The Telemetry Ingestion Layer:** The platform captures real-time vessel vectors (Latitude, Longitude, Heading, Hold Temperatures) utilizing existing Vessel Monitoring Systems (VMS) APIs or compressed short-burst satellite arrays.
2. **The Predictive Cloud Engine:** Live marine variables (Wave heights, current speeds, wave vectors) are programmatically parsed from spatial APIs and merged with vessel telemetry inside an extreme gradient boosting model to forecast dynamic transit shifts.
3. **The Autonomous Communication Routing Layer:** Triggers structural data routing payloads seamlessly mapped out to alert pre-verified mainland cold storage assets via **Dialog Ideamart**, completing the digital sea-to-shelf chain before the vessel berths.

---

## 🛠️ Tech Stack & Dependencies

- **Core Framework & Interface:** [Streamlit](https://streamlit.io) (Dynamic Front-End Framework)
- **Machine Learning & Frameworks:** [XGBoost](https://readthedocs.io) (Extreme Gradient Boosting Engine), NumPy, Pandas
- **Geospatial & Ingestion:** [Open-Meteo Marine API](https://open-meteo.com)
- **Communications Backend:** Dialog Ideamart API JSON Integration Specifications

---

## 🚀 Local Installation & Quick Deployment

To spin up the interactive developer prototype environment locally on your computer, execute the following configuration pipeline:

### 1. Clone the Active Project Repository
```bash
git clone https://github.com
cd coldchain-ai
```

### 2. Install Project Dependencies
Deploy the pre-requisite libraries mapped inside the runtime engine configurations:
```bash
pip install -r requirements.txt
```

### 3. Initialize the Web Dashboard Interface
Boot the local engine container to access the functional web workspace profile:
```bash
streamlit run app.py
```
*Your browser should automatically trigger a viewport redirection to access the dashboard workspace locally at `http://localhost:8501`.*

---

## 📁 Repository Directory Structure

```text
📁 coldchain-ai/
├── 📄 app.py              # Main Streamlit web UI, API handler, & inline predictive ML logic
├── 📄 requirements.txt    # Mandatory Python cloud server container dependencies file
└── 📄 README.md           # Professional project repository documentation index
```

---

## 🤝 Project Alignment & Dialog Axiata Ecosystem Synergy

ColdChain AI was meticulously architecturalized to scale via the existing infrastructural capabilities of **Dialog Axiata**:
- **Dialog NB-IoT / LTE-M Networks:** Optimal edge tracking connectivity pipeline inside cold holds for small-power marine data telemetry.
- **Dialog Extended-Range Coastal 4G/5G cells:** Deep penetration data dumps to sync localized IoT logs 20 nautical miles offshore.
- **Genie Business / Dialog Finance:** Escrow protection logic for fast, quality-verified instant payout distributions to vessel crews upon docking.

---
*Developed with dedication to introducing data-driven stability, safety, and operational excellence to coastal communities and marine systems across Sri Lanka.*
