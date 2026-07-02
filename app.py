##importing required libraries 

import streamlit as st
import pandas as pd 
import plotly.express as px
from datetime import datetime
from PIL import Image


#css
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#setting up page configuratoin 
st.set_page_config(
    page_title="StockVision",
    page_icon="📈",
    layout="wide"
)
load_css()
# st.title("📈Stock Vision")
# st.write("Welcome to Stock Vision V1")
# st.caption(
#     "A Financial Analytics Dashboard for Stock Performance and Risk Analysis."
# )


 # side bar :


df = pd.read_csv("data/processed/enginersin_features.csv")
logo = Image.open("assets/logo.png")
with st.sidebar:

    # st.image(logo, width=60)
    st.image(logo, use_container_width=True)

    st.divider()
st.sidebar.markdown(
    """
    <p style="
    color:#00C853;
    font-size:13px;
    font-weight:700;
    letter-spacing:1px;
    ">
    COMPANY INSIGHTS
    </p>
    """,
    unsafe_allow_html=True
)    
# st.sidebar.write("**Ticker:** ENGINERSIN.NS")
st.sidebar.caption("Choose a company")
selected_stock = st.sidebar.selectbox(
    "Select Stock",
   [
    "ENGINERSIN.NS",
    "POLYCAB.NS",
    "PARAS.NS"
]
)

#sidebar 
with st.sidebar.container(border=True):
     st.markdown("###  Dataset Summary")

     st.markdown(f"**Selected:** {selected_stock}")

     st.markdown(f"**Trading Days:** {len(df)}")

     st.markdown(f"**From:** {df['Date'].iloc[0]}")

     st.markdown(f"**To:** {df['Date'].iloc[-1]}")

     st.markdown(f""" Latest Close :
    <span style="color:#00C853;font-weight:bold;">
     ₹{df['Close'].iloc[-1]:.2f}
    </span>
    """,
    unsafe_allow_html=True)
    
     st.markdown(f"""  Data Source :   <span style="color:#A855F7;font-weight:bold;">
                 Yahoo Finance
    </span>
    """,
    unsafe_allow_html=True)
# st.subheader("feature engineered dataset")





with st.expander("view feature engineered dataset"):
    st.dataframe(df)
st.header("Dashboard overview")
st.caption(
    "A Financial Analytics Dashboard for Stock Performance and Risk Analysis."
)
left, right = st.columns([5, 2])


with right:

    current_time = datetime.now().strftime("%d %b %Y, %I:%M %p")

    st.success("🟢 Data Loaded")

    st.caption(f"Last Updated: {current_time}")    
#------------------------------------
#kpi section :
#------------------------------------
st.subheader(" Key Metrics")
st.header(f"selected stock:{selected_stock}")
col1, col2, col3 , col4,col5 = st.columns(5)
latest = df.iloc[-1]
previous = df.iloc[-2]

price_change = latest["Close"] - previous["Close"]
price_change_pct = (price_change / previous["Close"]) * 100
current_price = df["Close"].iloc[-1]



with col1:
    col1.metric(
     "Current Price",
        f"₹{latest['Close']:.2f}",
        f"{price_change_pct:.2f}%"


)
with col5:
    st.metric(
        "Volume",
        f"{latest['Volume']:,}"
    )

current_rsi = df["RSI"].iloc[-1]
with col2:
      st.metric(
        "RSI",
        f"{latest['RSI']:.2f}"
    )



max_drawdown = df["drawdown"].min()
with col3:
     st.metric(
        "Max Drawdown",
        f"{max_drawdown: .2%}"

    )
       

# current_volatility  = df["rolling_volatility"].iloc[-1]
with col4:
    st.metric(
        "Volatility",
        f"{latest['rolling_volatility']:.2%}"
    )
st.header("Price & Moving Averages")
st.subheader("Closing Price")
fig = px.line(df,x ="Date",y= ["Close","MA_20","MA_50"],
               title=" Price with Moving Averages",
    labels={
        "value": "Price (₹)",
        "variable": "Indicator"
    } )
# price

# st.plotly_chart(fig,use_container_width=True)
fig.update_traces(
    line=dict(
        
        width=3
    )
)
fig.data[0].line.color = "#00C853"   # Close (Green)
fig.data[1].line.color =  "#3B82F6"  # MA20 (Blue)
fig.data[2].line.color = "#EF4444"   # MA50 (Red)

fig.data[0].line.width = 3
fig.data[1].line.width = 2
fig.data[2].line.width = 2
fig.update_layout(

    template="plotly_dark",

    paper_bgcolor="#1A1F2E",

    plot_bgcolor="#1A1F2E",

    font=dict(
        color="white",
        size=14
    ),

    title_font=dict(
        size=22,
        color="white"
    ),

    margin=dict(
        l=30,
        r=30,
        t=60,
        b=30
    ),

    hovermode="x unified",

    legend=dict(
        orientation="h",
        y=1.05,
        x=0
    )
)
fig.update_xaxes(

    showgrid=True,

    gridcolor="#2A2F3A",

    zeroline=False

)

fig.update_yaxes(

    showgrid=True,

    gridcolor="#2A2F3A",

    zeroline=False

)
st.plotly_chart(fig,use_container_width=True)
st.divider()

#daily returns 

st.subheader("Daily Returns")
fig2 = px.line(df, x="Date",y="Returns",title="Daily returns")
fig2.update_traces(
    line=dict(
        color="#00C853",
        width=3
    )
)
fig2.update_layout(

    template="plotly_dark",

    paper_bgcolor="#1A1F2E",

    plot_bgcolor="#1A1F2E",

    font=dict(
        color="white",
        size=14
    ),

    title_font=dict(
        size=22,
        color="white"
    ),

    margin=dict(
        l=30,
        r=30,
        t=60,
        b=30
    ),

    hovermode="x unified",

    legend=dict(
        orientation="h",
        y=1.05,
        x=0
    )
)
fig2.update_xaxes(

    showgrid=True,

    gridcolor="#2A2F3A",

    zeroline=False

)

fig2.update_yaxes(

    showgrid=True,

    gridcolor="#2A2F3A",

    zeroline=False

)
st.plotly_chart(
    fig2,
    use_container_width=True
)
st.divider()

st.subheader("Cumulative returns")
fig3= px.line(df, x="Date",y="Cumulative_Returns",
              title="cumulative returns")
fig3.update_traces(
    line=dict(
        color="#00C853",
        width=3
    )
)


fig3.update_layout(

    template="plotly_dark",

    paper_bgcolor="#1A1F2E",

    plot_bgcolor="#1A1F2E",

    font=dict(
        color="white",
        size=14
    ),

    title_font=dict(
        size=22,
        color="white"
    ),

    margin=dict(
        l=30,
        r=30,
        t=60,
        b=30
    ),

    hovermode="x unified",

    legend=dict(
        orientation="h",
        y=1.05,
        x=0
    )
)
fig3.update_xaxes(

    showgrid=True,

    gridcolor="#2A2F3A",

    zeroline=False

)

fig3.update_yaxes(

    showgrid=True,

    gridcolor="#2A2F3A",

    zeroline=False

)
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
fig4.update_traces(
    line=dict(
        color="#00C853",
        width=3
    )
)
fig4.update_layout(

    template="plotly_dark",

    paper_bgcolor="#1A1F2E",

    plot_bgcolor="#1A1F2E",

    font=dict(
        color="white",
        size=14
    ),

    title_font=dict(
        size=22,
        color="white"
    ),

    margin=dict(
        l=30,
        r=30,
        t=60,
        b=30
    ),

    hovermode="x unified",

    legend=dict(
        orientation="h",
        y=1.05,
        x=0
    )
)
fig4.update_xaxes(

    showgrid=True,

    gridcolor="#2A2F3A",

    zeroline=False

)

fig4.update_yaxes(

    showgrid=True,

    gridcolor="#2A2F3A",

    zeroline=False

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
fig5.update_traces(line=dict(
    color="#00C853",
    width=3))

fig5.update_layout(

    template="plotly_dark",

    paper_bgcolor="#1A1F2E",

    plot_bgcolor="#1A1F2E",

    font=dict(
        color="white",
        size=14
    ),

    title_font=dict(
        size=22,
        color="white"
    ),

    margin=dict(
        l=30,
        r=30,
        t=60,
        b=30
    ),

    hovermode="x unified",

    legend=dict(
        orientation="h",
        y=1.05,
        x=0
    )
)
fig5.update_xaxes(

    showgrid=True,

    gridcolor="#2A2F3A",

    zeroline=False

)

fig5.update_yaxes(

    showgrid=True,

    gridcolor="#2A2F3A",

    zeroline=False

)
st.plotly_chart(
    fig5,
    use_container_width=True
)
st.divider()

st.caption(
    "Built by Vanshika Negi | StockVision V1"
)