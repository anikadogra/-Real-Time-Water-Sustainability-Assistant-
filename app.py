import streamlit as st
import pandas as pd
import plotly.express as px
import time

# Page Configuration
st.set_page_config(layout="wide", page_title="Water Sustainability Assistant")

# Title
st.title("💧 Real-Time Water Sustainability Assistant")

# Upload CSV File
uploaded_file = st.file_uploader("📂 Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Simulate loading screen for 2 seconds
    with st.spinner("Processing data... ⏳"):
        time.sleep(2)

    # Load the CSV File
    df = pd.read_csv(uploaded_file, parse_dates=["Date"])

    # Compute Average & Detect Anomalies
    avg_usage = df["Water_Usage_Liters"].mean()
    threshold = avg_usage * 2  # Anomalies are > 2x average usage
    df["Anomaly"] = df["Water_Usage_Liters"] > threshold

    # Layout: Data (Left), Graph (Right)
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("📋 Uploaded Data")
        st.dataframe(df)  # Display Data on the Left

    with col2:
        st.subheader("📊 Water Consumption Analysis")
        # Interactive Plotly Graph
        fig = px.line(df, x="Date", y="Water_Usage_Liters", markers=True, title="Daily Water Consumption",
                      labels={"Water_Usage_Liters": "Water Usage (Liters)", "Date": "Date"},
                      line_shape="linear")

        # Highlight Anomalies
        fig.add_scatter(x=df[df["Anomaly"]]["Date"], y=df[df["Anomaly"]]["Water_Usage_Liters"],
                        mode="markers", marker=dict(color="red", size=8), name="Anomalies")

        # Add Average Line
        fig.add_hline(y=avg_usage, line_dash="dash", line_color="green", annotation_text="Avg Usage")

        st.plotly_chart(fig, use_container_width=True)  # Display Graph on the Right

    # Summary at the Bottom
    st.subheader("📜 Summary")
    st.write(f"📊 **Average Daily Usage:** {avg_usage:.2f} liters")
    st.write(f"🚨 **Anomalous Days Detected:** {df['Anomaly'].sum()}")

else:
    st.info("🔼 Please upload a CSV file to analyze water usage data.")
