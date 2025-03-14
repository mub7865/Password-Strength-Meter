import streamlit as st
import re
import random
import string

# Function to check password strength
def password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    number_criteria = re.search(r'[0-9]', password)
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    score = sum([bool(length_criteria), bool(uppercase_criteria), bool(lowercase_criteria), bool(number_criteria), bool(special_char_criteria)])

    if score == 5:
        return "✅ Strong", "green", 100
    elif score >= 3:
        return "⚠️ Moderate", "orange", 60
    else:
        return "❌ Weak", "red", 30

# Function to generate a strong password
def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(12))

# Streamlit UI
st.set_page_config(page_title="Password Strength Checker", layout="centered")
st.title("🔐 Secure Password Strength Checker")

st.markdown("🔹 Enter a password and click 'Check Strength' to analyze its security.")

password = st.text_input("Enter your password:", type="password")
check_btn = st.button("🔍 Check Strength")

if check_btn:
    if password:
        strength, color, progress = password_strength(password)
        st.markdown(f"**Strength: `{strength}`**", unsafe_allow_html=True)
        st.progress(progress / 100)
        
        if strength == "❌ Weak":
            st.warning("⚠️ Your password is weak. Try using a mix of letters, numbers, and symbols.")
            st.write(f"🔹 **Suggested Strong Password:** `{generate_strong_password()}`")
    else:
        st.error("❌ Please enter a password to check!")

