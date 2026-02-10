"""
Financial Calculator for SACCO Members in Kenya
================================================
Calculates SACCO interest and Money Market Fund (MMF) returns for Kenyan SACCOs.
"""

import requests
from datetime import datetime, timedelta
from typing import Tuple, Optional


# ============================================================================
# SECTION 1: SACCO INTEREST CALCULATION
# ============================================================================

def get_sacco_inputs() -> Tuple[float, float, float]:
    """
    Prompt user for SACCO calculation inputs with validation.
    
    Returns:
        Tuple of (principal, monthly_contribution, annual_rate)
    """
    print("\n" + "="*60)
    print("SECTION 1: SACCO INTEREST CALCULATION")
    print("="*60)
    
    while True:
        try:
            principal = float(input("\nEnter principal amount (KES): "))
            if principal < 0:
                print("❌ Principal amount cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
    
    while True:
        try:
            monthly_contrib = float(input("Enter monthly contribution (KES): "))
            if monthly_contrib < 0:
                print("❌ Monthly contribution cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
    
    while True:
        try:
            annual_rate = float(input("Enter annual interest rate (%): "))
            if annual_rate < 0 or annual_rate > 100:
                print("❌ Interest rate must be between 0 and 100%. Please try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
    
    return principal, monthly_contrib, annual_rate


def calculate_sacco_returns(principal: float, monthly_contrib: float, annual_rate: float) -> dict:
    """
    Calculate SACCO investment returns.
    
    Formula:
    - Total contributions = principal + (monthly_contribution × 12)
    - Interest earned = Total contributions × (annual_rate / 100)
    - Final amount = Total contributions + Interest earned
    
    Args:
        principal: Initial amount (KES)
        monthly_contrib: Monthly contribution (KES)
        annual_rate: Annual interest rate (%)
    
    Returns:
        Dictionary with calculation results
    """
    # Calculate total contributions over 12 months
    total_contributions = principal + (monthly_contrib * 12)
    
    # Calculate interest earned (simple annual interest)
    interest_earned = total_contributions * (annual_rate / 100)
    
    # Calculate final amount
    final_amount = total_contributions + interest_earned
    
    return {
        "principal": principal,
        "monthly_contribution": monthly_contrib,
        "total_contributions": total_contributions,
        "annual_rate": annual_rate,
        "interest_earned": interest_earned,
        "final_amount": final_amount
    }


def display_sacco_results(results: dict) -> None:
    """Display SACCO calculation results in user-friendly format."""
    print("\n" + "-"*60)
    print("📊 SACCO CALCULATION RESULTS (After 1 Year)")
    print("-"*60)
    print(f"Initial Principal:        KES {results['principal']:>12,.2f}")
    print(f"Monthly Contribution:     KES {results['monthly_contribution']:>12,.2f}")
    print(f"Total Contributions:      KES {results['total_contributions']:>12,.2f}")
    print(f"Annual Interest Rate:     {results['annual_rate']:>15.2f}%")
    print("-"*60)
    print(f"Interest Earned:          KES {results['interest_earned']:>12,.2f}")
    print(f"{'FINAL AMOUNT':30} KES {results['final_amount']:>12,.2f}")
    print("-"*60)


# ============================================================================
# SECTION 2: MONEY MARKET FUND (MMF) CALCULATION
# ============================================================================

def fetch_mmf_rate() -> Optional[float]:
    """
    Attempt to fetch the latest MMF rate from Cytonn or other Kenyan sources.
    Falls back to manual input if fetching fails.
    
    Returns:
        MMF annual interest rate (%) or None if unable to fetch
    """
    print("\n" + "="*60)
    print("SECTION 2: MONEY MARKET FUND (MMF) CALCULATION")
    print("="*60)
    print("\nAttempting to fetch latest MMF rate...")
    
    try:
        # Try to fetch from a reliable source (example: generic approach)
        # Note: In production, use specific APIs from CBK, Cytonn, or other providers
        response = requests.get(
            "https://www.cytonn.com/",
            timeout=5
        )
        if response.status_code == 200:
            print("✓ Successfully connected to MMF data source.")
            # In production, parse response for actual rate
            # For now, returning None to trigger manual input
            return None
    except requests.exceptions.RequestException as e:
        print(f"⚠️  Unable to fetch MMF rate: {e}")
    
    return None


def get_mmf_rate_manual() -> float:
    """Prompt user to manually enter MMF annual interest rate."""
    while True:
        try:
            rate = float(input("\nEnter MMF annual interest rate (%): "))
            if rate < 0 or rate > 50:
                print("❌ Rate seems unrealistic. MMF rates typically range 0-15%. Please re-enter.")
                continue
            return rate
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


def get_mmf_inputs() -> Tuple[float, int, float]:
    """
    Prompt user for MMF calculation inputs.
    
    Returns:
        Tuple of (principal, days_invested, annual_rate)
    """
    # Try to fetch MMF rate automatically
    mmf_rate = fetch_mmf_rate()
    if mmf_rate is None:
        mmf_rate = get_mmf_rate_manual()
    
    print(f"\n✓ Using MMF annual rate: {mmf_rate:.2f}%\n")
    
    while True:
        try:
            principal = float(input("Enter MMF investment amount (KES): "))
            if principal < 0:
                print("❌ Investment amount cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
    
    while True:
        try:
            days = int(input("Enter number of days invested: "))
            if days <= 0:
                print("❌ Days invested must be greater than 0. Please try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")
    
    return principal, days, mmf_rate


def calculate_mmf_returns(principal: float, days_invested: int, annual_rate: float) -> dict:
    """
    Calculate MMF investment returns using daily compounding.
    
    Formula (Daily Compounding):
    Final Amount = Principal × (1 + (annual_rate / 100) / 365) ^ days_invested
    Interest Earned = Final Amount - Principal
    
    Args:
        principal: Investment amount (KES)
        days_invested: Number of days money is invested
        annual_rate: Annual interest rate (%)
    
    Returns:
        Dictionary with calculation results
    """
    # Daily interest rate
    daily_rate = annual_rate / 365 / 100
    
    # Calculate final amount with daily compounding
    final_amount = principal * ((1 + daily_rate) ** days_invested)
    
    # Calculate interest earned
    interest_earned = final_amount - principal
    
    return {
        "principal": principal,
        "days_invested": days_invested,
        "annual_rate": annual_rate,
        "daily_rate_percent": daily_rate * 100,
        "interest_earned": interest_earned,
        "final_amount": final_amount
    }


def display_mmf_results(results: dict) -> None:
    """Display MMF calculation results in user-friendly format."""
    print("\n" + "-"*60)
    print("📊 MMF CALCULATION RESULTS")
    print("-"*60)
    print(f"Investment Amount:        KES {results['principal']:>12,.2f}")
    print(f"Days Invested:            {results['days_invested']:>15} days")
    print(f"Annual Interest Rate:     {results['annual_rate']:>15.2f}%")
    print(f"Daily Interest Rate:      {results['daily_rate_percent']:>15.4f}%")
    print("-"*60)
    print(f"Interest Earned:          KES {results['interest_earned']:>12,.2f}")
    print(f"{'FINAL VALUE':30} KES {results['final_amount']:>12,.2f}")
    print("-"*60)


# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """Main program to run SACCO and MMF calculators."""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  🇰🇪 SACCO FINANCIAL CALCULATOR - KENYA 🇰🇪".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")
    
    # SECTION 1: SACCO Calculation
    try:
        principal, monthly_contrib, annual_rate = get_sacco_inputs()
        sacco_results = calculate_sacco_returns(principal, monthly_contrib, annual_rate)
        display_sacco_results(sacco_results)
    except KeyboardInterrupt:
        print("\n\n❌ Calculation interrupted by user.")
        return
    except Exception as e:
        print(f"\n❌ Error in SACCO calculation: {e}")
        return
    
    # SECTION 2: MMF Calculation
    try:
        principal, days, mmf_rate = get_mmf_inputs()
        mmf_results = calculate_mmf_returns(principal, days, mmf_rate)
        display_mmf_results(mmf_results)
    except KeyboardInterrupt:
        print("\n\n❌ Calculation interrupted by user.")
        return
    except Exception as e:
        print(f"\n❌ Error in MMF calculation: {e}")
        return
    
    # Summary
    print("\n" + "="*60)
    print("✓ Financial calculations completed successfully!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
