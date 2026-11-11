# Part A - Black-Box Testing Results

## 1. Test Execution

The black-box test cases were executed against the original Student Course Registration System using pytest.

| Result | Count |
|---|---:|
| Total test cases | 44 |
| Passed | 35 |
| Failed | 9 |

The tests were performed using the original implementation without modifying the source code.

## 2. Failed Test Cases

| Test Case | Requirement | Actual Problem |
|---|---|---|
| `test_credit_limit_exactly_18` | FR-01 | Exactly 18 credits rejected |
| `test_one_prerequisite_missing` | FR-03 | Missing prerequisite accepted |
| `test_positive_dues` | FR-04 | Positive dues did not block registration |
| `test_course_is_full` | FR-08 | Full course returned REGISTERED |
| `test_withdraw_registered_course` | FR-13 | Enrollment was not decreased |
| `test_missing_prerequisites` | FR-03 | Missing prerequisite accepted |
| `test_dues_have_priority` | FR-09 | Dues condition did not take priority |
| `test_waitlist_does_not_add_duplicate` | FR-08 | Full course returned REGISTERED |
| `test_mcdc_prerequisites_missing` | FR-03 | Partial prerequisite completion was accepted |

## 3. Main Defects Identified

Five main defect areas were identified:

1. **Incorrect credit limit boundary:** Exactly 18 credits are rejected.
2. **Incorrect prerequisite checking:** The program accepts a student who has completed only one of multiple required prerequisites.
3. **Incorrect outstanding dues condition:** Small positive dues do not block registration.
4. **Incorrect course capacity checking:** The WAITLISTED condition is unreachable because of conflicting validation logic.
5. **Missing enrollment decrement during withdrawal:** The course enrollment count is not decreased.

Some failed test cases expose the same underlying defect.

## 4. Conclusion

Black-box testing identified several incorrect behaviors in the original Student Course Registration System. A total of 44 test cases were executed, with 35 passing and 9 failing.

The failed tests provide evidence of defects in the supplied implementation. These results are retained as the baseline for evaluating the system against its requirements.