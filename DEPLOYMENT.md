# 🚀 DEPLOYMENT GUIDE

## Quick Start - Run Streamlit Locally

```bash
cd c:\Users\HP\ai\sacco
.\.venv\Scripts\activate
streamlit run streamlit_app.py
```

This opens the app in your browser at `http://localhost:8501`

---

## 📤 GitHub Setup & Push

### Step 1: Fix Git PATH (If needed)
Git is installed but not in your PATH. Add it to PATH:

1. Find Git installation:
   - Usually: `C:\Program Files\Git\cmd\git.exe` or `C:\Program Files (x86)\Git\cmd\git.exe`

2. Add to PowerShell session:
```powershell
$env:PATH += ";C:\Program Files\Git\cmd"
git --version
```

Or add Git to permanent PATH via Windows System Environment Variables.

### Step 2: Initialize Git & Commit

```powershell
cd C:\Users\HP\ai\sacco
git config user.email "your-email@example.com"
git config user.name "Your Name"
git init
git add .
git commit -m "Initial commit: SACCO financial calculator with Streamlit"
```

### Step 3: Create GitHub Repo & Push

**Option A: Using GitHub Web UI**
1. Go to https://github.com/new
2. Create repository named `sacco-calculator`
3. Do NOT initialize with README (we already have files)
4. Click Create Repository
5. Follow GitHub's instructions to push existing code:

```powershell
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/sacco-calculator.git
git push -u origin main
```

**Option B: Using GitHub CLI** (if installed)
```bash
gh repo create sacco-calculator --source=. --public --push
```

### Step 4: Verify

Go to: `https://github.com/YOUR-USERNAME/sacco-calculator`

---

## 🌐 Deploy to Streamlit Cloud

### Step 1: Create Streamlit Account
1. Go to https://streamlit.io/cloud
2. Sign up with GitHub account
3. Authorize Streamlit to access your repos

### Step 2: Deploy App

1. Click **"New app"** at https://share.streamlit.io/
2. Select:
   - **Repository**: `your-username/sacco-calculator`
   - **Branch**: `main`
   - **File path**: `streamlit_app.py`
3. Click **Deploy**

Streamlit will build and deploy your app. You'll get a URL like:
```
https://sacco-calculator.streamlit.app
```

### Step 3: Share Your App
- Share the Streamlit URL with anyone
- App updates automatically when you push to GitHub
- No server setup needed!

---

## 📋 Project Files

```
sacco-calculator/
├── financial_calculator.py     # Core calculator functions
├── streamlit_app.py            # Web interface
├── test_calculator.py          # Test suite
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
├── .gitignore                  # Git ignores
└── .venv/                      # Virtual environment
```

---

## 🔧 Development Workflow

1. **Make changes locally**
```powershell
.\.venv\Scripts\activate
streamlit run streamlit_app.py
```

2. **Test changes**
```powershell
python test_calculator.py
```

3. **Commit & Push**
```powershell
git add .
git commit -m "Your message"
git push
```

4. **Auto-deploy to Streamlit Cloud** ✨
   - Streamlit Cloud automatically redeploys when you push!

---

## 📦 Update Dependencies

To install all dependencies in a fresh environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

---

## 🐛 Troubleshooting

### Git not recognized
```powershell
$env:PATH += ";C:\Program Files\Git\cmd"
git --version
```

### Streamlit not starting
```powershell
pip install --upgrade streamlit
streamlit run streamlit_app.py
```

### Module not found errors
```powershell
.\.venv\Scripts\activate
pip install -r requirements.txt
```

---

## ✅ Next Steps

1. ✅ Create GitHub repository
2. ✅ Push code to GitHub
3. ✅ Deploy to Streamlit Cloud
4. ✅ Share Streamlit URL with SACCO members!

---

**Questions?** Check Streamlit docs: https://docs.streamlit.io/
