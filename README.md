# Copilot PR Review Test

This repository is designed to test GitHub Copilot's code review capabilities and validate whether it can detect when PR implementations don't match issue requirements.

## 🚀 Quick Start

**Steps 1-2 of AGENTS.md are complete!** (calculator.py baseline established)

**To complete the test:**
1. See [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for a condensed checklist (~25 min)
2. Or see [MANUAL_STEPS.md](MANUAL_STEPS.md) for detailed step-by-step instructions

## Test Plan Overview

See [AGENTS.md](AGENTS.md) for the original complete test plan.

## 📁 Repository Structure

- `calculator.py` - Simple calculator with basic arithmetic functions (test baseline)
- `AGENTS.md` - Original detailed test plan for validating Copilot code review
- `MANUAL_STEPS.md` - Detailed manual steps to complete remaining test phases (Steps 3-9)
- `QUICK_REFERENCE.md` - Quick checklist version of manual steps

## ℹ️ Implementation Status

- ✅ **Automated Steps (1-2):** Repository setup with calculator.py baseline
- 🔧 **Manual Steps (3-9):** Require GitHub UI interaction (issue creation, PR workflow, @copilot reviews)
  - These cannot be automated via GitHub API/MCP tools due to limitations around issue formatting, Copilot review requests, and the need for human analysis

## 🎯 Test Goal

Determine if GitHub Copilot's PR review feature:
- **Validates implementations against linked issue requirements**
- Or only provides generic technical code review without requirement awareness
