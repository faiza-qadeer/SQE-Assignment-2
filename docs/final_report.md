# Software Quality Engineering – Assignment 2
## Student Course Registration System

**Student Name:** Faiza Qadeer  
**Class:** BS-SE 5B  
**Course:** Software Quality Engineering

---

# 1. Introduction

The purpose of this assignment was to evaluate the quality and correctness of a Student Course Registration System using black-box testing, white-box testing, and GitHub collaboration tools.

The system was tested against the requirements provided in `REQUIREMENTS.md`. The testing process helped identify defects, measure code coverage, and document the results.

# 2. Part A – Black-Box Testing

## 2.1 Testing Techniques

The following black-box testing techniques were used:

- Equivalence Class Partitioning (ECP)
- Boundary Value Analysis (BVA)
- Decision Table Testing
- Test Case Design
- Test Execution and Result Analysis
- Test Case Optimization

The tests were designed using the functional requirements of the registration system.

## 2.2 Test Execution Results

A total of 44 test cases were executed using pytest.

| Result | Number |
|---|---:|
| Total test cases | 44 |
| Passed | 35 |
| Failed | 9 |

## 2.3 Defects Identified

Five main defect areas were identified:

1. The credit limit function rejects exactly 18 credits.
2. The prerequisite function accepts students who have completed only one of multiple required prerequisites.
3. Positive outstanding dues do not always block registration.
4. The course capacity logic does not correctly return WAITLISTED when a course is full.
5. The withdrawal function does not decrease the course enrollment count.

Some failed test cases exposed the same underlying defect.

## 2.4 Part A Conclusion

Black-box testing identified incorrect behaviors in the original implementation. The failed test cases were retained as evidence of the defects.

# 3. Part B – White-Box Testing

## 3.1 Control Flow Graphs

Control Flow Graphs (CFGs) were prepared for the five main functions:

- `check_credit_limit()`
- `prerequisites_satisfied()`
- `registration_decision()`
- `register_course()`
- `withdraw_course()`

These graphs represent the execution paths and decision points within the functions.

## 3.2 Cyclomatic Complexity

Cyclomatic complexity was calculated using:

**V(G) = Number of decision points + 1**

| Function | Cyclomatic Complexity |
|---|---:|
| check_credit_limit | 3 |
| prerequisites_satisfied | 2 |
| registration_decision | 8 |
| register_course | 4 |
| withdraw_course | 2 |
| **Total** | **19** |

The total of 19 represents the sum of the individual function complexities.

## 3.3 Independent Paths and MC/DC

Independent execution paths were identified for each function.

MC/DC test pairs were also designed to demonstrate how individual conditions affect decisions.

The WAITLISTED decision is unreachable in the original implementation because the capacity validation rejects enrollment values greater than capacity before the waitlist condition is checked.

Therefore, full MC/DC coverage of that decision could not be demonstrated against the original code.

## 3.4 Code Coverage Results

Coverage was measured using pytest-cov.

| Coverage Metric | Result |
|---|---:|
| Total statements | 53 |
| Covered statements | 49 |
| Missed statements | 4 |
| Statement coverage | 92.45% |
| Total branches | 26 |
| Covered branches | 21 |
| Branch coverage | 80.77% |
| Combined coverage reported by pytest | 89% |

The coverage report showed three partially covered branches and the following missing lines: 55, 59, 70–71.

## 3.5 Part B Conclusion

White-box testing helped analyze the internal structure of the program. CFGs, cyclomatic complexity, independent paths, MC/DC scenarios, and coverage measurements were used to evaluate the implementation.

# 4. Part C – GitHub Collaboration

## 4.1 Repository Creation

A public GitHub repository was created:

[ SQE-Assignment-2 ](https://github.com/faiza-qadeer/SQE-Assignment-2)

The repository contains the source code, test cases, requirements, and testing documentation.

## 4.2 Branch Management

The following branches were used:

- `main`
- `testing-improvements`

The testing-improvements branch was created to keep documentation and workflow changes separate from the main branch.

## 4.3 Commits

Important commits included:

| Commit | Description |
|---|---|
| `87dd38a` | Add Part A and Part B testing |
| `10d1956` | Document defects tracked in GitHub issues |
| `e126b10` | Add GitHub Actions automated testing |

## 4.4 GitHub Issues

Five issues were created to document the identified defects:

1. Fix credit limit boundary condition
2. Fix prerequisite validation logic
3. Fix outstanding dues validation
4. Fix course capacity and waitlist logic
5. Fix enrollment count during withdrawal

These issues provide a record of the defects and their expected corrections.

## 4.5 Pull Requests

Two Pull Requests were created and merged into the main branch.

- **Pull Request 1:** Document testing defects and improvements.
- **Pull Request 2:** Add GitHub Actions automated testing.

The Pull Requests were used to review and merge changes from the testing-improvements branch into main.

## 4.6 GitHub Actions

A GitHub Actions workflow was created at:

`.github/workflows/python-tests.yml`

The workflow automatically:

- Checks out the repository.
- Sets up Python.
- Installs project dependencies.
- Executes pytest with coverage measurement.

The workflow was triggered by pushes and pull requests.

The recorded workflow runs failed at the test step because the original implementation contains known defects that cause nine test failures. The workflow was successfully triggered for pushes and pull requests.

# 5. Comparison of Testing Results

Black-box testing focuses on the expected external behavior of the system, while white-box testing examines its internal structure and execution paths.

| Black-Box Testing | White-Box Testing |
|---|---|
| Tests functional requirements | Tests internal code structure |
| Uses ECP, BVA and decision tables | Uses CFGs and path analysis |
| Identifies incorrect outputs | Identifies uncovered statements and branches |
| Reports passed and failed tests | Measures statement and branch coverage |

Both techniques helped identify weaknesses in the Student Course Registration System.

# 6. Final Conclusion

This assignment provided practical experience in software testing and quality assurance.

Black-box testing identified functional defects, while white-box testing examined internal program logic and code coverage. GitHub was used to manage versions, document defects, create branches, and review changes through Pull Requests.

GitHub Actions was configured to execute automated tests whenever the specified repository events occurred.

Overall, the assignment demonstrated how different software quality engineering techniques can be combined to evaluate and improve software quality.