# coding: utf-8

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from photoprism_client.api.photos_api import PhotosApi


class TestPhotosApi(unittest.TestCase):
    """PhotosApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PhotosApi()

    def tearDown(self) -> None:
        pass

    def test_add_photo_label(self) -> None:
        """Test case for add_photo_label

        adds a label to a photo
        """
        pass

    def test_approve_photo(self) -> None:
        """Test case for approve_photo

        marks a photo in review as approved
        """
        pass

    def test_batch_photos_approve(self) -> None:
        """Test case for batch_photos_approve

        approves multiple photos that are currently under review
        """
        pass

    def test_batch_photos_archive(self) -> None:
        """Test case for batch_photos_archive

        moves multiple photos to the archive
        """
        pass

    def test_batch_photos_delete(self) -> None:
        """Test case for batch_photos_delete

        permanently removes multiple or all photos from the archive
        """
        pass

    def test_batch_photos_private(self) -> None:
        """Test case for batch_photos_private

        toggles private state of multiple photos
        """
        pass

    def test_batch_photos_restore(self) -> None:
        """Test case for batch_photos_restore

        restores multiple photos from the archive
        """
        pass

    def test_dislike_photo(self) -> None:
        """Test case for dislike_photo

        removes the favorite flags from a photo
        """
        pass

    def test_get_photo(self) -> None:
        """Test case for get_photo

        returns picture details as JSON
        """
        pass

    def test_get_photo_yaml(self) -> None:
        """Test case for get_photo_yaml

        returns picture details as YAML
        """
        pass

    def test_like_photo(self) -> None:
        """Test case for like_photo

        flags a photo as favorite
        """
        pass

    def test_photo_primary(self) -> None:
        """Test case for photo_primary

        sets the primary file for a photo
        """
        pass

    def test_photo_unstack(self) -> None:
        """Test case for photo_unstack

        removes a file from an existing photo stack
        """
        pass

    def test_remove_photo_label(self) -> None:
        """Test case for remove_photo_label

        removes a label from a photo
        """
        pass

    def test_search_geo(self) -> None:
        """Test case for search_geo

        finds photos and returns results as JSON, so they can be displayed on a map or in a viewer
        """
        pass

    def test_search_photos(self) -> None:
        """Test case for search_photos

        finds pictures and returns them as JSON
        """
        pass

    def test_update_photo(self) -> None:
        """Test case for update_photo

        updates picture details and returns them as JSON
        """
        pass

    def test_update_photo_label(self) -> None:
        """Test case for update_photo_label

        changes a photo label
        """
        pass


if __name__ == '__main__':
    unittest.main()
