import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Real-Time Water Sustainability Assistant 🌊")

# Upload CSV File
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load CSV Data
    df = pd.read_csv(uploaded_file, parse_dates=["Date"])

    # Show Data
    st.subheader("Uploaded Data")
    st.write(df)

    # Compute Anomalies
    avg_usage = df["Water_Usage_Liters"].mean()
    threshold = avg_usage * 2  # Define anomaly threshold
    df["Anomaly"] = df["Water_Usage_Liters"] > threshold

    # Plot the Graph
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Date"], df["Water_Usage_Liters"], marker='o', color='blue', label="Daily Usage")
    ax.scatter(df[df["Anomaly"]]["Date"], df[df["Anomaly"]]["Water_Usage_Liters"], color='red', label="Anomalies", zorder=3)
    ax.axhline(y=avg_usage, color='green', linestyle='dashed', label="Avg Usage")
    ax.set_xlabel("Date")
    ax.set_ylabel("Water Usage (Liters)")
    ax.set_title("Daily Water Consumption")
    ax.legend()
    plt.xticks(rotation=45)

    # Display Graph in Streamlit
    st.pyplot(fig)

    # Show Anomalies
    st.subheader("Anomalies Detected 🚨")
    st.write(df[df["Anomaly"]])

    # Summary Statistics
    st.subheader("Summary")
    st.write(f"📊 **Average Daily Usage:** {avg_usage:.2f} liters")
    st.write(f"🔴 **Anomalous Days Detected:** {df['Anomaly'].sum()}")

else:
    st.info("Please upload a CSV file to analyze water usage data.")
