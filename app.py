import streamlit as st
import pandas as pd
import pickle
import numpy as np

# 1. Load Model AND Column Names
# We wrap this in a function so it runs fast
@st.cache_resource
def load_artifacts():
    with open('churn_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('model_columns.pkl', 'rb') as f:
        model_columns = pickle.load(f)
    return model, model_columns

try:
    model, model_columns = load_artifacts()
except FileNotFoundError:
    st.error("❌ Files not found! Make sure you ran Step 1 to save 'churn_model.pkl' and 'model_columns.pkl'.")
    st.stop()

# 2. App Layout
st.title("🌲 Telecom Churn Predictor (Random Forest)")
st.markdown("Adjust the customer details to see the **Risk of Churn**.")

# 3. User Inputs (Side-by-side)
col1, col2 = st.columns(2)

with col1:
    tenure = st.slider("Tenure (Months)", 0, 72, 12)
    monthly_charges = st.number_input("Monthly Charges ($)", 18.0, 120.0, 70.0)
    total_charges = st.number_input("Total Charges ($)", 0.0, 9000.0, 500.0)
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

with col2:
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    payment_method = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    
    # Add other simple Yes/No features if your model uses them
    tech_support = st.selectbox("Tech Support", ["Yes", "No"])
    online_security = st.selectbox("Online Security", ["Yes", "No"])

# 4. Preprocessing Function (The Magic Part)
def preprocess_input():
    # A. Create a dict with the raw user data
    input_data = {
        'tenure': tenure,
        'monthly_charges': monthly_charges,
        'total_charges': total_charges,
        # Map Yes/No to 1/0 immediately
        'paperless_billing': 1 if paperless_billing == 'Yes' else 0,
        'tech_support': 1 if tech_support == 'Yes' else 0,
        'online_security': 1 if online_security == 'Yes' else 0,
        # For One-Hot columns, we just pass the text value for now
        'contract': contract,
        'internet_service': internet_service,
        'payment_method': payment_method
    }
    
    # B. Convert to DataFrame
    df = pd.DataFrame([input_data])
    
    # C. Apply One-Hot Encoding (get_dummies) just like in training
    df = pd.get_dummies(df)
    
    # D. Align with Training Columns (The Critical Fix)
    # This ensures the app has exactly the same columns as the model, in the same order.
    # Missing columns (e.g., if user selected DSL, 'Fiber' column is missing) are filled with 0.
    df = df.reindex(columns=model_columns, fill_value=0)
    
    return df

# 5. Prediction Logic
if st.button("Predict Churn Risk"):
    user_input = preprocess_input()
    
    # Get the probability (0 to 1)
    prediction_prob = model.predict_proba(user_input)[0][1]
    prediction_class = model.predict(user_input)[0]
    
    # Display Result
    st.divider()
    col_left, col_right = st.columns([1, 2])
    
    with col_left:
        # Gauge Chart logic (simple metric)
        st.metric(label="Churn Probability", value=f"{prediction_prob:.1%}")
    
    with col_right:
        if prediction_prob > 0.5:
            st.error(f"⚠️ **High Risk!** This customer is likely to leave.")
            st.progress(prediction_prob) # Red progress bar
        else:
            st.success(f"✅ **Safe.** This customer is likely to stay.")
            st.progress(prediction_prob) # Green progress bar