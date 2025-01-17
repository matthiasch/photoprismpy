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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class EntityFace(BaseModel):
    """
    EntityFace
    """ # noqa: E501
    collision_radius: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CollisionRadius")
    collisions: Optional[StrictInt] = Field(default=None, alias="Collisions")
    created_at: Optional[StrictStr] = Field(default=None, alias="CreatedAt")
    hidden: Optional[StrictBool] = Field(default=None, alias="Hidden")
    id: Optional[StrictStr] = Field(default=None, alias="ID")
    kind: Optional[StrictInt] = Field(default=None, alias="Kind")
    matched_at: Optional[StrictStr] = Field(default=None, alias="MatchedAt")
    sample_radius: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="SampleRadius")
    samples: Optional[StrictInt] = Field(default=None, alias="Samples")
    src: Optional[StrictStr] = Field(default=None, alias="Src")
    subj_uid: Optional[StrictStr] = Field(default=None, alias="SubjUID")
    updated_at: Optional[StrictStr] = Field(default=None, alias="UpdatedAt")
    __properties: ClassVar[List[str]] = ["CollisionRadius", "Collisions", "CreatedAt", "Hidden", "ID", "Kind", "MatchedAt", "SampleRadius", "Samples", "Src", "SubjUID", "UpdatedAt"]

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
        """Create an instance of EntityFace from a JSON string"""
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
        """Create an instance of EntityFace from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CollisionRadius": obj.get("CollisionRadius"),
            "Collisions": obj.get("Collisions"),
            "CreatedAt": obj.get("CreatedAt"),
            "Hidden": obj.get("Hidden"),
            "ID": obj.get("ID"),
            "Kind": obj.get("Kind"),
            "MatchedAt": obj.get("MatchedAt"),
            "SampleRadius": obj.get("SampleRadius"),
            "Samples": obj.get("Samples"),
            "Src": obj.get("Src"),
            "SubjUID": obj.get("SubjUID"),
            "UpdatedAt": obj.get("UpdatedAt")
        })
        return _obj


