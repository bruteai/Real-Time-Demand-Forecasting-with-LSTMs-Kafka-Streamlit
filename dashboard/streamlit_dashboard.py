import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_processing.data_processing import DataProcessor

# Load data
processor = DataProcessor("../data/sales_data.csv")
df = processor.load_data()

st.title("📊 AI-Driven Real-Time Demand Forecasting")

st.line_chart(df["Sales"])

st.subheader("Sales Trends Analysis")
fig, ax = plt.subplots()
df["Sales"].plot(ax=ax, color="blue", label="Sales Data")
ax.set_title("Sales Over Time")
st.pyplot(fig)
