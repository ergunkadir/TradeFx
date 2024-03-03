import streamlit as st;
from streamlit_option_menu import option_menu
from datetime import datetime
import yfinance as yf

st.set_page_config(
    page_title="TRADEFX | Genel Bakış",
    page_icon="💹",
)
if 'symbol' not in st.session_state:
    st.session_state['symbol']=''
hide_sty="""
<style>
footer{Visibility: hidden;}
</style>
"""
st.markdown(hide_sty,unsafe_allow_html=True)
st.title('TRADEFX ||')
st.write('dogru yatırım dogru analiz')

symbol =st.text_input(st.session_state["symbol"],st.session_state["symbol"],disabled=False)
if symbol not in "":
    st.session_state["symbol"]=symbol
    baslik=st.header(symbol+ " hisse verileri yüklendi")
    
else:
    baslik= st.header("BIST Hisseleri arayın")

price = yf.Ticker(symbol+'.IS')

col, col1= st.columns(2)

with col:
   st.write("Bölünmeler %")
   st.write(price.splits)

with col1:
   st.write("Temettüler lot başı %")
   st.write(price.dividends)

colz, colt= st.columns(2)

with colz:
   st.write("kazanç tarihleri")
   st.line_chart(price.get_earnings_dates())
   

with colt:
   st.write("sermaye")
   st.line_chart(price.get_shares_full())
veri =price.info
financials = price.financials
st.write("Şirket adı : ",veri.get('longName'))
st.write("Sektör : ",veri.get('industry'))
st.write("Varlıklar : ",veri.get('totalAssets'))
st.write("Son 4 çeyreklik büyüme ",veri.get('earningsQuarterlyGrowth'))
st.write("Piyasa degeri ","{:,}".format(veri.get('marketCap')))
st.write("FK ORANI ",veri.get('forwardPE'))
st.write("Toplam Lot sayısı : ","{:,}".format(veri.get('sharesOutstanding')))
st.write("Dolaşımdaki lot oranı  :","{:,}".format(veri.get('floatShares')))