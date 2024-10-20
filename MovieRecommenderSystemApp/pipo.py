import streamlit as st
import platform

# Display OS information
os_info = platform.platform()
st.write("Operating System:", os_info)
