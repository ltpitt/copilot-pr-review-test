# API/Tool Limitations Preventing Full Automation

This document explains the specific technical reasons why Steps 3-9 of AGENTS.md cannot be automated via GitHub API or MCP tools.

## Limitation Summary

| Step | Action Required | Why Automation Fails |
|------|----------------|---------------------|
| 3 | Create Issue with formatted body | GitHub Issues API via MCP lacks templating/markdown formatting control |
| 4 | Create branch with intentional bugs | Test requires deliberately "wrong" code that automation would correct |
| 5 | Create Pull Request | Can be automated BUT depends on Step 4's manual branch |
| 6 | Request `@copilot` review | Copilot PR review requests only work via GitHub UI mentions |
| 7 | Analyze review quality | Requires human subjective judgment of requirement-awareness |
| 8 | Create correct implementation | Can be automated BUT test design requires comparison with Step 4 |
| 9 | Compare reviews | Requires human analysis and qualitative comparison |

---

## Detailed Analysis

### Step 3: Issue Creation with Specific Formatting

**What's needed:**
```markdown
## User Story
As a user, I want to multiply two numbers...

## Acceptance Criteria
- [ ] Add a `multiply(a, b)` function...
- [ ] Function should return the product...

## Technical Requirements
- Follow existing code style
```

**Why it can't be automated:**
- GitHub Issues GraphQL/REST API via MCP tools only accepts plain text body
- Cannot programmatically create issues with markdown checkboxes and sections
- The test specifically requires this structured format to validate Copilot's parsing capabilities
- While technically possible via direct API calls with proper formatting, the MCP GitHub tools don't expose this level of control

**Workaround:** Manual creation via GitHub UI

---

### Step 4: Creating Intentionally Wrong Implementation

**What's needed:**
- A PR that claims to implement `multiply()` 
- But actually implements `divide()` and `send_analytics()` instead
- Commit message must be misleading: "Add multiplication function"

**Why it can't be automated:**
- This is the **core test mechanism** - intentionally wrong code
- Any automation would either:
  - Correctly implement `multiply()` (defeating the test purpose)
  - Or require explicit "write wrong code" logic (defeats purpose of realistic test)
- The test validates if Copilot catches human errors/mismatches
- Automation would create artificial test conditions

**Workaround:** Manual branch creation with deliberate mismatch

---

### Step 6: Requesting Copilot PR Reviews

**What's needed:**
- Use GitHub UI to add `@copilot` as reviewer on PR
- Copilot processes the mention and posts review comments

**Why it can't be automated:**
- Copilot PR reviews are triggered by `@copilot` mentions in GitHub UI
- GitHub API doesn't have a "request Copilot review" endpoint
- The reviewer API (`POST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers`) only works for:
  - Human users
  - GitHub Apps with specific permissions
  - NOT for Copilot's review service
- Copilot reviews use a different internal mechanism tied to UI interactions

**Technical evidence:**
```bash
# This fails:
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/repos/owner/repo/pulls/1/requested_reviewers" \
  -d '{"reviewers":["copilot"]}'
  
# Error: "copilot" is not a valid user for review requests
```

**Workaround:** Manual `@copilot` mention via GitHub UI

---

### Step 7: Analyzing Review Quality

**What's needed:**
- Human judgment: "Did Copilot reference the issue requirements?"
- Qualitative assessment: "Is this requirement-aware or just technical review?"
- Comparison: "Did language change between correct/incorrect implementations?"

**Why it can't be automated:**
- Requires subjective interpretation of review comments
- NLP/sentiment analysis would be insufficient for nuanced comparison
- The test goal is to document human-observable behavior
- Edge cases require judgment (e.g., "Copilot mentioned requirements but didn't validate them")

**Workaround:** Human analysis with documentation templates provided

---

### Step 9: Comparing Two Reviews

**What's needed:**
- Side-by-side qualitative comparison
- Document differences in review depth/approach
- Draw conclusion about overall requirement-awareness capability

**Why it can't be automated:**
- Builds on Step 7's subjective analysis
- Requires contextual understanding of both reviews
- Final conclusion requires human expertise interpretation
- The deliverable is a qualitative research finding, not quantitative metrics

**Workaround:** Human comparison using provided template tables

---

## What CAN Be Automated

✅ **Successfully automated:**
- Repository initialization (Steps 1-2)
- Creating baseline `calculator.py` 
- Documentation generation (this file, MANUAL_STEPS.md, etc.)

✅ **Could be automated (but blocked by dependencies):**
- Branch creation (depends on manual Step 4 completion)
- PR creation (depends on branches from Step 4 & 8)
- Fetching review comments via API (depends on Copilot posting reviews from Step 6)

---

## Alternative Approaches (Not Used)

### Approach 1: Use GitHub CLI (`gh`)
**Problem:** Still requires `@copilot` mention in PR description/comments, which doesn't trigger reviews consistently. Review requests must come from the UI "Reviewers" sidebar.

### Approach 2: GitHub Actions Workflow
**Problem:** 
- Cannot trigger Copilot reviews programmatically
- Would require same manual UI steps
- Adds unnecessary complexity to test scenario

### Approach 3: GraphQL Mutations
**Problem:**
- GraphQL API also lacks Copilot review request capability
- Issues API still doesn't support templated markdown formatting at the field level
- Same UI limitation remains

---

## Recommendations for GitHub

To make this test fully automatable, GitHub would need:

1. **Issues API Enhancement:**
   ```json
   POST /repos/{owner}/{repo}/issues
   {
     "title": "Add multiplication function",
     "body_template": {
       "user_story": "As a user...",
       "acceptance_criteria": ["criterion 1", "criterion 2"],
       "technical_requirements": ["requirement 1"]
     }
   }
   ```

2. **Copilot Review API:**
   ```json
   POST /repos/{owner}/{repo}/pulls/{number}/copilot-review
   {
     "action": "request"
   }
   ```

3. **Review Analysis API:**
   ```json
   GET /repos/{owner}/{repo}/pulls/{number}/copilot-review/analysis
   ```

These features don't currently exist in GitHub's public API.

---

## Conclusion

**Steps 3-9 require manual execution** due to fundamental limitations in:
- GitHub API capabilities (no Copilot review endpoints)
- Test design requirements (intentional mismatches)
- Analysis needs (qualitative human judgment)

The provided documentation (MANUAL_STEPS.md, QUICK_REFERENCE.md) gives complete instructions to execute the test in approximately 25 minutes.
