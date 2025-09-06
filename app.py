import streamlit as st
import joblib

# Load saved model and vectorizer
vectorizer = joblib.load("vectorizer.joblib")
model = joblib.load("spam_model.joblib")

st.set_page_config(page_title="Email Spam Detector", page_icon="📧")
st.title("📧 Email Spam Detector")

email_text = st.text_area("Paste email content:", height=250)

if st.button("Predict"):
    if not email_text.strip():
        st.warning("Please enter an email to classify.")
    else:
        # Vectorize using the loaded vectorizer
        X_new = vectorizer.transform([email_text])

        # Predict
        prediction = model.predict(X_new)[0]
        proba = model.predict_proba(X_new)[0][1]

        if prediction == 1:
            st.error(f"🚨 Spam detected! (Probability: {proba:.2%})")
        else:
            st.success(f"✅ This looks like a genuine email. (Spam probability: {proba:.2%})")
