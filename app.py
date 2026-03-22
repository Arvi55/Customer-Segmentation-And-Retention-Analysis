import streamlit as st
import numpy as np
import pickle


model = pickle.load(open('churn_model.pkl', 'rb'))


st.set_page_config(
    page_title="Churn Prediction App",
    page_icon="📊",
    layout="centered"
)


st.sidebar.title("📌 About This Project")

st.sidebar.write("""
This app predicts whether a customer is likely to churn using a Machine Learning model based on RFM analysis.
""")

st.sidebar.markdown("### 📥 Input Features")

st.sidebar.write("""
- **Recency** → Days since the customer's last purchase  
- **Frequency** → Total number of purchases made  
- **Monetary** → Total amount spent by the customer  
""")


st.title("📊 Customer Churn Prediction")

st.markdown("Enter customer details below:")


recency = st.number_input(
    "📅 Recency (days since last purchase)",
    min_value=0,
    value=30
)

frequency = st.number_input(
    "🔁 Frequency (number of purchases)",
    min_value=0,
    value=5
)

monetary = st.number_input(
    "💰 Monetary (total spend)",
    min_value=0.0,
    value=500.0
)


if st.button("🔍 Predict Churn"):
    input_data = np.array([[recency, frequency, monetary]])
    probability = model.predict_proba(input_data)[0][1]
    threshold = 0.2
    
    prediction = 1 if probability > threshold else 0
    st.subheader("📈 Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk of Churn")
    else:
        st.success("✅ Customer Likely to Stay")

    
    st.write(f"**Churn Probability:** {probability:.2f}")

   
    st.progress(int(probability * 100))

   
    st.subheader("🧠 Interpretation")

    if probability > 0.7:
        st.write("🔴 Customer is highly likely to churn. Immediate retention action recommended.")
    elif probability > 0.4:
        st.write("🟡 Customer is at moderate risk. Consider engagement strategies.")
    else:
        st.write("🟢 Customer is low risk.")


# Footer
# -----------------------------
st.markdown("---")
st.caption("Built using Machine Learning & Streamlit 🚀")
