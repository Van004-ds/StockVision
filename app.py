##importing required libraries 

import streamlit as st
import pandas as pd 
import plotly.express as px

#setting up page configuratoin 
st.set_page_config(
    page_title="StockVision",
    page_icon="📈",
    layout="wide"
)
st.title("📈Stock Vision")
# st.write("Welcome to Stock Vision V1")
st.caption(
    "A Financial Analytics Dashboard for Stock Performance and Risk Analysis."
)


 # lodaing data 


df = pd.read_csv("data/processed/enginersin_features.csv")
st.sidebar.title("Srock Information")
# st.sidebar.write("**Ticker:** ENGINERSIN.NS")
selected_stock = st.sidebar.selectbox(
    "Select Stock",
   [
    "ENGINERSIN.NS",
    "POLYCAB.NS",
    "PARAS.NS"
]
)

#sidebar 
st.sidebar.header("📋 Dataset Summary")
st.sidebar.write(f"**Selected:** {selected_stock}")
st.sidebar.write(f"** Trading Days :** {len(df)}")
st.sidebar.write(f"**From:** {df['Date'].iloc[0]}")
st.sidebar.write(f"**To:** {df['Date'].iloc[-1]}")
st.sidebar.write(f"**Latest Close:** ₹{df['Close'].iloc[-1]:.2f}")
# st.subheader("feature engineered dataset")
# st.dataframe(df.head())
with st.expander("view feature engineered dataset"):
    st.dataframe(df)
st.header("Dashboard overview")



#kpi section :
st.divider()

st.subheader("📊 Key Metrics")
st.header(f"selected stock:{selected_stock}")
col1, col2, col3 , col4 = st.columns(4)
current_price = df["Close"].iloc[-1]
col1.metric(
    label="Current_price ",
    value=f"₹{current_price: .2f}"
)
current_rsi = df["RSI"].iloc[-1]
col2.metric(label="Current RSI",
            value=f"{current_rsi: .2f}")
max_drawdown = df["drawdown"].min()
col3.metric(label="Max Drawdown",
            value=f"{max_drawdown: .2%}")
current_volatility  = df["rolling_volatility"].iloc[-1]
col4.metric(label="Rolling Volatility",
    value=f"{current_volatility:.2%}")
st.header("Price & Moving Averages")
st.subheader("Closing Price")
fig = px.line(df,x ="Date",y= ["Close","MA_20","MA_50"],
               title="ENGINERSIN.NS Price with Moving Averages",
    labels={
        "value": "Price (₹)",
        "variable": "Indicator"
    } )
# price

# st.plotly_chart(fig,use_container_width=True)
fig.update_traces(
    hovertemplate= "<b> %{fullData.name}</b><br>"
      "<b> Date: </b> %{x}<br>"
    "<b>Price:</b> ₹%{y:.2f}<extra></extra>"
    )
fig.update_layout(
    template="plotly_white",
    hovermode= "x unified",
    title_x= 0.5
)
st.plotly_chart(fig,use_container_width=True)
st.divider()
st.subheader("Daily Returns")
fig2 = px.line(df, x="Date",y="Returns",title="Daily returns")
fig2.update_layout(
    template="plotly_white",
    hovermode="x unified",
    title_x=0.5
)
st.plotly_chart(
    fig2,
    use_container_width=True
)
st.divider()

st.subheader("Cumulative returns")
fig3= px.line(df, x="Date",y="Cumulative_Returns",
              title="cumulative returns")
# df.columns
st.plotly_chart(fig3, use_container_width=True)
st.divider()

#risk analysis 
st.header("📉 Risk Analysis")
st.subheader("⚠ Maximum Drawdown")
fig4 =  px.line(
    df,
    x="Date",
    y="drawdown",
    title="Drawdown"
)
fig4.update_layout(
    template="plotly_white",
    hovermode="x unified",
    title_x=0.5
)

st.plotly_chart(
    fig4,
    use_container_width=True
)
st.divider()


#momemtum analysis 


st.header("📊 Momentum Analysis")
st.subheader("📊 RSI")

fig5 = px.line(
    df,
    x="Date",
    y="RSI",
    title="Relative Strength Index (RSI)"
)

fig5.update_layout(
    template="plotly_white",
    hovermode="x unified",
    title_x=0.5
)

st.plotly_chart(
    fig5,
    use_container_width=True
)
st.divider()

st.caption(
    "Built by Vanshika Negi | StockVision V1"
)