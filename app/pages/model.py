import streamlit as st
import pandas as pd
import joblib

st.header("🎣🔗 Phishing URL Detection")

st.markdown(
    "Enter the website characteristics below to predict "
    "whether the URL is phishing or benign."
)


# Load trained model
model = joblib.load(r"C:\Users\Lenovo\Documents\Cyber Square\Work\Phishing URL Detection (SVM)\Model\phishing_svm_model.joblib")




# --------------------------------------------------
# URL Characteristics
# --------------------------------------------------

st.subheader("🔗 URL Characteristics")

col1, col2, col3 = st.columns(3)

with col1:
    url_length = st.number_input(
        "URL Length",
        min_value=0,
        value=50
    )

with col2:
    url_dot_count = st.number_input(
        "URL Dot Count",
        min_value=0,
        value=2
    )

with col3:
    url_hyphen_count = st.number_input(
        "URL Hyphen Count",
        min_value=0,
        value=0
    )

col4, col5, col6 = st.columns(3)

with col4:
    url_slash_count = st.number_input(
        "URL Slash Count",
        min_value=0,
        value=2
    )

with col5:
    url_digit_count = st.number_input(
        "URL Digit Count",
        min_value=0,
        value=0
    )

with col6:
    url_special_char_count = st.number_input(
        "URL Special Char Count",
        min_value=0,
        value=5
    )

url_has_ip = st.selectbox(
    "URL Has IP",
    options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

# --------------------------------------------------
# Link & Webpage Characteristics
# --------------------------------------------------

st.subheader("🌐 Link & Webpage Characteristics")

col1, col2, col3 = st.columns(3)

with col1:
    link_density = st.number_input(
        "Link Density",
        min_value=0.0,
        value=0.1
    )

with col2:
    external_links = st.number_input(
        "External Links Count",
        min_value=0,
        value=1
    )

with col3:
    internal_links = st.number_input(
        "Internal Links Count",
        min_value=0,
        value=1
    )

col4, col5, col6 = st.columns(3)

with col4:
    external_ip = st.number_input(
        "External IP Count",
        min_value=0,
        value=0
    )

with col5:
    http_count = st.number_input(
        "HTTP Count",
        min_value=0,
        value=1
    )

with col6:
    https_count = st.number_input(
        "HTTPS Count",
        min_value=0,
        value=1
    )

col7, col8, col9 = st.columns(3)

with col7:
    non_count = st.number_input(
        "Non Count",
        min_value=0,
        value=0
    )

with col8:
    external_iframes = st.number_input(
        "External Iframes Count",
        min_value=0,
        value=0
    )

with col9:
    hidden_iframes = st.number_input(
        "Hidden Iframes Count",
        min_value=0,
        value=0
    )

if_https = st.selectbox(
    "If HTTPS",
    options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

# --------------------------------------------------
# Domain & Certificate Information
# --------------------------------------------------

st.subheader("🌍 Domain & Certificate Information")

col1, col2 = st.columns(2)

with col1:
    country = st.text_input(
        "Country",
        value="US"
    )

with col2:
    organization = st.text_input(
        "Organization",
        value="Unknown"
    )

col3, col4 = st.columns(2)

with col3:
    certificate = st.text_input(
        "Certificate",
        value="Valid"
    )

with col4:
    whois_country = st.text_input(
        "Whois_country",
        value="US"
    )

col5, col6 = st.columns(2)

with col5:
    certificate_validity = st.number_input(
        "Certificate Validity Days",
        min_value=0.0,
        value=90.0
    )

with col6:
    domain_validity = st.number_input(
        "Domain Validity Days",
        min_value=0.0,
        value=7671.0
    )

# --------------------------------------------------
# Prediction
# --------------------------------------------------

st.divider()

if st.button("🔍 Predict", use_container_width=True):

    input_data = pd.DataFrame({
        "Link Density": [link_density],
        "External Links Count": [external_links],
        "Internal Links Count": [internal_links],
        "External IP Count": [external_ip],
        "HTTP Count": [http_count],
        "HTTPS Count": [https_count],
        "Non Count": [non_count],
        "External Iframes Count": [external_iframes],
        "Hidden Iframes Count": [hidden_iframes],
        "If HTTPS": [if_https],
        "Country": [country],
        "Organization": [organization],
        "Certificate": [certificate],
        "Whois_country": [whois_country],
        "Certificate Validity Days": [certificate_validity],
        "Domain Validity Days": [domain_validity],
        "URL Length": [url_length],
        "URL Dot Count": [url_dot_count],
        "URL Hyphen Count": [url_hyphen_count],
        "URL Slash Count": [url_slash_count],
        "URL Digit Count": [url_digit_count],
        "URL Special Char Count": [url_special_char_count],
        "URL Has IP": [url_has_ip]
    })

    # Prediction
    prediction = model.predict(input_data)[0]

    # --------------------------------------------------
    # Display Result
    # --------------------------------------------------

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("🚨 Phishing URL Detected!")
    else:
        st.success("🛡️ Benign URL")



        
