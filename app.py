##importing required libraries 

import streamlit as st
import pandas as pd 
import plotly.express as px
from datetime import datetime
from PIL import Image

from src.pipeline import load_stock_data
from src.indicators import add_features
from src.data_cleaning import clean_data
from src.validation import validate_data
from src.eda import generate_eda
from src.company_info import get_company_info
import src.company_info
# st.write(src.company_info.__file__)
from src.insights import generate_insights
from src.chart_style import style_chart

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


# df = pd.read_csv("data/processed/enginersin_features.csv")
logo = Image.open("assets/logo.png")
with st.sidebar:

    # st.image(logo, width=60)
    st.image(logo, use_container_width=True)

    st.divider()

# st.sidebar.write("**Ticker:** ENGINERSIN.NS")
st.sidebar.caption("Choose a company")
# selected_stock = st.sidebar.selectbox(
#     "Select Stock",
#    [
#     "ENGINERSIN.NS",
#     "POLYCAB.NS",
#     "PARAS.NS"
# ]
# )
selected_stock = st.sidebar.text_input(
    "Enter Stock Ticker",
    value="ENGINERSIN.NS"
)

selected_stock = selected_stock.upper().strip()
try:
    df = load_stock_data(selected_stock)
    company = get_company_info(selected_stock)
    # st.write(company)
    df = validate_data(df)
    df = clean_data(df)
    df = add_features(df)
    eda_summary = generate_eda(df)
    insights = generate_insights(df)
    # st.write(insights)

except Exception as e:
    st.error(e)
    st.stop()



# st.write(df.head()) ->used for checking the data loading in the live streamlit app(for tsting purpose only )


# Sidebar
with st.sidebar.container(border=True):

    st.markdown("###  Dataset Summary")

    st.markdown(f"**Company:** {company['Name']}")

    st.markdown(f"**Ticker:** {selected_stock}")

    st.markdown(f"**Sector:** {company['Sector']}")

    st.markdown(f"**Industry:** {company['Industry']}")

    st.markdown(f"**Exchange:** {company['Exchange']}")

    st.markdown(f"**Currency:** {company['Currency']}")
    st.markdown(f"**Market Cap:** {company['Market Cap']}")

    st.markdown(f"**52 Week High:** {company['52 Week High']}")

    st.markdown(f"**52 Week Low:** {company['52 Week Low']}")

    st.markdown(f"**Dividend Yield:** {company['Dividend Yield']}")
    st.markdown("---")

    st.markdown(f"**Trading Days:** {eda_summary['Trading Days']}")

    st.markdown(f"**From:** {eda_summary['Start Date']}")

    st.markdown(f"**To:** {eda_summary['End Date']}")

    st.markdown(
        f"""
        **Latest Close:**
        <span style="color:#00C853;font-weight:bold;">
        {company['Currency']} {df['Close'].iloc[-1]:.2f}
        </span>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        **Data Source:**
        <span style="color:#A855F7;font-weight:bold;">
        Yahoo Finance
        </span>
        """,
        unsafe_allow_html=True
    )
# st.subheader("feature engineered dataset")

# st.write(eda_summary)
# ------------------------------------
# Sidebar Navigation
# ------------------------------------

st.sidebar.markdown("## 📊 Navigation")

st.sidebar.markdown("""
- [🏠 Dashboard](#dashboard)
- [📈 Price Analysis](#price-analysis)
- [📊 Returns Analysis](#returns-analysis)
- [⚠️ Risk Analysis](#risk-analysis)
- [📉 Momentum (RSI)](#momentum-rsi)
- [🔖 Market Insights](#Market-Insights)
- [💹 Cumulative returns](#Cumulative-returns)


""")
st.markdown('<div id="dashboard"></div>', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Project")

st.sidebar.link_button(
    "🐙 GitHub Repository",
    "https://github.com/Van004-ds/StockVision"
) 


with st.expander("view feature engineered dataset"):
    st.dataframe(df)

st.markdown('<div id="dashboard"></div>', unsafe_allow_html=True)


left, right = st.columns([5, 2])
with left:
    st.title(" Dashboard Overview")
    st.caption("Real-time stock market insights and analysis")

with right:

    current_time = datetime.now().strftime("%d %b %Y, %I:%M %p")

    st.success("🟢 Data Loaded")

    st.caption(f"Last Updated: {current_time}")   

     
#------------------------------------
# KPI Section
#------------------------------------

with st.container(border=True):

    

    col1, col2, col3, col4, col5 = st.columns(5)

    latest = df.iloc[-1]
    previous = df.iloc[-2]

    price_change = latest["Close"] - previous["Close"]
    price_change_pct = (price_change / previous["Close"]) * 100

    with col1:
     st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Current Price</div>
        <div class="kpi-value">{company['Currency']} {latest['Close']:.2f}</div>
        <div class="kpi-change">▲ {price_change_pct:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)
    with col2:
        with st.container(border=True):

            st.metric(
            "RSI",
            f"{latest['RSI']:.2f}"
        )

    max_drawdown = df["drawdown"].min()

    with col3:
        with st.container(border=True):


           st.metric(
            "Max Drawdown",
            f"{max_drawdown:.2%}"
        )

    with col4:
        with st.container(border=True):

          st.metric(
            "Volatility",
            f"{latest['rolling_volatility']:.2%}"
        )

    with col5:
        with st.container(border=True):

            st.metric(
            "Volume",
            f"{latest['Volume']:,}"
        )
st.markdown('<div id="Market-Insights"></div>', unsafe_allow_html=True)

            
#--------------------------------
#insights card ;
#----------------------------------


st.subheader(" Market Insights")

col1, col2 = st.columns(2)

with col1:
    st.metric("Trend", insights["Trend"])
    st.metric("RSI", insights["RSI"])

with col2:
    st.metric("Risk", insights["Risk"])
    st.metric("Drawdown", insights["Drawdown"])

st.markdown('<div id="price-analysis"></div>', unsafe_allow_html=True)

st.subheader("📈 Closing Price")

#price and mocing averages

with st.container(border=True):
    st.subheader("Closing Price")
    fig = px.line(
    df,
    x="Date",
    y=["Close","MA_20","MA_50"],
    color_discrete_map={
        "Close":"#29B60E",
        "MA_20":"#60A5FA",
        "MA_50":"#EF4444"
    }
)
    fig = style_chart(fig)
    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )






# price




st.divider()


st.markdown('<div id="returns-analysis"></div>', unsafe_allow_html=True)

#daily returns 

st.subheader("Daily Returns")
fig2 = px.line(df, x="Date",y="Returns",title="Daily returns",
 color_discrete_sequence=["#22C55E"])


fig2 = style_chart(fig2)

st.plotly_chart(
    fig2,
    use_container_width=True
)
st.divider()

st.markdown('<div id="Cumulative-returns"></div>', unsafe_allow_html=True)




st.subheader("Cumulative returns")

fig3= px.line(df, x="Date",y="Cumulative_Returns",
              title="cumulative returns",
              color_discrete_sequence=["#22C55E"],
              line_shape="spline")

fig3= style_chart(fig3)

st.plotly_chart(
    fig3,
    use_container_width=True
)
st.divider()
st.markdown('<div id="risk-analysis"></div>', unsafe_allow_html=True)

#risk analysis 
st.header(" Risk Analysis")
st.subheader("⚠ Maximum Drawdown")
fig4 =  px.line(
    df,
    x="Date",
    y="drawdown",
    title="Drawdown",
    color_discrete_sequence=["#088F8F"]
)

fig4 = style_chart(fig4)

st.plotly_chart(
    fig4,
    use_container_width=True
)
st.divider()

st.markdown('<div id="momentum-rsi"></div>', unsafe_allow_html=True)

#momemtum analysis 


st.header(" Momentum Analysis")
st.subheader(" RSI")

fig5 = px.line(
    df,
    x="Date",
    y="RSI",
    title="Relative Strength Index (RSI)",
    color_discrete_sequence=["#22C55E"]
    
)

fig5 = style_chart(fig5)

st.plotly_chart(
    fig5,
    use_container_width=True
)
st.divider()

st.caption(
    "Built by Vanshika Negi | StockVision V1"
)