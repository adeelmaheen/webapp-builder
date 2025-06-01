import streamlit as st

def mockup_1():
    st.warning("Example mockup 1: Population app sample code")
    st.code("""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'States': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California'],
    'Population': [4900000, 730000, 7000000, 3000000, 39000000]
}
df = pd.DataFrame(data)
st.title("Population App")
st.table(df)
fig, ax = plt.subplots()
ax.bar(df['States'], df['Population'], color='pink')
st.pyplot(fig)
""")

def mockup_2():
    st.warning("Example mockup 2: Stock prices app sample code")
    st.code("""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
prices = [125, 138, 132, 142, 145, 139]

data = pd.DataFrame({"Month": months, "Price": prices})
st.title("Stock Market App")
st.line_chart(data.set_index('Month'))
st.table(data)
""")
