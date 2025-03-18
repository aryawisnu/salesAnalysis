import streamlit as st

st.set_page_config(page_title="Sales Analysis Tools", page_icon="📊")
st.sidebar.header("📊 Sales Analysis Tools", divider=True)
st.sidebar.markdown(
"""
Sales Analysis Tools is an intuitive web platform designed to help businesses effortlessly upload, process, and visualize their sales, marketing, and product data. With a clean interface and powerful analysis features, this tool enables users to transform raw data into actionable insights, supporting data-driven decision-making and business growth.
"""
)
st.sidebar.subheader("Key Features:", divider=True)
st.sidebar.markdown(
"""
1. File Upload & Auto Processing
2. Data Tabulation
3. Interactive Sales & Marketing Dashboards
4. Multi-Category Analysis
"""
)

st.write("# About 🧐")

_left, mid, _right = st.columns(3)
with mid:
    st.image("https://media.tenor.com/IF2JdxzmyN4AAAAj/coding-girl.gif")

st.markdown(
"""
This website was created by Vira Angelina, a Business Statistics student at Institut Teknologi Sepuluh Nopember (ITS), class of 2022.

The Sales Analysis Tools platform is part of her academic project and personal portfolio, designed to showcase practical applications of data analysis in the business world. Built with a focus on simplicity and functionality, this tool helps users easily upload, process, and analyze sales, marketing, and product data.

Through this project, Vira aims to demonstrate her passion for data analytics, business intelligence, and the development of digital solutions that turn raw data into valuable business insights.    
"""
)

st.subheader("How to reach me?", divider=True)
_left, mid, _right = st.columns(3)
_left.markdown("[![Title]('https://img.icons8.com/material-outlined/48/000000/github.png')]('https://github.com/aryawisnu')")
mid.markdown("[![Title]('https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg')]('https://www.linkedin.com/in/vira-angelina/')")