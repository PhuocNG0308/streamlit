import streamlit as st
import pandas as pd
import time

def check_login(username, password):
    # Đọc dữ liệu từ file CSV
    csv_url = 'https://github.com/PhuocNG0308/streamlit/blob/main/UserData.csv'
    df = pd.read_csv(csv_url)

    # Kiểm tra username và password
    if username in df['username'].values and password in df['password'].values:
        return True
    else:
        return False


def main():
    # Biến trạng thái
    logged_in = False

    # Panel đăng nhập
    st.title("Đăng nhập")
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")
    login_button = st.button("Đăng nhập")

    if login_button:
        # Kiểm tra đăng nhập
        if check_login(username, password):
            # Đăng nhập thành công, đặt biến trạng thái là True
            logged_in = True

    # Kiểm tra trạng thái đăng nhập
    if logged_in:
        st.write("Bruh!!")

if __name__ == "__main__":
    main()