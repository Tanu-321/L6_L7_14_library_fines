import pytest
from library_fines import late_fine, can_borrow, renewal_status


# -------------------------------
# TESTS FOR late_fine()
# -------------------------------

def test_unknown_member():
    with pytest.raises(ValueError, match="unknown member"):
        late_fine("visitor", 20, False)


def test_negative_days():
    with pytest.raises(ValueError, match="invalid days"):
        late_fine("student", -5, False)


def test_student_late_return():
    assert late_fine("student", 15, False) == 2


def test_faculty_late_return():
    assert late_fine("faculty", 31, False) == 1


def test_guest_late_return():
    assert late_fine("guest", 15, False) == 5


def test_returned_on_time():
    assert late_fine("student", 10, False) == 0


def test_fine_exceeds_maximum():
    assert late_fine("student", 200, False) == 200


def test_damaged_book():
    assert late_fine("student", 10, True) == 150


def test_late_and_damaged_book():
    assert late_fine("student", 15, True) == 152


# -------------------------------
# TESTS FOR can_borrow()
# -------------------------------

def test_pending_fine_above_100():
    assert can_borrow(1, 101, "student") is False


def test_faculty_can_borrow():
    assert can_borrow(9, 0, "faculty") is True


def test_faculty_cannot_borrow():
    assert can_borrow(10, 0, "faculty") is False


def test_student_can_borrow():
    assert can_borrow(2, 0, "student") is True


def test_student_cannot_borrow():
    assert can_borrow(3, 0, "student") is False


# -------------------------------
# TESTS FOR renewal_status()
# -------------------------------

def test_reservation_denies_renewal():
    assert renewal_status(0, True, 5) == "denied"


def test_renewal_limit_reached():
    assert renewal_status(2, False, 5) == "limit reached"


def test_overdue_book():
    assert renewal_status(1, False, -1) == "overdue"


def test_successful_renewal():
    assert renewal_status(1, False, 5) == "renewed"