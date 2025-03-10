# AI-Driven Real-Time Demand Forecasting with LSTMs, Kafka & Streamlit

## Project Overview
This project implements **Deep Learning models (LSTM, Transformer-based models)** for forecasting **retail sales trends** and integrates with **Apache Kafka for real-time data ingestion**. The results are displayed in an **interactive Streamlit dashboard**.

## Tech Stack
- **Deep Learning:** PyTorch (LSTM-based forecasting)
- **Streaming Pipeline:** Apache Kafka (Real-time sales data ingestion)
- **Visualization:** Streamlit (Interactive Dashboard)
- **Data Processing:** Pandas, NumPy, MinMaxScaler

## Features Implemented
✅ LSTM-based Time Series Forecasting  
✅ Modular architecture with multiple independent components  
✅ Integration with **Real-time Apache Kafka Pipeline**  
✅ Streamlit Dashboard for Visualization  

## How to Run the Project
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/bruteai/ai-forecasting.git
cd ai-forecasting
```
### 2️⃣ Install Dependencies
```sh
pip install torch pandas numpy matplotlib seaborn streamlit kafka-python scikit-learn
```
### 3️⃣ Start the Kafka Consumer and Streamlit App
```sh
streamlit run dashboard/streamlit_dashboard.py
```

## 📂 Project Structure
```
📁 ai-forecasting
│── data/                  # Dataset (CSV files)
│── data_processing/        # Data processing modules
│   ├── data_processing.py  
│── models/                 # Deep learning model scripts
│   ├── lstm_model.py       
│── streaming/              # Kafka integration
│   ├── kafka_consumer.py   
│── dashboard/              # Streamlit dashboard
│   ├── streamlit_dashboard.py
│── README.md               # Project Documentation
```

## Future Enhancements
- Implement **Transformer-based models (BERT for Time Series Forecasting)**  
- Deploy as a **cloud-based API for retailers**  
- Integrate with **real-time stock inventory**  

---

💡 **Contributions Welcome!** If you'd like to improve this project, feel free to open a pull request.
