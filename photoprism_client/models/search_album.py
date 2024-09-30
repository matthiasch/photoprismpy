# coding: utf-8

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SearchAlbum(BaseModel):
    """
    SearchAlbum
    """ # noqa: E501
    caption: Optional[StrictStr] = Field(default=None, alias="Caption")
    category: Optional[StrictStr] = Field(default=None, alias="Category")
    country: Optional[StrictStr] = Field(default=None, alias="Country")
    created_at: Optional[StrictStr] = Field(default=None, alias="CreatedAt")
    day: Optional[StrictInt] = Field(default=None, alias="Day")
    deleted_at: Optional[StrictStr] = Field(default=None, alias="DeletedAt")
    description: Optional[StrictStr] = Field(default=None, alias="Description")
    favorite: Optional[StrictBool] = Field(default=None, alias="Favorite")
    filter: Optional[StrictStr] = Field(default=None, alias="Filter")
    link_count: Optional[StrictInt] = Field(default=None, alias="LinkCount")
    location: Optional[StrictStr] = Field(default=None, alias="Location")
    month: Optional[StrictInt] = Field(default=None, alias="Month")
    notes: Optional[StrictStr] = Field(default=None, alias="Notes")
    order: Optional[StrictStr] = Field(default=None, alias="Order")
    parent_uid: Optional[StrictStr] = Field(default=None, alias="ParentUID")
    path: Optional[StrictStr] = Field(default=None, alias="Path")
    photo_count: Optional[StrictInt] = Field(default=None, alias="PhotoCount")
    private: Optional[StrictBool] = Field(default=None, alias="Private")
    slug: Optional[StrictStr] = Field(default=None, alias="Slug")
    state: Optional[StrictStr] = Field(default=None, alias="State")
    template: Optional[StrictStr] = Field(default=None, alias="Template")
    thumb: Optional[StrictStr] = Field(default=None, alias="Thumb")
    thumb_src: Optional[StrictStr] = Field(default=None, alias="ThumbSrc")
    title: Optional[StrictStr] = Field(default=None, alias="Title")
    type: Optional[StrictStr] = Field(default=None, alias="Type")
    uid: Optional[StrictStr] = Field(default=None, alias="UID")
    updated_at: Optional[StrictStr] = Field(default=None, alias="UpdatedAt")
    year: Optional[StrictInt] = Field(default=None, alias="Year")
    __properties: ClassVar[List[str]] = ["Caption", "Category", "Country", "CreatedAt", "Day", "DeletedAt", "Description", "Favorite", "Filter", "LinkCount", "Location", "Month", "Notes", "Order", "ParentUID", "Path", "PhotoCount", "Private", "Slug", "State", "Template", "Thumb", "ThumbSrc", "Title", "Type", "UID", "UpdatedAt", "Year"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SearchAlbum from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchAlbum from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Caption": obj.get("Caption"),
            "Category": obj.get("Category"),
            "Country": obj.get("Country"),
            "CreatedAt": obj.get("CreatedAt"),
            "Day": obj.get("Day"),
            "DeletedAt": obj.get("DeletedAt"),
            "Description": obj.get("Description"),
            "Favorite": obj.get("Favorite"),
            "Filter": obj.get("Filter"),
            "LinkCount": obj.get("LinkCount"),
            "Location": obj.get("Location"),
            "Month": obj.get("Month"),
            "Notes": obj.get("Notes"),
            "Order": obj.get("Order"),
            "ParentUID": obj.get("ParentUID"),
            "Path": obj.get("Path"),
            "PhotoCount": obj.get("PhotoCount"),
            "Private": obj.get("Private"),
            "Slug": obj.get("Slug"),
            "State": obj.get("State"),
            "Template": obj.get("Template"),
            "Thumb": obj.get("Thumb"),
            "ThumbSrc": obj.get("ThumbSrc"),
            "Title": obj.get("Title"),
            "Type": obj.get("Type"),
            "UID": obj.get("UID"),
            "UpdatedAt": obj.get("UpdatedAt"),
            "Year": obj.get("Year")
        })
        return _obj

