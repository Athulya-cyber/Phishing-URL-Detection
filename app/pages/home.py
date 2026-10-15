import streamlit as st

st.title("🎣🔗 Phishing URL Detection")

st.header("Phishing URL Detection using SVM Classifier")

st.write("""
Phishing websites are fraudulent websites designed to imitate legitimate websites and deceive users into providing sensitive information. 

Detecting phishing websites manually can be difficult because phishing URLs may closely resemble legitimate URLs. 
Machine learning can help automate this process by learning patterns from URL and website-related features. 
This project uses an SVM classifier to distinguish between phishing and benign URLs.
""")

st.subheader("📊 Dataset Overview")

st.write("""
The dataset contains information about URLs and several characteristics associated with the corresponding websites. 
These characteristics include link information, HTTP/HTTPS usage, IP-related information, iframe information, 
country and organization details, SSL certificate information, WHOIS information, and URL-based characteristics.

The target variable **type** predicts, whether a URL is phishing or bengin.
""")

st.subheader("🤖 Project Objective")

st.write("""
The main objective of this project is to develop a machine learning model using Support Vector Machine (SVM) 
to classify URLs as phishing or benign based on their characteristics.
""")

st.info("Use the navigation menu on the left to explore each section.")

