from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.query_request import QueryRequest
from typing import Dict
from typing import cast
from ...models.http_validation_error import HTTPValidationError
from ...models.query_response import QueryResponse



def _get_kwargs(
    *,
    body: QueryRequest,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}


    

    

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/query",
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, QueryResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QueryResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, QueryResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: QueryRequest,

) -> Response[Union[HTTPValidationError, QueryResponse]]:
    """ Query Main

    Args:
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, QueryResponse]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: QueryRequest,

) -> Optional[Union[HTTPValidationError, QueryResponse]]:
    """ Query Main

    Args:
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, QueryResponse]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: QueryRequest,

) -> Response[Union[HTTPValidationError, QueryResponse]]:
    """ Query Main

    Args:
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, QueryResponse]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: QueryRequest,

) -> Optional[Union[HTTPValidationError, QueryResponse]]:
    """ Query Main

    Args:
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, QueryResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
