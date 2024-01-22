import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore, auth

# Khởi tạo Firebase
cred = credentials.Certificate("/workspaces/pr3/zalo-chat-5d081-firebase-adminsdk-x46ia-54e6ad4883.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Trang đăng nhập
def login_page():
    st.title("Login Page")

    # Thêm các phần tử đăng nhập như input cho email và password
    email = st.text_input("Email:")
    password = st.text_input("Password:", type="password")

    if st.button("Login"):
        # Thực hiện kiểm tra đăng nhập ở đây
        # Nếu đăng nhập thành công, chuyển sang trang chủ
        if authenticate_user(email, password):
            st.success("Login successful!")
            home_page()

        else:
            st.error("Invalid credentials. Please try again.")

    # Button để chuyển sang trang đăng ký
    if st.button("Register"):
        register_page()

# Trang đăng ký
def register_page():
    st.title("Register Page")

    # Thêm các phần tử đăng ký như input cho email và password
    email = st.text_input("Email:")
    password = st.text_input("Password:", type="password")

    if st.button("Register"):
        # Thực hiện đăng ký ở đây và lưu thông tin vào Firebase
        create_user(email, password)
        st.success("Registration successful! Please login.")
        login_page()

# Trang chủ
def home_page():
    st.title("Welcome to Facebook")
    st.write("Welcome to Facebook!")

def authenticate_user(email, password):
    try:
        # Thực hiện kiểm tra đăng nhập bằng Firebase
        user = auth.get_user_by_email(email)
        # Xác thực mật khẩu
        auth.get_user_by_email(email, password)
        return True
    except auth.AuthError:
        return False

def create_user(email, password):
    try:
        # Thực hiện đăng ký và lưu thông tin vào Firebase
        user = auth.create_user(
            email=email,
            password=password
        )
        print(f"User created: {user.uid}")
    except auth.AuthError as e:
        print(f"Error creating user: {e}")

# Chạy ứng dụng
login_page()