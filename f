"""conn = connect_database('DATA/intelligence_platform.db')
incidents = get_all_incidents_pandas(conn)
st.dataframe(incidents, use_container_width=True)


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.error("You must be logged in to view this page.")
    if st.button("Go to login"):
        st.switch_page("Home.py")
st.stop()

st.title(":bar_chart: Dashoard")
st.sucess(f"Welcome, {st.session_state.username}!")

st.divider()
if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.info("You have been logged out")
    st.switch_page("Home.py")"""