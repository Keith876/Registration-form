#Registration Form
import streamlit as st

st.title("Registration Form")

first, last = st.columns(2)

first.text_input("First name")
last.text_input("Last name")

email, mobile = st.columns([3, 1])
email.text_input("Email address")
mobile.text_input("Mobile number")

user, pw, pw2 = st.columns(3)
user.text_input("Username")
pw.text_input("Password", type="password")
pw2.text_input("Retype your password", type="password")

ch, sub = st.columns(2)
ch.checkbox("I Agree")
sub.button("Submit")

