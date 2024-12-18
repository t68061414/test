"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from petstore.types import BaseModel
from petstore.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class GetUserByNameRequestTypedDict(TypedDict):
    username: str
    r"""The name that needs to be fetched. Use user1 for testing."""


class GetUserByNameRequest(BaseModel):
    username: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The name that needs to be fetched. Use user1 for testing."""
