import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')





st.header("📊 Data Visualization")

st.subheader("Dataset")

data = pd.read_csv("Data/phishing_url_svm_ready.csv")

show_data = st.checkbox("Show Dataset")
if show_data:
    st.dataframe(data)

    st.markdown("---")






st.subheader("Dataset Overview")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Number of Records",
        data.shape[0])

with col2:
    st.metric(
        "Number of Features",
         data.shape[1])

st.markdown("---")



st.subheader("📋 Column Details")

column_details = {
    "Link Density": "Ratio of links present in a webpage compared with the webpage content.",
    "External Links Count": "Number of links pointing to external websites.",
    "Internal Links Count": "Number of links pointing to pages within the same website.",
    "External IP Count": "Number of external links or resources that use an IP address.",
    "HTTP Count": "Number of HTTP links or resources found on the webpage.",
    "HTTPS Count": "Number of HTTPS links or resources found on the webpage.",
    "Non Count": "Number of links or resources that do not use HTTP or HTTPS.",
    "External Iframes Count": "Number of iframes loading content from external websites.",
    "Hidden Iframes Count": "Number of hidden iframes detected on the webpage.",
    "If HTTPS": "Indicates whether the URL uses HTTPS. 1 = Yes, 0 = No.",
    "Country": "Country associated with the website or server information.",
    "Organization": "Organization or hosting provider associated with the website or IP.",
    "Certificate": "Information about the SSL/TLS certificate of the website.",
    "Whois_country": "Country recorded in the WHOIS registration information of the domain.",
    "Certificate Validity Days": "Number of days for which the SSL/TLS certificate is valid.",
    "Domain Validity Days": "Number of days for which the domain registration is valid.",
    "URL Length": "Total number of characters in the URL.",
    "URL Dot Count": "Number of dot (.) characters in the URL.",
    "URL Hyphen Count": "Number of hyphen (-) characters in the URL.",
    "URL Slash Count": "Number of slash (/) characters in the URL.",
    "URL Digit Count": "Number of numerical digits (0–9) in the URL.",
    "URL Special Char Count": "Number of special characters in the URL.",
    "URL Has IP": "Indicates whether the URL directly contains an IP address. 1 = Yes, 0 = No."
}


column_df = pd.DataFrame(
    column_details.items(),
    columns=["Column", "Description"]
)

st.dataframe(column_df, use_container_width=True)

st.markdown("---")






st.subheader("Statistics")

st.dataframe(data.describe())

st.markdown("---")






st.title("Data Analysis")


# Distribution of Target Variable

fig = plt.figure(figsize=(7, 5))

data['type'].value_counts().plot(kind='bar')

plt.xlabel('URL Type')
plt.ylabel('Count')
plt.title('Distribution of Phishing and Benign URLs')

plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.markdown("---")






# Distribution of Numerical Features

numerical_features = data.select_dtypes(
    include=['int64', 'float64']
).columns

fig, axes = plt.subplots(
    nrows=(len(numerical_features) + 2) // 3,
    ncols=3,
    figsize=(16, 14)
)

axes = axes.flatten()

for i, feature in enumerate(numerical_features):
    axes[i].hist(
        data[feature].dropna(),
        bins=20
    )
    
    axes[i].set_title(feature)
    axes[i].set_xlabel(feature)
    axes[i].set_ylabel('Frequency')

# Hide unused plots
for i in range(len(numerical_features), len(axes)):
    axes[i].set_visible(False)

fig.suptitle(
    'Distribution of Numerical Features',
    fontsize=16
)

fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.markdown("---")






# Boxplots - 2 × 3 Layout

features = [
    'URL Length',
    'URL Dot Count',
    'URL Hyphen Count',
    'URL Slash Count',
    'URL Digit Count',
    'URL Special Char Count'
]

fig, axes = plt.subplots(
    nrows=2,
    ncols=3,
    figsize=(14, 8)
)

axes = axes.flatten()

for i, feature in enumerate(features):

    data.boxplot(
        column=feature,
        by='type',
        ax=axes[i]
    )

    axes[i].set_title(feature)
    axes[i].set_xlabel('URL Type')
    axes[i].set_ylabel(feature)

# Remove pandas' automatic overall title
plt.suptitle('')

# Main title
fig.suptitle(
    'URL Feature Distribution by URL Type',
    fontsize=16,
    y=1.02
)

fig.tight_layout()

st.pyplot(fig)

plt.close(fig)

st.markdown("---")






# Correlation Heatmap

fig = plt.figure(figsize=(14, 10))

correlation = data.select_dtypes(
    include=['int64', 'float64']
).corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('Correlation Heatmap of Numerical Features')
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.markdown("---")




st.subheader("🔍 Key Insights")

st.markdown("""
- 📊 Phishing and benign URLs are almost equally distributed.
- 📈 Most numerical features have lower values, with some high-value observations.
- 🔗 URL length and special characters vary between the two classes.
- 🔢 URL digit counts show differences between phishing and benign URLs.
- 📍 URL dot and slash counts show considerable overlap between the classes.
- ⚠️ Some features contain outliers.
- 🔄 Some numerical features are strongly correlated with each other.
- 🛡️ The graphs show that multiple features together can help distinguish phishing and benign URLs.
""")




