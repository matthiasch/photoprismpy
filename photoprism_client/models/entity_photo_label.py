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
from photoprism_client.models.entity_label import EntityLabel
from typing import Optional, Set
from typing_extensions import Self

class EntityPhotoLabel(BaseModel):
    """
    EntityPhotoLabel
    """ # noqa: E501
    label: Optional[EntityLabel] = None
    label_id: Optional[StrictInt] = Field(default=None, alias="labelID")
    label_src: Optional[StrictStr] = Field(default=None, alias="labelSrc")
    photo: Optional[EntityPhoto] = None
    photo_id: Optional[StrictInt] = Field(default=None, alias="photoID")
    uncertainty: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["label", "labelID", "labelSrc", "photo", "photoID", "uncertainty"]

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
        """Create an instance of EntityPhotoLabel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of label
        if self.label:
            _dict['label'] = self.label.to_dict()
        # override the default output from pydantic by calling `to_dict()` of photo
        if self.photo:
            _dict['photo'] = self.photo.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EntityPhotoLabel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "label": EntityLabel.from_dict(obj["label"]) if obj.get("label") is not None else None,
            "labelID": obj.get("labelID"),
            "labelSrc": obj.get("labelSrc"),
            "photo": EntityPhoto.from_dict(obj["photo"]) if obj.get("photo") is not None else None,
            "photoID": obj.get("photoID"),
            "uncertainty": obj.get("uncertainty")
        })
        return _obj

from photoprism_client.models.entity_photo import EntityPhoto
# TODO: Rewrite to not use raise_errors
EntityPhotoLabel.model_rebuild(raise_errors=False)

