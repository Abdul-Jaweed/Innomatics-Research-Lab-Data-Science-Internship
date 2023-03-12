import streamlit as st


st.title(":blue[Innomatics] Data App :sunglasses:")
st.snow()

st.header("Data Science Insternship")

st.subheader("Feb 2023")

CODE = '''print("Hello, world")'''

st.code(CODE, language="python")



clk = st.button("Click Me")

if clk == True:
    st.subheader(":green[You clicked me] :+1:")
    st.balloons()