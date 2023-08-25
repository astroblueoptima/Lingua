
def test_handle_ask():
    response = handle_ask("What is Python?", {})
    assert "Python is a programming language" in response
