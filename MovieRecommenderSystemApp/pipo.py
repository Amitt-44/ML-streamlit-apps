import streamlit as st
import platform
import sys


import os

def get_linux_distribution():
    if os.path.exists('/etc/os-release'):
        with open('/etc/os-release') as f:
            return f.read()
    return "Not running on a Linux system"

st.write(get_linux_distribution())


# Display the Python version
st.write("Python version:", sys.version)
# Display OS information

# Display the Streamlit version
st.write("Streamlit version:", st.__version__)
os_info = platform.platform()
st.write("Operating System:", os_info)
