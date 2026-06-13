import streamlit as st
import joblib
import numpy as np
import os

# ==============================================================================
# 1. PAGE CONFIGURATION & STYLING
# ==============================================================================
st.set_page_config(
    page_title="Smart Home Energy Predictor",
    page_icon="⚡",
    layout="centered"
)

# Custom CSS styling for a cleaner dashboard UI look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    h1 { color: #1E3A8A; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Smart Home Daily Energy Cost Predictor")
st.markdown(
    "Adjust the usage hours and weather controls to see your estimated daily electricity costs update in real-time.")
st.markdown("---")


# ==============================================================================
# 2. LOAD THE TRAINED MACHINE LEARNING ENGINE
# ==============================================================================
@st.cache_resource
def load_ml_model():
    # Base filenames
    model_file = 'energy_regression_model.pkl'
    features_file = 'model_features.pkl'

    # Absolute path safety checkpoint to prevent path resolution glitches in PyCharm
    base_path = os.path.dirname(__file__) if os.path.dirname(__file__) else "."

    model = joblib.load(os.path.join(base_path, model_file))
    features = joblib.load(os.path.join(base_path, features_file))
    return model, features


try:
    model, feature_names = load_ml_model()
except Exception as e:
    st.error("❌ HOUP_ERROR: Unable to automatically load model binary files.")
    st.info(
        "💡 Solution: Ensure 'energy_regression_model.pkl' and 'model_features.pkl' are placed in the exact same PyCharm folder directory right next to this app.py file!")
    st.stop()

# ==============================================================================
# 3. INTERACTIVE SIDEBAR CONTROLS (WEATHER FEATURES)
# ==============================================================================
st.sidebar.header("🧠 Environment Variables")
st.sidebar.markdown("Simulate external weather parameters:")

input_values = {}

if 'temperature' in feature_names:
    input_values['temperature'] = st.sidebar.slider("🌡️ Outdoor Temperature (°F)", min_value=10.0, max_value=110.0,
                                                    value=65.0, step=1.0)
if 'humidity' in feature_names:
    input_values['humidity'] = st.sidebar.slider("💧 Humidity Level", min_value=0.0, max_value=1.0, value=0.6, step=0.01)
if 'cloudCover' in feature_names:
    input_values['cloudCover'] = st.sidebar.slider("☁️ Cloud Cover Fraction", min_value=0.0, max_value=1.0, value=0.3,
                                                   step=0.01)

# ==============================================================================
# 4. MAIN INTERFACE SLIDERS (APPLIANCE OPERATION HOURS)
# ==============================================================================
st.subheader("🔌 Daily Appliance Operational Hours")
st.markdown("Set how many hours each appliance runs during a 24-hour window:")

# Divide screen space into two equal, beautiful layout columns
col1, col2 = st.columns(2)

# Extract appliance columns dynamically from our feature list metadata
appliance_features = [feature for feature in feature_names if 'hours' in feature]

for index, app_feature in enumerate(appliance_features):
    # Formulate a beautiful clean title label from the column string name
    clean_label = app_feature.replace('_hours', '').replace('_', ' ').title()

    # Alternate rendering between left column and right column
    with col1 if index % 2 == 0 else col2:
        input_values[app_feature] = st.slider(
            label=f"⏳ {clean_label} (Hours)",
            min_value=0.0,
            max_value=24.0,
            value=2.0,  # Default starter runtime position
            step=0.5
        )

# Make sure hidden categorical/one-hot columns match our dataset constraints
for feature in feature_names:
    if feature not in input_values:
        input_values[feature] = 1.0  # Set weather_Clear baseline constant to True


# ==============================================================================
# 5. LIVE CALCULATION LOOP & POST-PROCESSING SAFETY GATE
# ==============================================================================
# Re-align input dictionary variables into the precise order the model expects
ordered_features_array = [input_values[feature] for feature in feature_names]

# Feed the feature array straight into the Linear Regression equation
raw_prediction = model.predict([ordered_features_array])[0]

# Lazy Genius Safety Gate: If data limits skew into negatives, default to base connection fees
safe_bill_prediction = max(50.00, raw_prediction)

st.markdown("---")
st.subheader("🔮 Projected Billing Output")

# FIXED Contrast: Large, bold, beautiful dark/light text that automatically pops on your screen!
st.write(f"### 💵 **Estimated Daily Cost:** ₹{safe_bill_prediction:.2f}")

# Active user suggestions banner - Perfectly aligned to prevent IndentationErrors
if safe_bill_prediction > 250.00:
    st.warning("⚠️ High Consumption Alert: High simulated power usage detected. Try lowering high-draw appliance runtimes to conserve energy costs.")
else:
    st.success("🌱 Efficient Configuration: Your simulated home runtime setup keeps energy expenses highly cost-effective!")