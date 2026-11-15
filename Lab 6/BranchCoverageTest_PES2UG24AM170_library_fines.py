
import pytest
from library_fines import late_fine, can_borrow, renewal_status


# --------------------------------
# BRANCH TESTS FOR late_fine()
# --------------------------------

def test_unknown_member_branch():
    with pytest.raises(ValueError, match="unknown member"):
        late_fine("visitor", 10, False)


def test_valid_member_branch():
    assert late_fine("student", 10, False) == 0


def test_negative_days_branch():
    with pytest.raises(ValueError, match="invalid days"):
        late_fine("student", -1, False)


def test_valid_days_branch():
    assert late_fine("student", 15, False) == 2


def test_faculty_loan_period_branch():
    assert late_fine("faculty", 31, False) == 1


def test_non_faculty_loan_period_branch():
    assert late_fine("guest", 15, False) == 5


def test_overdue_branch():
    assert late_fine("student", 15, False) == 2


def test_not_overdue_branch():
    assert late_fine("student", 10, False) == 0


def test_fine_exceeds_200_branch():
    assert late_fine("student", 200, False) == 200


def test_fine_does_not_exceed_200_branch():
    assert late_fine("student", 15, False) == 2


def test_damaged_book_branch():
    assert late_fine("student", 10, True) == 150


def test_not_damaged_book_branch():
    assert late_fine("student", 10, False) == 0


# --------------------------------
# BRANCH TESTS FOR can_borrow()
# --------------------------------

def test_pending_fine_above_100_branch():
    assert can_borrow(1, 101, "student") is False


def test_pending_fine_not_above_100_branch():
    assert can_borrow(1, 100, "student") is True


def test_faculty_borrow_branch():
    assert can_borrow(9, 0, "faculty") is True


def test_non_faculty_borrow_branch():
    assert can_borrow(2, 0, "student") is True


def test_faculty_book_limit_branch():
    assert can_borrow(10, 0, "faculty") is False


def test_student_book_limit_branch():
    assert can_borrow(3, 0, "student") is False


# --------------------------------
# BRANCH TESTS FOR renewal_status()
# --------------------------------

def test_reservation_branch():
    assert renewal_status(0, True, 5) == "denied"


def test_no_reservation_branch():
    assert renewal_status(1, False, 5) == "renewed"


def test_renewal_limit_branch():
    assert renewal_status(2, False, 5) == "limit reached"


def test_renewal_limit_not_reached_branch():
    assert renewal_status(1, False, 5) == "renewed"


def test_overdue_renewal_branch():
    assert renewal_status(1, False, -1) == "overdue"


def test_not_overdue_renewal_branch():
    assert renewal_status(1, False, 5) == "renewed"
