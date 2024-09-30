# coding: utf-8

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from photoprism_client.models.entity_label import EntityLabel

class TestEntityLabel(unittest.TestCase):
    """EntityLabel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntityLabel:
        """Test EntityLabel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntityLabel`
        """
        model = EntityLabel()
        if include_optional:
            return EntityLabel(
                created_at = '',
                custom_slug = '',
                deleted_at = '',
                description = '',
                favorite = True,
                id = 56,
                name = '',
                notes = '',
                photo_count = 56,
                priority = 56,
                published_at = '',
                slug = '',
                thumb = '',
                thumb_src = '',
                uid = '',
                updated_at = ''
            )
        else:
            return EntityLabel(
        )
        """

    def testEntityLabel(self):
        """Test EntityLabel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
