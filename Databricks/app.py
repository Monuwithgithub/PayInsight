import streamlit as st
import pandas as pd
pip install matplotlib
import matplotlib.pyplot as plt

st.set_page_config(page_title="Payment Dashboard", layout="wide")


# Load data
daily_revenue = pd.read_csv("data/daily_revenue.csv")
payment_method = pd.read_csv("data/payment_method_kpi.csv")
customer = pd.read_csv("data/customer_360.csv")
failures = pd.read_csv("data/payment_failures.csv")

# Title
st.title("💳 Payment Analytics Dashboard")
 

# Sidebar filter
st.sidebar.header("Filters")

selected_method = st.sidebar.selectbox(
    "Select Payment Method",
    ["All"] + list(payment_method["payment_method"].unique())
)
if selected_method != "All":
    payment_method_filtered = payment_method[
        payment_method["payment_method"] == selected_method
    ]
else:
    payment_method_filtered = payment_method

# ================= KPI =================
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", int(daily_revenue["total_revenue"].sum()))
col2.metric("Total Transactions", int(daily_revenue["transactions"].sum()))
col3.metric("Avg Transaction Value", round(daily_revenue["avg_ticket_size"].mean(), 2))

# ================= Revenue =================
st.subheader("📈 Daily Revenue Trend")

fig, ax = plt.subplots()
ax.plot(daily_revenue["date"], daily_revenue["total_revenue"])
plt.xticks(rotation=45)
st.pyplot(fig)

# ================= Payment Method =================
st.subheader("💳 Payment Method Distribution")

fig2, ax2 = plt.subplots()
ax2.pie(payment_method["transactions"], labels=payment_method["payment_method"], autopct='%1.1f%%')
st.pyplot(fig2)

# ================= Failure =================
st.subheader("⚠️ Payment Failure Analysis")
st.bar_chart(failures.set_index("payment_status"))

# ================= Customers =================
st.subheader("👤 Top Customers")

top_customers = customer.sort_values(by="lifetime_value", ascending=False).head(10)
st.dataframe(top_customers)

# ================= Insights =================
st.subheader("📌 Insights")

st.write("""
- UPI has highest usage
- Card payments show more failures
- Revenue varies across days
""")

method_filter = st.sidebar.selectbox(
    "Select Payment Method",
    payment_method["payment_method"]
)

# ================= DOWNLOAD FULL REPORT =================
st.subheader("📥 Download Full Report")

def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

# Merge datasets (example)
report_df = daily_revenue.merge(
    payment_method,
    how="left",
    left_index=True,
    right_index=True
)

csv_data = convert_df(report_df)

st.download_button(
    label="⬇️ Download Full Payment Report",
    data=csv_data,
    file_name='full_payment_report.csv',
    mime='text/csv',
)
st.download_button("Download Revenue Data", convert_df(daily_revenue), "revenue.csv")
st.download_button("Download Customer Data", convert_df(customer), "customers.csv")
st.download_button("Download Failure Data", convert_df(failures), "failures.csv")
