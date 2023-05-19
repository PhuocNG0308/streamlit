import streamlit as st

def main():
    st.title("Đăng nhập")

    username = st.text_input("Tên người dùng")
    password = st.text_input("Mật khẩu", type="password")

    if st.button("Đăng nhập"):
        if username == "admin" and password == "password":
            st.success("Đăng nhập thành công")
            # Thực hiện các hành động sau khi đăng nhập thành công
        else:
            st.error("Tên người dùng hoặc mật khẩu không chính xác")

if __name__ == "__main__":
    main()