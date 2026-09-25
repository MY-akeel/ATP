import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import requests
import time

# --- SETUP MOCK AI ENGINE AND API ---
class ColdChainEngine:
    def __init__(self):
        self.eta_model = xgb.XGBRegressor(n_estimators=10, max_depth=3, learning_rate=0.1)
        X = np.array([[0.5, 120.0, 0.1], [2.5, 180.0, 0.6], [1.2, 90.0, 0.3]])
        y = np.array([12.0, 5.0, 10.5]) # Speeds in knots
        self.eta_model.fit(X, y)
        
    def calculate_eta(self, distance_nm, wave_h, wave_dir, current_spd):
        features = np.array([[wave_h, wave_dir, current_spd]])
        predicted_speed = max(float(self.eta_model.predict(features).item()), 2.0)
        return round(distance_nm / predicted_speed, 1)


@st.cache_data
def get_live_ocean_data(lat, lon):
    url = "https://open-meteo.com"
    params = {"latitude": lat, "longitude": lon, "hourly": ["wave_height", "wave_direction"], "currents_hourly": ["current_speed"], "forecast_days": 1}
    try:
        res = requests.get(url, params=params, timeout=5).json()
        return res["hourly"]["wave_height"], res["hourly"]["wave_direction"], res["currents_hourly"]["current_speed"]
    except Exception:
        return 1.2, 140.0, 0.3 # Fallback

engine = ColdChainEngine()

# --- STREAMLIT DASHBOARD UI ---
st.set_page_config(page_title="ColdChain AI Dashboard", page_icon="⚓", layout="wide")

st.title("⚓ ColdChain AI: Catch-to-Market Optimization Control Hub")
st.markdown("### Real-Time Fleet Tracking & Predictive Logistics (Dialog Innovation Challenge Prototype)")
st.write("---")

# Top KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Vessels Monitored", "14 Boats")
col2.metric("Post-Harvest Spoilage Rate", "4.2%", "-18.5% MoM", delta_color="inverse")
col3.metric("Avg. Cold Hold Temp", "1.8°C", "Stable")
col4.metric("Dialog Ideamart Dispatches Today", "42 Alerts")

# Sidebar Configuration
st.sidebar.header("🚢 Vessel Operational Telemetry")
vessel_select = st.sidebar.selectbox("Select Target Fishing Vessel", ["Nil Diya 03", "Ocean Queen", "Sea Cruiser 09"])
distance = st.sidebar.slider("Distance to Harbor (Nautical Miles)", 10.0, 200.0, 45.0)
hold_temp = st.sidebar.slider("Current Cold Hold Temperature (°C)", -2.0, 10.0, 1.5)

# Coordinate dictionary for simulated live GPS positions near Sri Lankan fishing ports
coords = {
    "Nil Diya 03": (5.50, 80.50),      # South of Matara
    "Ocean Queen": (5.85, 81.25),     # South-East of Hambantota
    "Sea Cruiser 09": (6.10, 79.70)    # West of Colombo / Dikowita
}
lat, lon = coords[vessel_select]

# Fetch Real-time Marine Metrics
wave_h, wave_dir, current_spd = get_live_ocean_data(lat, lon)

# --- NEW: MAP VISUALIZATION ANCHOR ---
st.subheader("🗺️ Live Fleet GPS Tracker & Geofence Map")
# Format a DataFrame specifically structured for Streamlit's native map UI mapping requirements
map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
st.map(map_data, zoom=7)
st.write("")

# Main Dashboard Content layout
left_col, right_col = st.columns(2)

with left_col:
    st.subheader(f"📊 Live Diagnostics: {vessel_select}")
    
    predicted_eta = engine.calculate_eta(distance, wave_h, wave_dir, current_spd)
    spoilage_status = "🔴 HIGH RISK" if hold_temp > 4.0 else "🟢 SAFE (Premium Quality)"
    
    st.info(f"📍 **Vessel Current GPS Coordinates:** Latitude `{lat}`, Longitude `{lon}`")
    
    metric_a, metric_b = st.columns(2)
    metric_a.markdown(f"🤖 **AI Predicted Time to Dock:** `{predicted_eta} Hours`")
    metric_b.markdown(f"🌡️ **Spoilage Risk Metric:** {spoilage_status}")
    
    st.write("")
    st.markdown("#### Live Environmental Features Ingested by AI Engine:")
    env_df = pd.DataFrame({
        "Feature Parameter": ["Wave Height", "Wave Direction", "Ocean Current Speed"],
        "Live Ingested Value": [f"{wave_h} meters", f"{wave_dir}°", f"{current_spd} m/s"]
    })
    st.table(env_df)

with right_col:
    st.subheader("💬 Dialog API Integrations")
    st.write("Trigger instant grid optimization using Dialog Axiata infrastructure.")
    
    phone_number = st.text_input("Exporter/Truck Operator Mobile Number", value="0771234567")
    
    if st.button("🚀 Dispatch Pre-emptive Ideamart SMS Alert"):
        with st.spinner("Broadcasting routing payload to Dialog Gateways..."):
            time.sleep(1) # Network latency simulation
            
            sms_payload = {
                "message": f"ALERT: Vessel [{vessel_select}] docking in {predicted_eta}h. Catch Quality: {spoilage_status}. Assign cold trucks to harbor berth.",
                "destinationAddress": f"tel:94{phone_number[1:]}"
            }
            
            st.success("✅ Ideamart API Payload Forwarded Successfully!")
            st.json(sms_payload)

st.write("---")
st.caption("Developed for the Dialog Innovation Challenge. Built with Streamlit, XGBoost, and Open-Meteo APIs.")
