# coding: utf-8

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from photoprism_client.api.images_api import ImagesApi


class TestImagesApi(unittest.TestCase):
    """ImagesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ImagesApi()

    def tearDown(self) -> None:
        pass

    def test_album_cover(self) -> None:
        """Test case for album_cover

        returns an album cover image
        """
        pass

    def test_download_album(self) -> None:
        """Test case for download_album

        streams the album contents as zip archiv
        """
        pass

    def test_folder_cover(self) -> None:
        """Test case for folder_cover

        returns a folder cover image
        """
        pass

    def test_get_download(self) -> None:
        """Test case for get_download

        returns the raw file data
        """
        pass

    def test_get_photo_download(self) -> None:
        """Test case for get_photo_download

        returns the primary file matching that belongs to the photo
        """
        pass

    def test_get_thumb(self) -> None:
        """Test case for get_thumb

        returns a thumbnail image with the requested size
        """
        pass

    def test_label_cover(self) -> None:
        """Test case for label_cover

        returns a label cover image
        """
        pass


if __name__ == '__main__':
    unittest.main()