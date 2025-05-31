import pandas as pd
import numpy as np
from datetime import datetime, timedelta

import streamlit as st
import plotly.express as px

def generate_scada_data(num_turbines=5, days=1, seed=42):
    np.random.seed(seed)
    
    data = []
    for day_offset in range(days):
        current_date = datetime.strptime("2025-05-23", "%Y-%m-%d") + timedelta(days=day_offset)
        start_time = current_date.replace(hour=12, minute=0, second=0)
        end_time = current_date.replace(hour=23, minute=50, second=0)
        timestamps = pd.date_range(start=start_time, end=end_time, freq='10min')

        for turbine_id in range(1, num_turbines + 1):
            for ts in timestamps:
                wind_speed = np.clip(np.random.normal(12, 3), 0, 25)
                rpm = np.random.normal(1500, 50)
                temp = np.random.normal(55, 5)
                power = min(wind_speed * 80, 2500) + np.random.normal(0, 50)
                data.append([f"Turbine-{turbine_id}", ts, wind_speed, rpm, temp, power])

    return pd.DataFrame(data, columns=['TURBINE_ID', 'TIME_STAMP', 'WIND_SPEED', 'RPM', 'TEMPERATURE', 'POWER'])

def generate_alerts(df):
    alerts = []
    for _, row in df.iterrows():
        if row['TEMPERATURE'] > 60:
            alerts.append([row['TURBINE_ID'], row['TIME_STAMP'], "High Temperature"])
        if row['WIND_SPEED'] < 3:  # Assuming you meant "Low Wind Speed" when wind speed is too low
            alerts.append([row['TURBINE_ID'], row['TIME_STAMP'], "Low Wind Speed"])
    return pd.DataFrame(alerts, columns=['TURBINE_ID', 'TIME_STAMP', 'ALERT'])

st.title("Scada Dashboard")
df = generate_scada_data(num_turbines=10,days=7,seed = 42)
alerts = generate_alerts(df)

selected_turbine = st.selectbox('Select a turbine',df['TURBINE_ID'].unique())
turbine_df = df[df['TURBINE_ID']==selected_turbine]

st.subheader("Power Output")
st.plotly_chart(px.line(turbine_df,x="TIME_STAMP",y="POWER"))

st.subheader("Wind Speed")
st.plotly_chart(px.line(turbine_df,x="TIME_STAMP",y="WIND_SPEED"))

st.subheader("Alerts")
st.dataframe(alerts[alerts['TURBINE_ID'] == selected_turbine])

#streamlit run scada_dashboard.py




