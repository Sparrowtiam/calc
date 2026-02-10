"""
Quick test of financial calculator functions (non-interactive)
"""
from financial_calculator import (
    calculate_sacco_returns,
    display_sacco_results,
    calculate_mmf_returns,
    display_mmf_results
)

print("="*70)
print("TEST 1: SACCO CALCULATION")
print("="*70)

sacco_results = calculate_sacco_returns(
    principal=50000,           # KES 50,000 initial
    monthly_contrib=5000,      # KES 5,000 per month
    annual_rate=8              # 8% annual interest
)
display_sacco_results(sacco_results)

print("\n" + "="*70)
print("TEST 2: MMF CALCULATION")
print("="*70)

mmf_results = calculate_mmf_returns(
    principal=100000,          # KES 100,000 investment
    days_invested=90,          # 90 days invested
    annual_rate=6              # 6% annual interest rate
)
display_mmf_results(mmf_results)

print("\n" + "="*70)
print("✓ All tests completed successfully!")
print("="*70)
