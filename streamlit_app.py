"""
Streamlit Web App - SACCO Financial Calculator
=============================================
Interactive web interface for SACCO and MMF calculations using Streamlit
"""

import streamlit as st

# ============================================================================
# PAGE CONFIGURATION (MUST BE FIRST!)
# ============================================================================

st.set_page_config(
    page_title="SACCO Calculator",
    page_icon="🇰🇪",
    layout="wide"
)

# ============================================================================
# CALCULATOR FUNCTIONS
# ============================================================================

def calculate_sacco_returns(principal: float, monthly_contrib: float, annual_rate: float) -> dict:
    """Calculate SACCO investment returns with simple annual interest."""
    total_contributions = principal + (monthly_contrib * 12)
    interest_earned = total_contributions * (annual_rate / 100)
    final_amount = total_contributions + interest_earned
    
    return {
        "principal": principal,
        "monthly_contribution": monthly_contrib,
        "total_contributions": total_contributions,
        "annual_rate": annual_rate,
        "interest_earned": interest_earned,
        "final_amount": final_amount
    }


def calculate_mmf_returns(principal: float, days_invested: int, annual_rate: float) -> dict:
    """Calculate MMF investment returns with daily compounding."""
    daily_rate = annual_rate / 365 / 100
    final_amount = principal * ((1 + daily_rate) ** days_invested)
    interest_earned = final_amount - principal
    
    return {
        "principal": principal,
        "days_invested": days_invested,
        "annual_rate": annual_rate,
        "daily_rate_percent": daily_rate * 100,
        "interest_earned": interest_earned,
        "final_amount": final_amount
    }


# ============================================================================
# HEADER
# ============================================================================

st.title("🇰🇪 SACCO Financial Calculator")
st.markdown("#### Kenya SACCOs - Investment Returns Calculator")
st.divider()


# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    Calculate SACCO and MMF investment returns.
    
    **SACCO**: Simple annual interest
    **MMF**: Daily compounding returns
    """)


# ============================================================================
# MAIN CONTENT - TABS
# ============================================================================

tab1, tab2 = st.tabs(["📊 SACCO Calculator", "💰 MMF Calculator"])

# ============================================================================
# TAB 1: SACCO
# ============================================================================

with tab1:
    st.header("SACCO Interest Calculator")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        principal = st.number_input(
            "Principal (KES)",
            min_value=0.0,
            value=50000.0,
            step=1000.0
        )
    
    with col2:
        monthly = st.number_input(
            "Monthly Contribution (KES)",
            min_value=0.0,
            value=5000.0,
            step=500.0
        )
    
    with col3:
        rate = st.number_input(
            "Annual Rate (%)",
            min_value=0.0,
            max_value=100.0,
            value=8.0,
            step=0.5
        )
    
    if st.button("Calculate", key="sacco"):
        result = calculate_sacco_returns(principal, monthly, rate)
        
        st.divider()
        st.subheader("Results")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Principal", f"KES {result['principal']:,.0f}")
        
        with col2:
            st.metric("Total Contributions", f"KES {result['total_contributions']:,.0f}")
        
        with col3:
            st.metric("Interest Earned", f"KES {result['interest_earned']:,.2f}")
        
        with col4:
            st.metric("Final Amount", f"KES {result['final_amount']:,.2f}")
        
        st.divider()
        st.write("**Breakdown:**")
        
        data = {
            "Item": [
                "Initial Principal",
                "Monthly Contribution × 12",
                "Total Contributions",
                "Interest Rate",
                "Interest Earned",
                "Final Amount"
            ],
            "Value": [
                f"KES {result['principal']:,.2f}",
                f"KES {result['monthly_contribution'] * 12:,.2f}",
                f"KES {result['total_contributions']:,.2f}",
                f"{result['annual_rate']:.2f}%",
                f"KES {result['interest_earned']:,.2f}",
                f"KES {result['final_amount']:,.2f}"
            ]
        }
        
        st.table(data)


# ============================================================================
# TAB 2: MMF
# ============================================================================

with tab2:
    st.header("Money Market Fund (MMF) Calculator")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        investment = st.number_input(
            "Investment Amount (KES)",
            min_value=0.0,
            value=100000.0,
            step=5000.0
        )
    
    with col2:
        days = st.number_input(
            "Days Invested",
            min_value=1,
            value=90,
            step=1
        )
    
    with col3:
        mmf_rate = st.number_input(
            "Annual Rate (%)",
            min_value=0.0,
            max_value=50.0,
            value=6.0,
            step=0.1
        )
    
    if st.button("Calculate", key="mmf"):
        result = calculate_mmf_returns(investment, days, mmf_rate)
        
        st.divider()
        st.subheader("Results")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Investment", f"KES {result['principal']:,.0f}")
        
        with col2:
            st.metric("Days", f"{result['days_invested']}")
        
        with col3:
            st.metric("Interest Earned", f"KES {result['interest_earned']:,.2f}")
        
        with col4:
            st.metric("Final Value", f"KES {result['final_amount']:,.2f}")
        
        st.divider()
        st.write("**Breakdown:**")
        
        data = {
            "Item": [
                "Investment Amount",
                "Days Invested",
                "Annual Rate",
                "Daily Rate",
                "Interest Earned",
                "Final Value",
                "Return %"
            ],
            "Value": [
                f"KES {result['principal']:,.2f}",
                f"{result['days_invested']} days",
                f"{result['annual_rate']:.2f}%",
                f"{result['daily_rate_percent']:.4f}%",
                f"KES {result['interest_earned']:,.2f}",
                f"KES {result['final_amount']:,.2f}",
                f"{(result['interest_earned'] / result['principal'] * 100):.3f}%"
            ]
        }
        
        st.table(data)


# ============================================================================
# FOOTER
# ============================================================================

st.divider()
st.markdown("""
---
**Disclaimer:** For educational purposes only.  
**Developer:** Martin Gitau | **Email:** tiamsparrow@gmail.com
""")
