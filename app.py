import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ------------------ CONFIG ------------------
st.set_page_config(page_title="AI Guardian", layout="wide")

# ------------------ LOAD MODEL ------------------
MODEL_PATH = "finalmodels/02Autism_Prediction/best_autism_prediction_model.joblib"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# ------------------ MOCK PREPROCESS ------------------
# NOTE: Replace with real saved artifacts if available
def preprocess_input(data):
    # Minimal safe preprocessing (since artifacts not loaded)
    data = data.copy()

    # Example encoding (must match training ideally)
    binary_map = {"Yes": 1, "No": 0, "Male": 1, "Female": 0}

    for col in data.columns:
        if data[col].dtype == object:
            data[col] = data[col].map(binary_map).fillna(0)

    return data.values


# ------------------ STYLE ------------------
st.markdown("""
<style>
.big-button button {
    height: 150px;
    width: 100%;
    font-size: 18px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)


# ------------------ SESSION STATE ------------------
if "page" not in st.session_state:
    st.session_state.page = "home"


# ------------------ HOME ------------------
def home():
    st.title("🛡️ AI Guardian Platform")
    st.markdown("### Unified AI for Healthcare, Environment, Agriculture & Defense")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🌫️ Air Quality Monitoring", key="aqi"):
            st.session_state.page = "aqi"

    with col2:
        if st.button("🧠 Autism Prediction", key="autism"):
            st.session_state.page = "autism"

    with col3:
        if st.button("🌾 Crop Disease Detection", key="agri"):
            st.session_state.page = "agri"

    with col4:
        if st.button("🛰️ Drone Threat Detection", key="defense"):
            st.session_state.page = "defense"


# ------------------ AUTISM PAGE ------------------

def autism_page():
    st.title("🧠 Autism Prediction")

    st.markdown("### AQ-10 Screening Questions (0 = No, 1 = Yes)")

    # --- A1 to A10 Scores ---
    cols = st.columns(5)
    A_scores = {}

    for i in range(10):
        with cols[i % 5]:
            A_scores[f"A{i+1}_Score"] = st.selectbox(
                f"A{i+1}_Score",
                [0, 1],
                key=f"A{i+1}"
            )

    st.markdown("### Demographic & Medical Info")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider("Age", 1, 100, 25)
        gender = st.selectbox("Gender (0=Female,1=Male)", [0, 1])
        ethnicity = st.slider("Ethnicity", 0, 10, 5)

    with col2:
        jaundice = st.selectbox("Jaundice (0=No,1=Yes)", [0, 1])
        austim = st.selectbox("Family Autism (0=No,1=Yes)", [0, 1])
        used_app_before = st.selectbox("Used App Before", [0, 1])

    with col3:
        contry_of_res = st.slider("Country Code", 0, 100, 30)
        result = st.slider("Screening Score", -6.0, 16.0, 5.0)
        relation = st.selectbox("Relation", [0, 1, 2, 3, 4])

    # --- Predict ---
    if st.button("Predict"):

        input_dict = {
            **A_scores,
            "age": age,
            "gender": gender,
            "ethnicity": ethnicity,
            "jaundice": jaundice,
            "austim": austim,
            "contry_of_res": contry_of_res,
            "used_app_before": used_app_before,
            "result": result,
            "relation": relation
        }

        input_df = pd.DataFrame([input_dict])

        try:
            pred = model.predict(input_df)[0]
            prob = model.predict_proba(input_df)[0].max()

            if pred == 1:
                st.error(f"⚠️ Autism Likely (Confidence: {prob:.2f})")
            else:
                st.success(f"✅ No Autism Detected (Confidence: {prob:.2f})")

        except Exception as e:
            st.error(f"Model error: {e}")

    if st.button("⬅ Back"):
        st.session_state.page = "home"
# def autism_page():
#     st.title("🧠 Autism Prediction")

#     col1, col2 = st.columns(2)

#     with col1:
#         age = st.number_input("Age", 1, 100, 25)
#         gender = st.selectbox("Gender", ["Male", "Female"])
#         jaundice = st.selectbox("Jaundice at Birth", ["Yes", "No"])

#     with col2:
#         family_history = st.selectbox("Family History of Autism", ["Yes", "No"])
#         result = st.slider("Screening Score", 0.0, 100.0, 50.0)

#     if st.button("Predict"):

#         input_df = pd.DataFrame([{
#             "age": age,
#             "gender": gender,
#             "jaundice": jaundice,
#             "autism": family_history,
#             "result": result
#         }])

#         X = preprocess_input(input_df)

#         try:
#             pred = model.predict(X)[0]
#             prob = model.predict_proba(X)[0].max()

#             if pred == 1:
#                 st.error(f"⚠️ Autism Likely (Confidence: {prob:.2f})")
#             else:
#                 st.success(f"✅ No Autism Detected (Confidence: {prob:.2f})")

#         except Exception as e:
#             st.error(f"Model error: {e}")

#     if st.button("⬅ Back"):
#         st.session_state.page = "home"


# ------------------ AQI PAGE ------------------
def aqi_page():
    st.title("🌫️ Air Quality Monitoring")

    city = st.text_input("Enter City", "Hyderabad")

    if st.button("Check AQI"):
        st.info("🚧 Connect to Indian Govt AQI API here")

    if st.button("⬅ Back"):
        st.session_state.page = "home"


# ------------------ AGRI PAGE ------------------
def agri_page():
    st.title("🌾 Wheat Disease Detection")

    file = st.file_uploader("Upload Crop Image")

    if file:
        st.image(file)
        st.success("🚧 Model integration pending")

    if st.button("⬅ Back"):
        st.session_state.page = "home"


# ------------------ DEFENSE PAGE ------------------
def defense_page():
    st.title("🛰️ Drone / Aircraft Detection")

    file = st.file_uploader("Upload Image/Video")

    if file:
        st.success("🚧 Object detection model pending")

    if st.button("⬅ Back"):
        st.session_state.page = "home"


# ------------------ ROUTER ------------------
if st.session_state.page == "home":
    home()
elif st.session_state.page == "autism":
    autism_page()
elif st.session_state.page == "aqi":
    aqi_page()
elif st.session_state.page == "agri":
    agri_page()
elif st.session_state.page == "defense":
    defense_page()

