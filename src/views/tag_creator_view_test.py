from unittest.mock import patch
from src.views.http_types.http_response import HttpResponse
from src.views.http_types.http_request import HttpRequest
from src.controllers.tag_creator_controller import TagCreatorController
from .tag_creator_view import TagCreatorView


@patch.object(TagCreatorController, 'create')
def test_validate_and_create(tag_create):
    req = HttpRequest(body={"product_code": "123456"})

    tag_create.return_value = req

    tag_creator_view = TagCreatorView()

    result = tag_creator_view.validate_and_create(req)

    assert isinstance(result, HttpResponse)

    assert result.status_code == 200
