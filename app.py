import streamlit as st
import pandas as pd
from db_config import get_connection
import auth, queries

st.set_page_config(layout="wide")

st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #f4f6f9;
}

/* Headings */
h1, h2, h3, h4 {
    color: black !important;
    font-weight: bold;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: white;
}
section[data-testid="stSidebar"] * {
    color: black !important;
}

/* Buttons */
.stButton>button {
    background-color: #1976d2;
    color: white;
    border-radius: 8px;
}

/*  INPUT BOX FIX */
.stTextInput input, .stNumberInput input {
    background-color: #2c2f3a !important;
    color: white !important;
    border-radius: 8px;
    padding: 8px;
}

/* Labels */
label {
    color: black !important;
    font-weight: bold;
}

/* Tables */
thead tr th {
    color: black !important;
}
tbody tr td {
    color: black !important;
}

</style>
""", unsafe_allow_html=True)

if "conn" not in st.session_state:
    st.session_state.conn = get_connection()
    st.session_state.cursor = st.session_state.conn.cursor(dictionary=True)

conn = st.session_state.conn
cursor = st.session_state.cursor

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title(" Hospital Login")

    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Login"):
        success, status = auth.login_or_register(cursor, conn, u, p)

        if success:
            st.session_state.login = True

            if status == "registered":
                st.success("New user created & logged in ")
            else:
                st.success("Login Successful ")

            st.rerun()
        else:
            st.error("Wrong Password ")

    st.stop()

st.sidebar.markdown("###  Account")
if st.sidebar.button("Logout"):
    st.session_state.login = False
    st.rerun()

# ---------------- MENU ----------------
st.title(" Hospital Management Dashboard")

menu = st.sidebar.radio("Menu", [
    "Dashboard","Patients","Doctors",
    "Appointments","Treatments","Analytics"
])

if menu == "Dashboard":
    col1, col2 = st.columns(2)

    revenue = pd.DataFrame(queries.get_revenue(cursor))
    doctors = pd.DataFrame(queries.most_consulted_doctors(cursor))

    with col1:
        st.subheader(" Revenue")
        if not revenue.empty:
            st.line_chart(revenue.set_index("month"))

    with col2:
        st.subheader(" Doctor Visits")
        if not doctors.empty:
            st.bar_chart(doctors.set_index("name"))

elif menu == "Patients":
    cursor.execute("SELECT * FROM patients")
    df = pd.DataFrame(cursor.fetchall())
    df.insert(0, "S.No", range(1, len(df)+1))
    st.dataframe(df, use_container_width=True)

elif menu == "Doctors":
    cursor.execute("SELECT * FROM doctors")
    df = pd.DataFrame(cursor.fetchall())
    df.insert(0, "S.No", range(1, len(df)+1))
    st.dataframe(df, use_container_width=True)

elif menu == "Appointments":
    cursor.execute("""
        SELECT a.appointment_id, p.name, d.name AS doctor, a.date
        FROM appointments a
        JOIN patients p ON a.patient_id=p.patient_id
        JOIN doctors d ON a.doctor_id=d.doctor_id
    """)
    df = pd.DataFrame(cursor.fetchall())
    df.insert(0, "S.No", range(1, len(df)+1))
    st.dataframe(df, use_container_width=True)

elif menu == "Treatments":
    cursor.execute("""
        SELECT t.treatment_id, p.name, d.name AS doctor,
               t.diagnosis, t.cost, t.treatment_date
        FROM treatments t
        JOIN patients p ON t.patient_id=p.patient_id
        JOIN doctors d ON t.doctor_id=d.doctor_id
    """)
    df = pd.DataFrame(cursor.fetchall())
    df.insert(0, "S.No", range(1, len(df)+1))
    st.dataframe(df, use_container_width=True)

elif menu == "Analytics":
    diseases = pd.DataFrame(queries.common_diseases(cursor))
    visits = pd.DataFrame(queries.patient_visits(cursor))

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Most Common Diseases")
        if not diseases.empty:
            st.bar_chart(diseases.set_index("diagnosis"))

    with col2:
        st.subheader("Patient Visits")
        if not visits.empty:
            st.bar_chart(visits.set_index("name"))