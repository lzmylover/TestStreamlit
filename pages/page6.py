import streamlit as st

# print(st.session_state)
if "a" not in st.session_state:
    st.session_state.a = 0

a = 0
clicked = st.button("加1")
if clicked:
    # a += 1
    st.session_state.a += 1

st.write(st.session_state.a)
print(st.session_state)


