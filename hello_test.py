from unittest.mock import patch
import hello

@patch('builtins.print')
def test_hello(mock_print):
    hello.hello()
    mock_print.assert_called_with('Hello World')