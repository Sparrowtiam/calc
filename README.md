# SACCO Financial Calculator - Kenya

A Python financial calculator for SACCO members in Kenya. Calculates SACCO interest returns and Money Market Fund (MMF) investment returns.

**🌐 Live Demo**: Coming soon on Streamlit Cloud  
**💻 GitHub**: [sacco-calculator](https://github.com/)  
**📚 Docs**: See [DEPLOYMENT.md](DEPLOYMENT.md) for setup & deployment instructions

## Features

### Web Interface (Streamlit)
- Interactive web dashboard for SACCO and MMF calculations
- Real-time calculation results
- Beautiful data visualization
- Mobile-friendly interface
- **Run locally**: `streamlit run streamlit_app.py`

### Section 1: SACCO Interest Calculation
- Calculate total contributions over 12 months (principal + monthly contributions)
- Compute annual interest earned (simple interest)
- Display final amount after 1 year
- Input validation for all entries

### Section 2: Money Market Fund (MMF) Calculation
- Fetch latest MMF rates from Kenyan sources (Cytonn, CBK, etc.)
- Fallback to manual rate entry if internet unavailable
- Calculate daily compounding returns
- Support for custom investment duration

## Requirements

- Python 3.8+
- `requests` library (for fetching MMF rates)

## Installation

1. Create and activate virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # On Windows PowerShell
# or
source .venv/bin/activate     # On macOS/Linux
```

2. Install dependencies:
```bash
pip install requests
```

## Usage

### Option 1: Web Interface (Recommended)
Run the interactive Streamlit app:
```bash
streamlit run streamlit_app.py
```
Opens in browser at `http://localhost:8501`

### Option 2: Interactive Command Line
Run the main calculator script:
```bash
python financial_calculator.py
```

## Example Calculation Results

### SACCO Example:
- Principal: KES 50,000
- Monthly Contribution: KES 5,000
- Annual Rate: 8%
- **Results:**
  - Total Contributions: KES 110,000
  - Interest Earned: KES 8,800
  - **Final Amount: KES 118,800**

### MMF Example:
- Investment Amount: KES 100,000
- Days Invested: 90
- Annual Rate: 6%
- **Results:**
  - Daily Rate: 0.0164%
  - Interest Earned: KES 1,490.33
  - **Final Value: KES 101,490.33**

## Formulas Used

### SACCO (Simple Interest)
```
Total Contributions = Principal + (Monthly Contribution × 12)
Interest = Total Contributions × (Annual Rate / 100)
Final Amount = Total Contributions + Interest
```

### MMF (Daily Compounding)
```
Daily Rate = Annual Rate / 365 / 100
Final Amount = Principal × (1 + Daily Rate) ^ Days
Interest = Final Amount - Principal
```

## File Structure

```
sacco/
├── financial_calculator.py    # Core calculator functions
├── streamlit_app.py           # Web interface (Streamlit)
├── test_calculator.py         # Test/demo script
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation
├── DEPLOYMENT.md              # Deployment guide
├── .gitignore                 # Git ignores
└── .venv/                     # Virtual environment
```

## Notes

- All amounts are in Kenyan Shillings (KES)
- SACCO calculation uses simple annual interest
- MMF calculation uses daily compounding for accuracy
- MMF rates default to manual input if network fetch fails
- Input validation prevents negative amounts and unrealistic rates

## 🚀 Deployment

### GitHub
1. Initialize Git and push to GitHub
2. See [DEPLOYMENT.md](DEPLOYMENT.md) for step-by-step instructions

### Streamlit Cloud
1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Auto-deploys on every git push!
4. Share live URL with SACCO members

**Full setup guide**: [DEPLOYMENT.md](DEPLOYMENT.md)

## License

Created for SACCO members in Kenya - 2026
