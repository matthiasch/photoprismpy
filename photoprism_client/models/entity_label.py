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

class EntityLabel(BaseModel):
    """
    EntityLabel
    """ # noqa: E501
    created_at: Optional[StrictStr] = Field(default=None, alias="CreatedAt")
    custom_slug: Optional[StrictStr] = Field(default=None, alias="CustomSlug")
    deleted_at: Optional[StrictStr] = Field(default=None, alias="DeletedAt")
    description: Optional[StrictStr] = Field(default=None, alias="Description")
    favorite: Optional[StrictBool] = Field(default=None, alias="Favorite")
    id: Optional[StrictInt] = Field(default=None, alias="ID")
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    notes: Optional[StrictStr] = Field(default=None, alias="Notes")
    photo_count: Optional[StrictInt] = Field(default=None, alias="PhotoCount")
    priority: Optional[StrictInt] = Field(default=None, alias="Priority")
    published_at: Optional[StrictStr] = Field(default=None, alias="PublishedAt")
    slug: Optional[StrictStr] = Field(default=None, alias="Slug")
    thumb: Optional[StrictStr] = Field(default=None, alias="Thumb")
    thumb_src: Optional[StrictStr] = Field(default=None, alias="ThumbSrc")
    uid: Optional[StrictStr] = Field(default=None, alias="UID")
    updated_at: Optional[StrictStr] = Field(default=None, alias="UpdatedAt")
    __properties: ClassVar[List[str]] = ["CreatedAt", "CustomSlug", "DeletedAt", "Description", "Favorite", "ID", "Name", "Notes", "PhotoCount", "Priority", "PublishedAt", "Slug", "Thumb", "ThumbSrc", "UID", "UpdatedAt"]

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
        """Create an instance of EntityLabel from a JSON string"""
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
        """Create an instance of EntityLabel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CreatedAt": obj.get("CreatedAt"),
            "CustomSlug": obj.get("CustomSlug"),
            "DeletedAt": obj.get("DeletedAt"),
            "Description": obj.get("Description"),
            "Favorite": obj.get("Favorite"),
            "ID": obj.get("ID"),
            "Name": obj.get("Name"),
            "Notes": obj.get("Notes"),
            "PhotoCount": obj.get("PhotoCount"),
            "Priority": obj.get("Priority"),
            "PublishedAt": obj.get("PublishedAt"),
            "Slug": obj.get("Slug"),
            "Thumb": obj.get("Thumb"),
            "ThumbSrc": obj.get("ThumbSrc"),
            "UID": obj.get("UID"),
            "UpdatedAt": obj.get("UpdatedAt")
        })
        return _obj


