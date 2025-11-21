# Quick Reference: Completing AGENTS.md Test

## ✅ What's Done
Steps 1-2 automated ✓ (calculator.py exists with add/subtract)

## 📝 What You Need to Do

### 1. Create Issue (5 min)
**URL:** https://github.com/ltpitt/copilot-pr-review-test/issues/new  
**Title:** "Add multiplication function"  
**Body:** Copy from MANUAL_STEPS.md Step 3  
**Note:** Remember the issue number!

---

### 2. Create WRONG Implementation Branch (2 min)
```bash
git checkout main && git pull
git checkout -b feature/add-multiply

# Copy the WRONG implementation from MANUAL_STEPS.md Step 4
# (divide() + send_analytics() instead of multiply())

git add calculator.py
git commit -m "Add multiplication function"
git push origin feature/add-multiply
```

---

### 3. Create PR #1 (Mismatched) (2 min)
**URL:** https://github.com/ltpitt/copilot-pr-review-test/compare/main...feature/add-multiply  
**Title:** "Add multiplication function"  
**Body:** "Fixes #[ISSUE_NUMBER]"  
**Action:** Request `@copilot` review

---

### 4. Analyze First Review (5 min)
**Look for:**
- Does it mention the issue requirements?
- Does it notice multiply() is missing?
- Does it flag unrelated functions?

**Screenshot or copy the review text!**

---

### 5. Create CORRECT Implementation Branch (2 min)
```bash
git checkout main
git checkout -b feature/add-multiply-correct

# Copy the CORRECT implementation from MANUAL_STEPS.md Step 8
# (proper multiply() function)

git add calculator.py
git commit -m "Add multiply function to calculator"
git push origin feature/add-multiply-correct
```

---

### 6. Create PR #2 (Correct) (2 min)
**URL:** https://github.com/ltpitt/copilot-pr-review-test/compare/main...feature/add-multiply-correct  
**Title:** "Add multiplication function (correct implementation)"  
**Body:** "Fixes #[ISSUE_NUMBER]"  
**Action:** Request `@copilot` review

---

### 7. Compare Reviews (5 min)
Fill out comparison table in MANUAL_STEPS.md and draw conclusion:
- **Is Copilot requirement-aware?** YES / NO / PARTIAL
- **Evidence?** Quote specific review comments

---

## 🎯 Total Time: ~25 minutes

## 📄 For Full Details
See: [MANUAL_STEPS.md](./MANUAL_STEPS.md)
