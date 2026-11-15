
from hypothesis import given, strategies as st
from library_fines import parse_member_id, total_fine, shelf_code


@given(st.one_of(st.text(), st.none()))
def test_parse_member_id_no_unexpected_crash(s):
    try:
        parse_member_id(s)
    except ValueError:
        pass


@given(st.one_of(st.text(), st.none()))
def test_total_fine_no_unexpected_crash(s):
    try:
        total_fine(s)
    except ValueError:
        pass


@given(st.one_of(st.text(), st.none()))
def test_shelf_code_no_unexpected_crash(s):
    try:
        shelf_code(s)
    except ValueError:
        pass
