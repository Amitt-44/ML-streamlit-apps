import streamlit as st
import platform

# Display OS information

# Display the Streamlit version
st.write("Streamlit version:", st.__version__)
os_info = platform.platform()
st.write("Operating System:", os_info)
