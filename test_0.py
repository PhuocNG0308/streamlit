import streamlit as st
import time

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
        if username == "admin" and password == "password":
            # Đăng nhập thành công, đặt biến trạng thái là True
            logged_in = True

    # Kiểm tra trạng thái đăng nhập
    if logged_in:
        # Hiển thị menu thao tác
        show_menu()

def show_menu():
    st.title("Menu thao tác")
    st.write("Chọn một tác vụ từ menu bên dưới.")

    # Hiển thị các tác vụ trong menu
    menu_options = ["Tác vụ 1", "Tác vụ 2", "Tác vụ 3"]
    selected_option = st.selectbox("Chọn tác vụ", menu_options)

    if selected_option == "Tác vụ 1":
        # Xử lý tác vụ 1
        st.write("Đang xử lý tác vụ 1...")
    elif selected_option == "Tác vụ 2":
        # Xử lý tác vụ 2
        st.write("Đang xử lý tác vụ 2...")
    elif selected_option == "Tác vụ 3":
        # Xử lý tác vụ 3
        st.write("Đang xử lý tác vụ 3...")

if __name__ == "__main__":
    while True:
        main()
        # Làm mới giao diện sau mỗi lần lặp
        time.sleep(1)
        st.experimental_rerun()