import streamlit as st
import platform
import sys


# Get Linux distribution information
distribution = platform.linux_distribution()
st.write(f"Linux Distribution: {distribution}")

# Display the Python version
st.write("Python version:", sys.version)
# Display OS information

# Display the Streamlit version
st.write("Streamlit version:", st.__version__)
os_info = platform.platform()
st.write("Operating System:", os_info)
