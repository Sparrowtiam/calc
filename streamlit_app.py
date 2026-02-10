"""
Streamlit Web App - SACCO Financial Calculator
=============================================
Interactive web interface for SACCO and MMF calculations using Streamlit
"""

import streamlit as st
import requests
from datetime import datetime
from typing import Optional


# ============================================================================
# CALCULATOR FUNCTIONS (From financial_calculator.py)
# ============================================================================

def calculate_sacco_returns(principal: float, monthly_contrib: float, annual_rate: float) -> dict:
    """
    Calculate SACCO investment returns.
    
    Formula:
    - Total contributions = principal + (monthly_contribution × 12)
    - Interest earned = Total contributions × (annual_rate / 100)
    - Final amount = Total contributions + Interest earned
    """
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
    """
    Calculate MMF investment returns using daily compounding.
    
    Formula (Daily Compounding):
    Final Amount = Principal × (1 + (annual_rate / 100) / 365) ^ days_invested
    Interest Earned = Final Amount - Principal
    """
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
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="SACCO Financial Calculator",
    page_icon="🇰🇪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 18px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# HEADER
# ============================================================================

st.title("🇰🇪 SACCO Financial Calculator")
st.markdown("### Kenya SACCOs - Investment Returns Calculator")
st.markdown("---")

# ============================================================================
# SIDEBAR - INFO
# ============================================================================

with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    **SACCO Financial Calculator** helps Kenyan SACCO members calculate:
    
    1. **SACCO Returns** - Annual interest on contributions
    2. **MMF Returns** - Money Market Fund daily compounding
    
    All amounts in **KES** (Kenyan Shillings)
    """)
    
    st.divider()
    st.markdown("""
    **Formulas Used:**
    
    **SACCO (Simple Interest):**
    - Total = Principal + (Monthly × 12)
    - Interest = Total × (Rate / 100)
    
    **MMF (Daily Compound):**
    - Final = Principal × (1 + Daily Rate)^Days
    """)
    
    st.divider()
    st.markdown("*Created for SACCO Members in Kenya*")


# ============================================================================
# MAIN TABS
# ============================================================================

tab1, tab2 = st.tabs(["📊 SACCO Calculator", "💰 MMF Calculator"])

# ============================================================================
# TAB 1: SACCO CALCULATOR
# ============================================================================

with tab1:
    st.header("SACCO Interest Calculator")
    st.markdown("Calculate your SACCO returns over 12 months")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        principal = st.number_input(
            "Initial Principal (KES)",
            min_value=0.0,
            value=50000.0,
            step=1000.0,
            help="Your initial investment in the SACCO"
        )
    
    with col2:
        monthly_contrib = st.number_input(
            "Monthly Contribution (KES)",
            min_value=0.0,
            value=5000.0,
            step=500.0,
            help="Amount you contribute each month"
        )
    
    with col3:
        annual_rate = st.number_input(
            "Annual Interest Rate (%)",
            min_value=0.0,
            max_value=100.0,
            value=8.0,
            step=0.5,
            help="SACCO annual interest rate"
        )
    
    # Calculate SACCO returns
    if st.button("Calculate SACCO Returns", key="sacco_calc"):
        sacco_results = calculate_sacco_returns(principal, monthly_contrib, annual_rate)
        
        # Display results in columns
        st.divider()
        st.subheader("📈 Results After 1 Year")
        
        result_col1, result_col2, result_col3, result_col4 = st.columns(4)
        
        with result_col1:
            st.metric(
                "Initial Principal",
                f"KES {sacco_results['principal']:,.2f}"
            )
        
        with result_col2:
            st.metric(
                "Total Contributions",
                f"KES {sacco_results['total_contributions']:,.2f}",
                delta=f"+{sacco_results['total_contributions'] - sacco_results['principal']:,.2f}"
            )
        
        with result_col3:
            st.metric(
                "Interest Earned",
                f"KES {sacco_results['interest_earned']:,.2f}",
                f"{annual_rate}%"
            )
        
        with result_col4:
            st.metric(
                "🎯 Final Amount",
                f"KES {sacco_results['final_amount']:,.2f}",
                delta=f"+{sacco_results['interest_earned']:,.2f}",
                delta_color="off"
            )
        
        # Display summary table
        st.divider()
        summary_data = {
            "Item": [
                "Initial Principal",
                "Monthly Contribution",
                "Number of Months",
                "Total Contributions",
                "Annual Interest Rate",
                "Interest Earned",
                "Final Amount"
            ],
            "Value": [
                f"KES {sacco_results['principal']:,.2f}",
                f"KES {sacco_results['monthly_contribution']:,.2f}",
                "12",
                f"KES {sacco_results['total_contributions']:,.2f}",
                f"{sacco_results['annual_rate']:.2f}%",
                f"KES {sacco_results['interest_earned']:,.2f}",
                f"KES {sacco_results['final_amount']:,.2f}"
            ]
        }
        
        st.table(summary_data)


# ============================================================================
# TAB 2: MMF CALCULATOR
# ============================================================================

with tab2:
    st.header("Money Market Fund (MMF) Calculator")
    st.markdown("Calculate your MMF investment returns with daily compounding")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        investment_amount = st.number_input(
            "Investment Amount (KES)",
            min_value=0.0,
            value=100000.0,
            step=5000.0,
            help="Amount to invest in MMF"
        )
    
    with col2:
        days_invested = st.number_input(
            "Days Invested",
            min_value=1,
            value=90,
            step=1,
            help="Number of days money is invested"
        )
    
    with col3:
        # Option to fetch or manual input for MMF rate
        rate_source = st.radio(
            "MMF Rate Source",
            ["Enter Manually", "Fetch from Kenya (Beta)"],
            index=0
        )
        
        if rate_source == "Enter Manually":
            mmf_rate = st.number_input(
                "MMF Annual Interest Rate (%)",
                min_value=0.0,
                max_value=50.0,
                value=6.0,
                step=0.1,
                help="Annual interest rate for MMF"
            )
        else:
            # Try to fetch rate
            with st.spinner("Fetching latest MMF rates..."):
                try:
                    response = requests.get("https://www.cytonn.com/", timeout=3)
                    mmf_rate = st.number_input(
                        "MMF Annual Interest Rate (%)",
                        min_value=0.0,
                        max_value=50.0,
                        value=6.0,
                        step=0.1,
                        help="Enter MMF rate manually"
                    )
                    st.info("⚠️ Could not auto-fetch. Please enter rate manually.")
                except:
                    mmf_rate = st.number_input(
                        "MMF Annual Interest Rate (%)",
                        min_value=0.0,
                        max_value=50.0,
                        value=6.0,
                        step=0.1,
                        help="Enter MMF rate manually"
                    )
                    st.warning("⚠️ No internet connection. Entering rate manually.")
    
    # Calculate MMF returns
    if st.button("Calculate MMF Returns", key="mmf_calc"):
        mmf_results = calculate_mmf_returns(investment_amount, days_invested, mmf_rate)
        
        # Display results in columns
        st.divider()
        st.subheader("📈 Investment Results")
        
        result_col1, result_col2, result_col3, result_col4 = st.columns(4)
        
        with result_col1:
            st.metric(
                "Investment Amount",
                f"KES {mmf_results['principal']:,.2f}"
            )
        
        with result_col2:
            st.metric(
                "Days Invested",
                f"{mmf_results['days_invested']} days"
            )
        
        with result_col3:
            st.metric(
                "Interest Earned",
                f"KES {mmf_results['interest_earned']:,.2f}",
                f"{mmf_rate}% p.a."
            )
        
        with result_col4:
            st.metric(
                "🎯 Final Value",
                f"KES {mmf_results['final_amount']:,.2f}",
                delta=f"+{mmf_results['interest_earned']:,.2f}",
                delta_color="off"
            )
        
        # Display summary table
        st.divider()
        summary_data = {
            "Item": [
                "Initial Investment",
                "Days Invested",
                "Annual Rate",
                "Daily Rate",
                "Interest Earned",
                "Final Value",
                "Return %"
            ],
            "Value": [
                f"KES {mmf_results['principal']:,.2f}",
                f"{mmf_results['days_invested']} days",
                f"{mmf_results['annual_rate']:.2f}%",
                f"{mmf_results['daily_rate_percent']:.4f}%",
                f"KES {mmf_results['interest_earned']:,.2f}",
                f"KES {mmf_results['final_amount']:,.2f}",
                f"{(mmf_results['interest_earned'] / mmf_results['principal'] * 100):.3f}%"
            ]
        }
        
        st.table(summary_data)
        
        # Additional info
        st.info(
            f"💡 With daily compounding at {mmf_rate}% annual rate, "
            f"your KES {mmf_results['principal']:,.0f} investment will earn "
            f"KES {mmf_results['interest_earned']:,.2f} in {mmf_results['days_invested']} days."
        )


# ============================================================================
# FOOTER
# ============================================================================

st.divider()
st.markdown("""
---
**Disclaimer:** This calculator is for educational purposes only. 
Actual returns may vary based on market conditions and SACCO policies.
""")
