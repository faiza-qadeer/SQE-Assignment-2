
import pytest

from registration import (
    Student,
    Course,
    check_credit_limit,
    prerequisites_satisfied,
    registration_decision,
    register_course,
    withdraw_course
)


def test_credit_limit_valid():
    assert check_credit_limit(5, 3) == True


def test_credit_limit_exceeded():
    assert check_credit_limit(15, 4) == False


def test_invalid_current_credits():
    with pytest.raises(ValueError):
        check_credit_limit(19, 2)


def test_empty_prerequisites():
    assert prerequisites_satisfied(set(), set()) == True


def test_prerequisite_matched():
    assert prerequisites_satisfied({"CS101"}, {"CS101", "CS102"}) == True


def test_prerequisite_not_matched():
    assert prerequisites_satisfied({"CS101"}, {"CS102"}) == False


def test_registration_dues_branch():
    student = Student("S01", outstanding_dues=1500)
    course = Course("CS201", 3, 30)

    assert registration_decision(student, course) == "DUES_BLOCK"


def test_registration_already_registered_branch():
    student = Student("S01", registered_courses={"CS201"})
    course = Course("CS201", 3, 30)

    assert registration_decision(student, course) == "ALREADY_REGISTERED"


def test_registration_prerequisite_branch():
    student = Student("S01")
    course = Course("CS201", 3, 30, prerequisites={"CS101"})

    assert registration_decision(student, course) == "PREREQUISITES_MISSING"


def test_registration_credit_limit_branch():
    student = Student("S01", current_credits=16)
    course = Course("CS201", 3, 30)

    assert registration_decision(student, course) == "CREDIT_LIMIT"


def test_registration_success_branch():
    student = Student("S01")
    course = Course("CS201", 3, 30)

    assert registration_decision(student, course) == "REGISTERED"


def test_register_course_updates_student():
    student = Student("S01")
    course = Course("CS201", 3, 30)

    register_course(student, course)

    assert "CS201" in student.registered_courses
    assert student.current_credits == 3
    assert course.enrolled == 1


def test_withdraw_course_not_registered():
    student = Student("S01")
    course = Course("CS201", 3, 30)

    assert withdraw_course(student, course) == False


def test_withdraw_course_registered():
    student = Student("S01", current_credits=3, registered_courses={"CS201"})
    course = Course("CS201", 3, 30, enrolled=1)

    assert withdraw_course(student, course) == True
    assert "CS201" not in student.registered_courses
    assert student.current_credits == 0
