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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class EntityDetails(BaseModel):
    """
    EntityDetails
    """ # noqa: E501
    artist: Optional[StrictStr] = Field(default=None, alias="Artist")
    artist_src: Optional[StrictStr] = Field(default=None, alias="ArtistSrc")
    copyright: Optional[StrictStr] = Field(default=None, alias="Copyright")
    copyright_src: Optional[StrictStr] = Field(default=None, alias="CopyrightSrc")
    keywords: Optional[StrictStr] = Field(default=None, alias="Keywords")
    keywords_src: Optional[StrictStr] = Field(default=None, alias="KeywordsSrc")
    license: Optional[StrictStr] = Field(default=None, alias="License")
    license_src: Optional[StrictStr] = Field(default=None, alias="LicenseSrc")
    notes: Optional[StrictStr] = Field(default=None, alias="Notes")
    notes_src: Optional[StrictStr] = Field(default=None, alias="NotesSrc")
    software: Optional[StrictStr] = Field(default=None, alias="Software")
    software_src: Optional[StrictStr] = Field(default=None, alias="SoftwareSrc")
    subject: Optional[StrictStr] = Field(default=None, alias="Subject")
    subject_src: Optional[StrictStr] = Field(default=None, alias="SubjectSrc")
    created_at: Optional[StrictStr] = Field(default=None, alias="createdAt")
    photo_id: Optional[StrictInt] = Field(default=None, alias="photoID")
    updated_at: Optional[StrictStr] = Field(default=None, alias="updatedAt")
    __properties: ClassVar[List[str]] = ["Artist", "ArtistSrc", "Copyright", "CopyrightSrc", "Keywords", "KeywordsSrc", "License", "LicenseSrc", "Notes", "NotesSrc", "Software", "SoftwareSrc", "Subject", "SubjectSrc", "createdAt", "photoID", "updatedAt"]

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
        """Create an instance of EntityDetails from a JSON string"""
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
        """Create an instance of EntityDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Artist": obj.get("Artist"),
            "ArtistSrc": obj.get("ArtistSrc"),
            "Copyright": obj.get("Copyright"),
            "CopyrightSrc": obj.get("CopyrightSrc"),
            "Keywords": obj.get("Keywords"),
            "KeywordsSrc": obj.get("KeywordsSrc"),
            "License": obj.get("License"),
            "LicenseSrc": obj.get("LicenseSrc"),
            "Notes": obj.get("Notes"),
            "NotesSrc": obj.get("NotesSrc"),
            "Software": obj.get("Software"),
            "SoftwareSrc": obj.get("SoftwareSrc"),
            "Subject": obj.get("Subject"),
            "SubjectSrc": obj.get("SubjectSrc"),
            "createdAt": obj.get("createdAt"),
            "photoID": obj.get("photoID"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


