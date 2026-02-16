import streamlit as st
import pkg_resources
import streamlit as st

installed_packages = [pkg.key for pkg in pkg_resources.working_set]
st.write("Installed packages:", installed_packages)

st.set_page_config(page_title = 'Country Analysis' , layout='wide')
st.title('Country Economic Analysis')
st.write("Multi-page professional Streamlit app.")
st.write("Use the sidebar to navigate between pages.")


