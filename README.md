# Copilot PR Review Test

This repository tests GitHub Copilot's code review capabilities - specifically whether it validates implementations against linked issue requirements, or only performs technical code analysis.

## 🎯 Test Goal

**Research Question:** Does GitHub Copilot's PR review feature detect when a PR doesn't implement what the linked issue requested?

**Method:** Create intentionally mismatched PR → Request Copilot review → Analyze if it notices the mismatch

---

## ✅ Status: Ready for Manual Execution

**Automated Portions Complete:**
- ✓ Repository baseline established (calculator.py with add/subtract)
- ✓ Complete documentation package created
- ✓ All code and docs tested and validated

**Your Action Required:** Execute Steps 3-9 manually (~25 minutes)

---

## 🚀 Quick Start

### For Fast Execution (Recommended)
1. Read: [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - Overview of what's done and what's needed (5 min)
2. Execute: [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - 7-step checklist with commands (~25 min)
3. Reference: [MANUAL_STEPS.md](MANUAL_STEPS.md) - Detailed instructions when needed

### For Technical Understanding
- Read: [API_LIMITATIONS.md](API_LIMITATIONS.md) - Why Steps 3-9 require manual execution
- Then follow the Quick Start path above

---

## 📚 Complete Documentation Set

| Document | Purpose | Size | Audience |
|----------|---------|------|----------|
| **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** | What's done, what's next | 6.2 KB | Everyone (start here) |
| **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** | Fast execution checklist | 2.2 KB | Action-oriented users |
| **[MANUAL_STEPS.md](MANUAL_STEPS.md)** | Detailed step-by-step guide | 7.4 KB | First-time executors |
| **[API_LIMITATIONS.md](API_LIMITATIONS.md)** | Why automation fails | 6.9 KB | Technical/curious users |
| **[AGENTS.md](AGENTS.md)** | Original test specification | 4.0 KB | Reference |

---

## 📊 What You'll Discover

After completing the manual steps, you'll have evidence to answer:

**Is Copilot Requirement-Aware?**
- ✅ **YES** - It validates PRs against issue acceptance criteria
- ❌ **NO** - It only does technical code review
- ⚠️ **PARTIAL** - Some awareness but inconsistent

**Deliverable:** Comparison of two Copilot reviews (mismatched vs correct implementation)

---

## 🔧 Why Manual Steps Required?

**TL;DR:** GitHub API limitations and test design requirements

**Key Blockers:**
1. No API endpoint for Copilot review requests (@copilot is UI-only)
2. MCP tools can't create markdown-formatted issues
3. Test needs intentionally wrong code (automation would fix it)
4. Analysis requires human qualitative judgment

**Full details:** [API_LIMITATIONS.md](API_LIMITATIONS.md)

---

## 📁 Repository Structure

- `calculator.py` - Test baseline (add/subtract functions)
- `IMPLEMENTATION_SUMMARY.md` - ⭐ **Start here** - Complete overview
- `QUICK_REFERENCE.md` - ⚡ Fast execution checklist
- `MANUAL_STEPS.md` - 📖 Detailed instructions
- `API_LIMITATIONS.md` - 🔧 Technical deep-dive
- `AGENTS.md` - 📋 Original test specification
- `LICENSE` - MIT License
- `README.md` - This file

---

## ⏱️ Time Estimate

- **Documentation Review:** 5-10 minutes
- **Manual Steps Execution:** 20-25 minutes
- **Analysis & Documentation:** 5-10 minutes
- **Total:** ~30-45 minutes

---

## 🎯 Expected Workflow

```bash
# 1. Read the overview
open IMPLEMENTATION_SUMMARY.md

# 2. Follow the quick reference
open QUICK_REFERENCE.md

# 3. Execute Step 3: Create Issue
# → Go to GitHub, create issue with acceptance criteria

# 4. Execute Steps 4-5: Create wrong implementation + PR
git checkout -b feature/add-multiply
# → Edit calculator.py with divide() instead of multiply()
git push origin feature/add-multiply
# → Create PR linking to issue

# 5. Execute Step 6: Request @copilot review
# → Add @copilot as reviewer in GitHub UI

# 6. Execute Step 7: Analyze first review
# → Screenshot/document Copilot's feedback

# 7. Execute Step 8: Create correct implementation
git checkout -b feature/add-multiply-correct
# → Edit calculator.py with proper multiply()
git push origin feature/add-multiply-correct
# → Create PR, request @copilot review

# 8. Execute Step 9: Compare reviews
# → Document differences, draw conclusions
```

---

## 💡 Support

**Questions about:**
- **What to do?** → [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- **How to do it?** → [MANUAL_STEPS.md](MANUAL_STEPS.md)
- **Why manual?** → [API_LIMITATIONS.md](API_LIMITATIONS.md)
- **What's the goal?** → This README (you're here!)

---

## 📜 License

MIT License - See [LICENSE](LICENSE)

---

**Ready to start?** → [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) ⭐
