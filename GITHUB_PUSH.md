# ⚡ PUSH TO GITHUB - Quick Guide

## Your Repository Details
- **URL**: https://github.com/Sparrowtiam/calc.git
- **Developer**: Martin Gitau
- **Email**: tiamsparrow@gmail.com4ewsesedwseds

---

## 🔧 Option 1: Command Line Push (Recommended)

### Step 1: Install Git
1. Download: https://git-scm.com/download/win
2. Run installer (accept all defaults)
3. Restart PowerShell

### Step 2: Configure Git
```powershell
git config --global user.name "Martin Gitau"
git config --global user.email "tiamsparrow@gmail.com4ewsesedwseds"
```

### Step 3: Initialize & Push
```powershell
cd C:\Users\HP\ai\sacco

# Initialize git (if not done)
git init

# Add remote repository
git remote add origin https://github.com/Sparrowtiam/calc.git

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: SACCO financial calculator with Streamlit"

# Push to GitHub
git branch -M main
git push -u origin main
```

**Note:** First push may prompt for GitHub authentication:
- Use your GitHub username & personal access token (or password)
- Or use GitHub Desktop for easier authentication

---

## 🌐 Option 2: GitHub Web UI (No Installation)

1. Go to: https://github.com/Sparrowtiam/calc
2. Click **"Add file"** → **"Upload files"**
3. Upload these files:
   - `financial_calculator.py`
   - `streamlit_app.py`
   - `test_calculator.py`
   - `requirements.txt`
   - `README.md`
   - `DEPLOYMENT.md`
   - `.gitignore`

4. Write commit message: "Initial commit: SACCO calculator with Streamlit"
5. Click **"Commit changes"**

---

## 📱 Option 3: GitHub Desktop (GUI)

If you find command line confusing:

1. Download: https://desktop.github.com/
2. Install & sign in with your GitHub account
3. Click "File" → "Clone Repository"
4. Paste: `https://github.com/Sparrowtiam/calc.git`
5. Open folder: `C:\Users\HP\ai\sacco`
6. Drag calculator files into the repo folder
7. Write commit message & click "Commit to main"
8. Click "Push origin"

---

## ✅ After Push

Once pushed, verify at:
```
https://github.com/Sparrowtiam/calc
```

Then deploy to Streamlit Cloud with these steps:

1. Go to: https://streamlit.io/cloud
2. Click "New app"
3. Select repository: `Sparrowtiam/calc`
4. Select branch: `main`
5. File path: `streamlit_app.py`
6. Click "Deploy"

Your app will be live at: `https://calc-sparrowtiam.streamlit.app` (or similar)

---

## 🆘 Troubleshooting

### "Git not recognized"
- Git not installed yet - download from https://git-scm.com/download/win

### "Authentication failed"
- Generate Personal Access Token: https://github.com/settings/tokens
- Use token instead of password when pushing

### "Remote already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/Sparrowtiam/calc.git
```

---

**Next Steps:**
1. Install Git (if using Option 1)
2. Choose your push method
3. Deploy to Streamlit Cloud
4. Share your live calculator with SACCO members! 🇰🇪
