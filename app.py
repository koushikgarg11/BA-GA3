import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# App Title
st.set_page_config(page_title="Dynamic Dataset Explorer", layout="wide")
st.title("📂 Dynamic Dataset Explorer")
st.markdown("Upload any CSV file and explore it interactively with charts, summaries, and export options.")

# File Upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Load Data
    df = pd.read_csv(uploaded_file)

    # Show Preview
    st.subheader("🔎 Data Preview")
    st.dataframe(df.head())

    # Show Summary
    st.subheader("📑 Dataset Summary")
    st.write(df.describe(include="all"))

    # Sidebar Controls
    st.sidebar.header("📊 Chart Controls")
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
    all_cols = df.columns.tolist()

    chart_type = st.sidebar.selectbox("Choose chart type", ["Scatter", "Line", "Bar", "Histogram"])
    x_axis = st.sidebar.selectbox("X-axis", options=numeric_cols)
    y_axis = st.sidebar.selectbox("Y-axis", options=numeric_cols)

    # Plotting
    st.subheader("📈 Visualization")
    fig, ax = plt.subplots()

    if chart_type == "Scatter":
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif chart_type == "Line":
        sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif chart_type == "Bar":
        sns.barplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif chart_type == "Histogram":
        sns.histplot(data=df[x_axis], bins=30, kde=True, ax=ax)

    st.pyplot(fig)

    # Export Button
    st.subheader("⬇️ Export Data")
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, "processed_data.csv", "text/csv")

else:
    st.info("👈 Upload a CSV file to begin exploring.")
