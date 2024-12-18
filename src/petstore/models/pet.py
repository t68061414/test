"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .category import Category, CategoryTypedDict
from .tag import Tag, TagTypedDict
from enum import Enum
from petstore.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class Status(str, Enum):
    r"""pet status in the store"""

    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"


class PetTypedDict(TypedDict):
    name: str
    photo_urls: List[str]
    id: NotRequired[int]
    category: NotRequired[CategoryTypedDict]
    tags: NotRequired[List[TagTypedDict]]
    status: NotRequired[Status]
    r"""pet status in the store"""


class Pet(BaseModel):
    name: str

    photo_urls: Annotated[List[str], pydantic.Field(alias="photoUrls")]

    id: Optional[int] = None

    category: Optional[Category] = None

    tags: Optional[List[Tag]] = None

    status: Optional[Status] = None
    r"""pet status in the store"""
