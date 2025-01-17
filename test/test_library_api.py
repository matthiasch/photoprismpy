# coding: utf-8

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from photoprism_client.api.library_api import LibraryApi


class TestLibraryApi(unittest.TestCase):
    """LibraryApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LibraryApi()

    def tearDown(self) -> None:
        pass

    def test_api_v1_import_path_post(self) -> None:
        """Test case for api_v1_import_path_post

        """
        pass

    def test_api_v1_index_post(self) -> None:
        """Test case for api_v1_index_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
