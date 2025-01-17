# coding: utf-8

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from photoprism_client.models.search_photo import SearchPhoto

class TestSearchPhoto(unittest.TestCase):
    """SearchPhoto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchPhoto:
        """Test SearchPhoto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchPhoto`
        """
        model = SearchPhoto()
        if include_optional:
            return SearchPhoto(
                altitude = 56,
                camera_id = 56,
                camera_make = '',
                camera_model = '',
                camera_serial = '',
                camera_src = '',
                cell_accuracy = 56,
                cell_id = '',
                checked_at = '',
                color = 56,
                country = '',
                created_at = '',
                day = 56,
                deleted_at = '',
                description = '',
                document_id = '',
                duration = -9223372036854775808,
                edited_at = '',
                exposure = '',
                f_number = 1.337,
                faces = 56,
                favorite = True,
                file_name = '',
                file_root = '',
                file_uid = '',
                files = [
                    photoprism_client.models.entity/file.entity.File(
                        aspect_ratio = 1.337,
                        chroma = 56,
                        codec = '',
                        color_profile = '',
                        colors = '',
                        created_at = '',
                        created_in = 56,
                        deleted_at = '',
                        diff = 56,
                        duration = -9223372036854775808,
                        error = '',
                        fps = 1.337,
                        file_type = '',
                        frames = 56,
                        hdr = True,
                        hash = '',
                        height = 56,
                        instance_id = '',
                        luminance = '',
                        main_color = '',
                        media_id = '',
                        media_type = '',
                        media_utc = 56,
                        mime = '',
                        missing = True,
                        mod_time = 56,
                        name = '',
                        orientation = 56,
                        orientation_src = '',
                        original_name = '',
                        photo_uid = '',
                        portrait = True,
                        primary = True,
                        projection = '',
                        published_at = '',
                        root = '',
                        sidecar = True,
                        size = 56,
                        software = '',
                        taken_at = '',
                        time_index = '',
                        uid = '',
                        updated_at = '',
                        updated_in = 56,
                        video = True,
                        watermark = True,
                        width = 56, )
                    ],
                focal_length = 56,
                hash = '',
                height = 56,
                id = '',
                instance_id = '',
                iso = 56,
                lat = 1.337,
                lens_id = 56,
                lens_make = '',
                lens_model = '',
                lng = 1.337,
                merged = True,
                month = 56,
                name = '',
                original_name = '',
                panorama = True,
                path = '',
                place_city = '',
                place_country = '',
                place_id = '',
                place_label = '',
                place_src = '',
                place_state = '',
                portrait = True,
                private = True,
                quality = 56,
                resolution = 56,
                scan = True,
                stack = 56,
                taken_at = '',
                taken_at_local = '',
                taken_src = '',
                time_zone = '',
                title = '',
                type = '',
                type_src = '',
                uid = '',
                updated_at = '',
                width = 56,
                year = 56
            )
        else:
            return SearchPhoto(
        )
        """

    def testSearchPhoto(self):
        """Test SearchPhoto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
