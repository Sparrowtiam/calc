import streamlit as st

st.set_page_config(page_title="SACCO Calculator", page_icon="🇰🇪")

st.title("🇰🇪 SACCO Financial Calculator")
st.markdown("Kenya SACCOs - Investment Returns Calculator")
st.divider()

# Sidebar
with st.sidebar:
    st.header("About")
    st.write("Calculate SACCO and MMF returns")

# Calculator functions
def sacco_calc(principal, monthly, rate):
    total = principal + (monthly * 12)
    interest = total * (rate / 100)
    return total, interest, total + interest

def mmf_calc(principal, days, rate):
    daily = rate / 365 / 100
    final = principal * ((1 + daily) ** days)
    return final - principal, final

# Tabs
tab1, tab2 = st.tabs(["SACCO", "MMF"])

# TAB 1: SACCO
with tab1:
    st.header("SACCO Interest Calculator")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        principal = st.number_input("Principal (KES)", 0.0, value=50000.0, step=1000.0)
    with col2:
        monthly = st.number_input("Monthly (KES)", 0.0, value=5000.0, step=500.0)
    with col3:
        rate = st.number_input("Rate (%)", 0.0, 100.0, value=8.0, step=0.5)
    
    if st.button("Calculate", key="sacco"):
        total, interest, final = sacco_calc(principal, monthly, rate)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Principal", f"KES {principal:,.0f}")
        with col2:
            st.metric("Total", f"KES {total:,.0f}")
        with col3:
            st.metric("Interest", f"KES {interest:,.2f}")
        with col4:
            st.metric("Final", f"KES {final:,.2f}")

# TAB 2: MMF
with tab2:
    st.header("MMF Calculator")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        principal = st.number_input("Investment (KES)", 0.0, value=100000.0, step=5000.0)
    with col2:
        days = st.number_input("Days", 1, value=90)
    with col3:
        rate = st.number_input("Rate (%)", 0.0, 50.0, value=6.0, step=0.1)
    
    if st.button("Calculate", key="mmf"):
        interest, final = mmf_calc(principal, days, rate)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Investment", f"KES {principal:,.0f}")
        with col2:
            st.metric("Days", f"{days}")
        with col3:
            st.metric("Interest", f"KES {interest:,.2f}")
        with col4:
            st.metric("Final", f"KES {final:,.2f}")

st.divider()
st.write("*For educational purposes only*")
