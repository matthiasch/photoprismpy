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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CustomizeFeatureSettings(BaseModel):
    """
    CustomizeFeatureSettings
    """ # noqa: E501
    account: Optional[StrictBool] = None
    albums: Optional[StrictBool] = None
    archive: Optional[StrictBool] = None
    delete: Optional[StrictBool] = None
    download: Optional[StrictBool] = None
    edit: Optional[StrictBool] = None
    estimates: Optional[StrictBool] = None
    favorites: Optional[StrictBool] = None
    files: Optional[StrictBool] = None
    folders: Optional[StrictBool] = None
    var_import: Optional[StrictBool] = Field(default=None, alias="import")
    labels: Optional[StrictBool] = None
    library: Optional[StrictBool] = None
    logs: Optional[StrictBool] = None
    moments: Optional[StrictBool] = None
    people: Optional[StrictBool] = None
    places: Optional[StrictBool] = None
    private: Optional[StrictBool] = None
    ratings: Optional[StrictBool] = None
    reactions: Optional[StrictBool] = None
    review: Optional[StrictBool] = None
    search: Optional[StrictBool] = None
    services: Optional[StrictBool] = None
    settings: Optional[StrictBool] = None
    share: Optional[StrictBool] = None
    upload: Optional[StrictBool] = None
    videos: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["account", "albums", "archive", "delete", "download", "edit", "estimates", "favorites", "files", "folders", "import", "labels", "library", "logs", "moments", "people", "places", "private", "ratings", "reactions", "review", "search", "services", "settings", "share", "upload", "videos"]

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
        """Create an instance of CustomizeFeatureSettings from a JSON string"""
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
        """Create an instance of CustomizeFeatureSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account": obj.get("account"),
            "albums": obj.get("albums"),
            "archive": obj.get("archive"),
            "delete": obj.get("delete"),
            "download": obj.get("download"),
            "edit": obj.get("edit"),
            "estimates": obj.get("estimates"),
            "favorites": obj.get("favorites"),
            "files": obj.get("files"),
            "folders": obj.get("folders"),
            "import": obj.get("import"),
            "labels": obj.get("labels"),
            "library": obj.get("library"),
            "logs": obj.get("logs"),
            "moments": obj.get("moments"),
            "people": obj.get("people"),
            "places": obj.get("places"),
            "private": obj.get("private"),
            "ratings": obj.get("ratings"),
            "reactions": obj.get("reactions"),
            "review": obj.get("review"),
            "search": obj.get("search"),
            "services": obj.get("services"),
            "settings": obj.get("settings"),
            "share": obj.get("share"),
            "upload": obj.get("upload"),
            "videos": obj.get("videos")
        })
        return _obj


