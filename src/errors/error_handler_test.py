from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableError
from .error_handler import handle_errors


def test_handle_errors_generic():
    mock_exception = Exception("error")

    result = handle_errors(mock_exception)

    assert isinstance(result, HttpResponse)

    assert hasattr(result, "status_code")
    assert hasattr(result, "body")

    assert "errors" in result.body
    assert "title" in result.body["errors"][0]
    assert "detail" in result.body["errors"][0]

    assert result.status_code == 500
    assert result.body["errors"][0]["title"] == "Server Error"
    assert result.body["errors"][0]["detail"] == str(mock_exception)


def test_handle_errors_http_unprocessable_error():
    mock_exception = HttpUnprocessableError("error")

    result = handle_errors(mock_exception)

    assert isinstance(result, HttpResponse)

    assert hasattr(result, "status_code")
    assert hasattr(result, "body")

    assert "errors" in result.body
    assert "title" in result.body["errors"][0]
    assert "detail" in result.body["errors"][0]

    assert result.status_code == mock_exception.status_code
    assert result.body["errors"][0]["title"] == mock_exception.name
    assert result.body["errors"][0]["detail"] == mock_exception.message
