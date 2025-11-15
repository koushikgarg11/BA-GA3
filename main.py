import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("📂 Dynamic Dataset Explorer")
st.write("Upload any dataset (CSV) and explore it interactively.")

# File Upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read data
    df = pd.read_csv(uploaded_file)

    # Show preview
    st.subheader("🔎 Data Preview")
    st.dataframe(df.head())

    # Basic Info
    st.subheader("📑 Dataset Summary")
    st.write(df.describe(include="all"))

    # Column Selection
    st.sidebar.header("Visualization Controls")
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
    selected_x = st.sidebar.selectbox("Select X-axis", options=numeric_cols)
    selected_y = st.sidebar.selectbox("Select Y-axis", options=numeric_cols)

    # Plot
    if selected_x and selected_y:
        st.subheader("📊 Scatter Plot")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=selected_x, y=selected_y, ax=ax)
        st.pyplot(fig)

    # Download Option
    st.subheader("⬇️ Export Data")
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Cleaned CSV", csv, "dataset.csv", "text/csv")

else:
    st.info("Please upload a CSV file to get started.")
