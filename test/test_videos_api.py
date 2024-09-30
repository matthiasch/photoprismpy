# coding: utf-8

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from photoprism_client.api.videos_api import VideosApi


class TestVideosApi(unittest.TestCase):
    """VideosApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VideosApi()

    def tearDown(self) -> None:
        pass

    def test_get_video(self) -> None:
        """Test case for get_video

        returns a video, optionally limited to a byte range for streaming
        """
        pass


if __name__ == '__main__':
    unittest.main()