📧 Email Spam Detector

An NLP + Machine Learning project to classify emails as Spam 🚨 or Ham ✅ using TfidfVectorizer and Logistic Regression.

The model achieves 95%+ accuracy on the test dataset.

🚀 Features

Preprocesses raw email text

Uses TF-IDF for feature extraction

Trained with Logistic Regression classifier

Achieves 95%+ accuracy

Interactive Streamlit web app frontend

📂 Project Structure
email_spam_detector/
│── app.py                # Streamlit frontend
│── spam_model.joblib     # Trained ML model
│── vectorizer.joblib     # Fitted TF-IDF vectorizer (or use pipeline)
│── requirements.txt      # Dependencies
│── README.md             # Project documentation

⚡ Installation & Setup

Clone this repository:

git clone https://github.com/your-username/email_spam_detector.git
cd email_spam_detector


Create virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies:

pip install -r requirements.txt


Run Streamlit app:

streamlit run app.py

📊 Model Performance

Algorithm: Logistic Regression

Vectorization: TF-IDF

Accuracy: 95%+ on test data

Precision/Recall: Balanced, ensuring fewer false negatives

🎯 Example Predictions

Spam Example:

"Congratulations! You WON a FREE iPhone 🎉 Click here to claim"
→ 🚨 Spam

Ham Example:

"Reminder: Project meeting scheduled tomorrow at 10:30 AM"
→ ✅ Ham

🌐 Deployment

Can be deployed easily on Streamlit Cloud

Requirements handled via requirements.txt

📌 Future Improvements

Highlight suspicious keywords in emails (e.g., FREE, WIN, CLICK)

Add deep learning models (LSTMs / BERT) for comparison

Extend dataset with multilingual emails

✨ Developed as a Machine Learning + NLP project with a focus on real-world application.
