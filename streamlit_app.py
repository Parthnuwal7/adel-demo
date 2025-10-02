import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Adel Demo App",
    page_icon="🚀",
    layout="wide"
)

# Title and header
st.title("🚀 Welcome to Adel Demo App")
st.markdown("---")

# Introduction section
st.header("About This App")
st.write("""
This is a basic Streamlit application created for deployment demonstration.
Streamlit makes it easy to create interactive web applications with Python.
""")

# Interactive elements
st.header("Interactive Demo")

# Text input
name = st.text_input("Enter your name:", placeholder="Your name here")
if name:
    st.success(f"Hello, {name}! 👋")

# Slider
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")

# Select box
favorite_color = st.selectbox(
    "What's your favorite color?",
    ["Red", "Blue", "Green", "Yellow", "Purple"]
)
st.write(f"Your favorite color is {favorite_color}.")

# Checkbox
if st.checkbox("Show additional information"):
    st.info("""
    **Streamlit Features:**
    - Easy to use Python framework
    - Fast prototyping
    - Interactive widgets
    - Beautiful UI components
    - Built-in deployment options
    """)

# Button
if st.button("Click me!"):
    st.balloons()
    st.success("🎉 Congratulations! You clicked the button!")

# Sidebar
with st.sidebar:
    st.header("Sidebar")
    st.write("This is a sidebar where you can add navigation or additional controls.")
    st.markdown("---")
    st.info("Made with ❤️ using Streamlit")

# Footer
st.markdown("---")
st.markdown("### Thank you for using Adel Demo App!")
