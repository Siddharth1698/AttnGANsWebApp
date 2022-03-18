import streamlit as st
from multiapp import MultiApp
import demo

app = MultiApp()
st.set_page_config(page_title="RobrtaAttnGAN", initial_sidebar_state="auto")

st.sidebar.title("Gans Project")
# Add all application here

app.add_app("Birds Image Generation", demo.demo_gan)



# The main app
app.run()
