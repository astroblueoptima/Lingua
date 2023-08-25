
def test_handle_debug():
    result = handle_debug("for i in range(3) print(i)")
    assert "Missing colon in 'for' loop" in result
