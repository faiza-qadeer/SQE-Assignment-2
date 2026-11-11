
import pytest
from registration import check_credit_limit, prerequisites_satisfied


# FR-01: Credit limit testing

def test_credit_limit_below_18():
    assert check_credit_limit(15, 2) == True


def test_credit_limit_exactly_18():
    assert check_credit_limit(15, 3) == True


def test_credit_limit_above_18():
    assert check_credit_limit(16, 3) == False


# FR-02: Invalid credit inputs

def test_invalid_current_credits():
    with pytest.raises(ValueError, match="Invalid current credits"):
        check_credit_limit(19, 3)


def test_invalid_course_credits():
    with pytest.raises(ValueError, match="Invalid course credits"):
        check_credit_limit(10, 5)


# FR-03: Prerequisite testing

def test_all_prerequisites_completed():
    assert prerequisites_satisfied(
        {"CS101", "MATH101"},
        {"CS101", "MATH101"}
    ) == True


def test_one_prerequisite_missing():
    assert prerequisites_satisfied(
        {"CS101"},
        {"CS101", "MATH101"}
    ) == False


def test_no_prerequisites_required():
    assert prerequisites_satisfied(
        set(),
        set()
    ) == True


from registration import Student, Course
from registration import registration_decision, register_course, withdraw_course


# FR-04: Outstanding dues

def test_zero_dues():
    s = Student("S1", outstanding_dues=0)
    c = Course("CS201", 3, 30)
    assert registration_decision(s, c) == "REGISTERED"


def test_positive_dues():
    s = Student("S2", outstanding_dues=1)
    c = Course("CS201", 3, 30)
    assert registration_decision(s, c) == "DUES_BLOCK"


# FR-05: Already registered

def test_already_registered():
    s = Student("S3", registered_courses={"CS201"})
    c = Course("CS201", 3, 30)
    assert registration_decision(s, c) == "ALREADY_REGISTERED"


# FR-08: Course capacity

def test_course_has_available_seat():
    s = Student("S4")
    c = Course("CS201", 3, 30, enrolled=29)
    assert registration_decision(s, c) == "REGISTERED"


def test_course_is_full():
    s = Student("S5")
    c = Course("CS201", 3, 30, enrolled=30)
    assert registration_decision(s, c) == "WAITLISTED"


# FR-13 and FR-14: Withdrawal

def test_withdraw_registered_course():
    s = Student("S6", current_credits=3, registered_courses={"CS201"})
    c = Course("CS201", 3, 30, enrolled=10)

    assert withdraw_course(s, c) == True
    assert s.current_credits == 0
    assert c.enrolled == 9


def test_withdraw_not_registered_course():
    s = Student("S7")
    c = Course("CS201", 3, 30, enrolled=10)

    assert withdraw_course(s, c) == False
    assert c.enrolled == 10

# FR-06: Missing prerequisites

def test_missing_prerequisites():
    s = Student("S8", completed_courses={"CS101"})
    c = Course("CS201", 3, 30, prerequisites={"CS101", "MATH101"})

    assert registration_decision(s, c) == "PREREQUISITES_MISSING"


# FR-07: Credit limit exceeded

def test_registration_exceeds_credit_limit():
    s = Student("S9", current_credits=16)
    c = Course("CS201", 3, 30)

    assert registration_decision(s, c) == "CREDIT_LIMIT"


# FR-09: Priority of conditions

def test_dues_have_priority():
    s = Student(
        "S10",
        outstanding_dues=100,
        registered_courses={"CS201"}
    )
    c = Course("CS201", 3, 30)

    assert registration_decision(s, c) == "DUES_BLOCK"


# FR-10: Decision should not change objects

def test_decision_does_not_change_student_or_course():
    s = Student("S11", current_credits=6)
    c = Course("CS201", 3, 30, enrolled=10)

    registration_decision(s, c)

    assert s.current_credits == 6
    assert s.registered_courses == set()
    assert c.enrolled == 10


# FR-11: Successful registration updates records

def test_successful_registration_updates_records():
    s = Student("S12")
    c = Course("CS201", 3, 30)

    result = register_course(s, c)

    assert result == "REGISTERED"
    assert "CS201" in s.registered_courses
    assert s.current_credits == 3
    assert c.enrolled == 1


# FR-12: Waitlist should not contain duplicate student

def test_waitlist_does_not_add_duplicate():
    s = Student("S13")
    c = Course("CS201", 3, 30, enrolled=30, waitlist=["S13"])

    result = register_course(s, c)

    assert result == "WAITLISTED"
    assert c.waitlist.count("S13") == 1


# FR-15: Negative dues are invalid

def test_negative_dues_are_invalid():
    s = Student("S14", outstanding_dues=-1)
    c = Course("CS201", 3, 30)

    with pytest.raises(ValueError, match="Invalid dues"):
        registration_decision(s, c)


# FR-15: Invalid course capacity

def test_invalid_course_capacity():
    s = Student("S15")
    c = Course("CS201", 3, 0)

    with pytest.raises(ValueError, match="Invalid capacity or enrollment"):
        registration_decision(s, c)
# Additional FR-02 boundary tests

def test_current_credits_zero():
    assert check_credit_limit(0, 1) == True

def test_zero_course_credits_invalid():
    with pytest.raises(ValueError):
        check_credit_limit(18, 0)


def test_current_credits_at_18_cannot_add_course():
    assert check_credit_limit(18, 1) == False
def test_course_credits_one():
    assert check_credit_limit(10, 1) == True

def test_course_credits_four():
    assert check_credit_limit(10, 4) == True

# MC/DC paired test cases

# C1: Negative dues
def test_mcdc_negative_dues():
    s = Student("M1", outstanding_dues=-1)
    c = Course("CS301", 3, 30)
    with pytest.raises(ValueError):
        registration_decision(s, c)

def test_mcdc_zero_dues():
    s = Student("M2", outstanding_dues=0)
    c = Course("CS301", 3, 30)
    assert registration_decision(s, c) == "REGISTERED"


# C2: Invalid capacity and enrollment validation
def test_mcdc_negative_enrollment():
    s = Student("M3")
    c = Course("CS301", 3, 30, enrolled=-1)
    with pytest.raises(ValueError):
        registration_decision(s, c)

def test_mcdc_valid_enrollment():
    s = Student("M4")
    c = Course("CS301", 3, 30, enrolled=0)
    assert registration_decision(s, c) == "REGISTERED"

def test_mcdc_enrollment_above_capacity():
    s = Student("M5")
    c = Course("CS301", 3, 30, enrolled=31)
    with pytest.raises(ValueError):
        registration_decision(s, c)

def test_mcdc_enrollment_at_capacity():
    s = Student("M6")
    c = Course("CS301", 3, 30, enrolled=30)
    assert registration_decision(s, c) == "REGISTERED"

def test_mcdc_zero_capacity():
    s = Student("M7")
    c = Course("CS301", 3, 0, enrolled=0)
    with pytest.raises(ValueError):
        registration_decision(s, c)

def test_mcdc_positive_capacity():
    s = Student("M8")
    c = Course("CS301", 3, 1, enrolled=0)
    assert registration_decision(s, c) == "REGISTERED"


# C3: Outstanding dues greater than 1000
def test_mcdc_high_dues():
    s = Student("M9", outstanding_dues=1001)
    c = Course("CS301", 3, 30)
    assert registration_decision(s, c) == "DUES_BLOCK"

def test_mcdc_no_high_dues():
    s = Student("M10", outstanding_dues=0)
    c = Course("CS301", 3, 30)
    assert registration_decision(s, c) == "REGISTERED"


# C4: Already registered
def test_mcdc_already_registered():
    s = Student("M11", registered_courses={"CS301"})
    c = Course("CS301", 3, 30)
    assert registration_decision(s, c) == "ALREADY_REGISTERED"

def test_mcdc_not_already_registered():
    s = Student("M12")
    c = Course("CS301", 3, 30)
    assert registration_decision(s, c) == "REGISTERED"


# C5: Prerequisites missing
def test_mcdc_prerequisites_missing():
    s = Student("M13", completed_courses={"CS101"})
    c = Course("CS301", 3, 30,
               prerequisites={"CS101", "MATH101"})
    assert registration_decision(s, c) == "PREREQUISITES_MISSING"

def test_mcdc_prerequisites_completed():
    s = Student("M14",
                completed_courses={"CS101", "MATH101"})
    c = Course("CS301", 3, 30,
               prerequisites={"CS101", "MATH101"})
    assert registration_decision(s, c) == "REGISTERED"


# C6: Credit limit
def test_mcdc_credit_limit_exceeded():
    s = Student("M15", current_credits=15)
    c = Course("CS301", 3, 30)
    assert registration_decision(s, c) == "CREDIT_LIMIT"

def test_mcdc_credit_limit_allowed():
    s = Student("M16", current_credits=14)
    c = Course("CS301", 3, 30)
    assert registration_decision(s, c) == "REGISTERED"
