import streamlit as st
from ring.db.user import Role, User, Users
from ring.auth import hash_email


st.header("👤 Nutzerverwaltung")

users = Users()

all_users = users.all()

col1, col2 = st.columns(2)

with col1:
    st.header("Alle Nutzer")
    for u in all_users:
        st.write(u)
with col2:
    st.header("Neuer Nutzer")
    new_username = st.text_input("Benutzername")
    new_user_email = st.text_input("Email")
    new_user_role = st.selectbox(
        "Rolle", [Role.USER, Role.OWNER, Role.ADMIN, Role.VISITOR]
    )
    user = User(
        username=new_username, role=new_user_role, id=hash_email(new_user_email)
    )
    st.write(user)
    st.button("Speichern", on_click=lambda: users.upsert(user))
