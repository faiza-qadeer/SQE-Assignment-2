
# Part A - Black-Box Test Design

## 1. Equivalence Class Partitioning (ECP)

Equivalence Class Partitioning divides input values into groups that are expected to behave similarly.

| Input | Valid classes | Invalid classes |
|---|---|---|
| Current credits | 0 to 18 | Below 0, above 18 |
| Course credits | 1 to 4 | Below 1, above 4 |
| Outstanding dues | Zero | Negative dues |
| Registration dues condition | Zero dues | Positive dues |
| Prerequisites | All completed, none required | One or more missing |
| Course capacity | Seats available, course full | Invalid capacity or enrollment |

## 2. Boundary Value Analysis (BVA)

Boundary Value Analysis tests values around important limits.

| Condition | Test values | Expected behavior |
|---|---|---|
| Credit total | 17, 18, 19 | 17 and 18 allowed; 19 rejected |
| Course credits | 0, 1, 4, 5 | 1 to 4 valid |
| Outstanding dues | -1, 0, 1 | Invalid, allowed, blocked |
| Course capacity | 29, 30 | 29 registered; 30 waitlisted (capacity 30) |

## 3. Decision Table Testing

| Dues | Already registered | Prerequisites | Credit limit | Seat available | Expected result |
|---|---|---|---|---|---|
| Positive | Any | Any | Any | Any | DUES_BLOCK |
| Zero | Yes | Any | Any | Any | ALREADY_REGISTERED |
| Zero | No | No | Any | Any | PREREQUISITES_MISSING |
| Zero | No | Yes | No | Any | CREDIT_LIMIT |
| Zero | No | Yes | Yes | Yes | REGISTERED |
| Zero | No | Yes | Yes | No | WAITLISTED |

Negative dues are invalid and raise a ValueError.

The conditions are evaluated in the priority order defined in the requirements.