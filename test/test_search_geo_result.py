# coding: utf-8

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from photoprism_client.models.search_geo_result import SearchGeoResult

class TestSearchGeoResult(unittest.TestCase):
    """SearchGeoResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchGeoResult:
        """Test SearchGeoResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchGeoResult`
        """
        model = SearchGeoResult()
        if include_optional:
            return SearchGeoResult(
                description = '',
                favorite = True,
                hash = '',
                height = 56,
                lat = 1.337,
                lng = 1.337,
                taken_at = '',
                taken_at_local = '',
                title = '',
                type = '',
                uid = '',
                width = 56
            )
        else:
            return SearchGeoResult(
        )
        """

    def testSearchGeoResult(self):
        """Test SearchGeoResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
