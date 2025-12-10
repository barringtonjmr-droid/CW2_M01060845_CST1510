import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.data.db import connect_database
import streamlit as st
from app.data.datasets import get_all_datasets_pandas, insert_data, update_datasets, delete_datasets
import pandas as pd

conn = connect_database()
st.title("Data Science Management")

# Protect Page
if "logged_in" not in st.session_state:
    st.error("You must log in first. Please go to the Login page from the sidebar.")
    st.stop() 

query = get_all_datasets_pandas()
df = pd.DataFrame(query)
st.subheader("All Datasets")
st.write(query)

with st.expander("Add New Dataset"):
    dataset_id = st.text_input("Dataset ID")
    name = st.text_input("Name")
    rows = st.number_input("Number of Rows")
    columns = st.number_input("Number of Columns", min_value=1)
    uploaded_by = st.text_input("Uploaded By")
    uploaded_at = st.text_input("Created At (YYYY-MM-DD)")

    if st.button("Add Dataset"):
        # Validate fields
        if not all([dataset_id, name, rows, columns, uploaded_by, uploaded_at]):
            st.warning("All fields are required.")
        else:
            new_id = insert_data(
                dataset_id,
                name,
                rows,
                columns,
                uploaded_by,
                uploaded_at
            )
            st.success(f"Dataset successfully added! New ID: {new_id}")

with st.expander("Update Dataset"):
    available = df["dataset_id"].tolist()

    old_id = st.selectbox("Select dataset to update", available)
    new_id = st.text_input("New Dataset ID")

    if st.button("Update Dataset"):
        if not new_id:
            st.warning("Enter new dataset ID.")
        else:
            updated = update_datasets(old_id, new_id)
            if updated:
                st.success(f"Updated '{old_id}' → '{new_id}'")
            else:
                st.error("No dataset updated. Check dataset ID.")

with st.expander("Delete Dataset"):
    dataset_to_delete = st.selectbox("Select dataset", df["dataset_id"].tolist())

    if st.button("Delete Dataset"):
        deleted = delete_datasets(dataset_to_delete)
        if deleted:
            st.success(f"Dataset '{dataset_to_delete}' deleted! Refresh page.")
        else:
            st.error("No dataset deleted. Check dataset ID.")

st.header("📊 Data Science Analytics Dashboard")

if df.empty:
    st.info("No data available for analytics.")
else:
    st.subheader("📌 Overview Metrics")

    col1, col2, col3, col4 = st.columns(4)

    total_datasets = len(df)
    total_rows = df["rows"].sum()
    total_columns = df["columns"].sum()
    unique_uploaders = df["uploaded_by"].nunique()

    with col1:
        st.metric("Total Datasets", total_datasets)

    with col2:
        st.metric("Total Rows", total_rows)

    with col3:
        st.metric("Total Columns", total_columns)

    with col4:
        st.metric("Unique Uploaders", unique_uploaders)

    st.markdown("---")

    # clean date
    df["upload_date"] = pd.to_datetime(df["upload_date"], errors="coerce")
    
    # 2️⃣ Top Uploaders (bar chart)
    st.subheader("🏆 Top Uploaders")

    top_uploaders = df["uploaded_by"].value_counts()

    st.bar_chart(top_uploaders)

    st.markdown("---")

    # 3️⃣ Rows & Columns Trend (area chart)
    st.subheader("📊 Rows / Columns Trend Over Time")

    trend_df = df.sort_values("upload_date")[["upload_date", "rows", "columns"]]
    trend_df = trend_df.set_index("upload_date")

    st.area_chart(trend_df)

    st.markdown("---")

    # 4️⃣ Rows Per Uploader (bar chart)
    st.subheader("📦 Total Rows Per Uploader")

    rows_per_uploader = df.groupby("uploaded_by")["rows"].sum()

    st.bar_chart(rows_per_uploader)

    st.markdown("---")

    # 5️⃣ Columns Per Uploader (bar chart)
    st.subheader("📐 Total Columns Per Uploader")

    columns_per_uploader = df.groupby("uploaded_by")["columns"].sum()

    st.bar_chart(columns_per_uploader)

