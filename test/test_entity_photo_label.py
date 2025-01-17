# coding: utf-8

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from photoprism_client.models.entity_photo_label import EntityPhotoLabel

class TestEntityPhotoLabel(unittest.TestCase):
    """EntityPhotoLabel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntityPhotoLabel:
        """Test EntityPhotoLabel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntityPhotoLabel`
        """
        model = EntityPhotoLabel()
        if include_optional:
            return EntityPhotoLabel(
                label = photoprism_client.models.entity/label.entity.Label(
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
                    updated_at = '', ),
                label_id = 56,
                label_src = '',
                photo = photoprism_client.models.entity/photo.entity.Photo(
                    albums = [
                        photoprism_client.models.entity/album.entity.Album(
                            caption = '',
                            category = '',
                            country = '',
                            created_at = '',
                            created_by = '',
                            day = 56,
                            deleted_at = '',
                            description = '',
                            favorite = True,
                            filter = '',
                            id = 56,
                            location = '',
                            month = 56,
                            notes = '',
                            order = '',
                            parent_uid = '',
                            path = '',
                            private = True,
                            published_at = '',
                            slug = '',
                            state = '',
                            template = '',
                            thumb = '',
                            thumb_src = '',
                            title = '',
                            type = '',
                            uid = '',
                            updated_at = '',
                            year = 56, )
                        ],
                    altitude = 56,
                    camera = photoprism_client.models.entity/camera.entity.Camera(
                        description = '',
                        id = 56,
                        make = '',
                        model = '',
                        name = '',
                        notes = '',
                        slug = '',
                        type = '', ),
                    camera_id = 56,
                    camera_serial = '',
                    camera_src = '',
                    cell = photoprism_client.models.entity/cell.entity.Cell(
                        category = '',
                        created_at = '',
                        id = '',
                        name = '',
                        place = photoprism_client.models.entity/place.entity.Place(
                            city = '',
                            country = '',
                            created_at = '',
                            district = '',
                            favorite = True,
                            keywords = '',
                            label = '',
                            photo_count = 56,
                            place_id = '',
                            state = '',
                            updated_at = '', ),
                        postcode = '',
                        street = '',
                        updated_at = '', ),
                    cell_accuracy = 56,
                    cell_id = '',
                    color = 56,
                    country = '',
                    created_by = '',
                    day = 56,
                    description = '',
                    description_src = '',
                    details = photoprism_client.models.entity/details.entity.Details(
                        artist = '',
                        artist_src = '',
                        copyright = '',
                        copyright_src = '',
                        keywords = '',
                        keywords_src = '',
                        license = '',
                        license_src = '',
                        notes = '',
                        notes_src = '',
                        software = '',
                        software_src = '',
                        subject = '',
                        subject_src = '',
                        created_at = '',
                        photo_id = 56,
                        updated_at = '', ),
                    document_id = '',
                    duration = -9223372036854775808,
                    estimated_at = '',
                    exposure = '',
                    f_number = 1.337,
                    faces = 56,
                    favorite = True,
                    focal_length = 56,
                    iso = 56,
                    lat = 1.337,
                    lens = photoprism_client.models.entity/lens.entity.Lens(
                        description = '',
                        id = 56,
                        make = '',
                        model = '',
                        name = '',
                        notes = '',
                        slug = '',
                        type = '', ),
                    lens_id = 56,
                    lng = 1.337,
                    month = 56,
                    name = '',
                    original_name = '',
                    panorama = True,
                    path = '',
                    place = photoprism_client.models.entity/place.entity.Place(
                        city = '',
                        country = '',
                        created_at = '',
                        district = '',
                        favorite = True,
                        keywords = '',
                        label = '',
                        photo_count = 56,
                        place_id = '',
                        state = '',
                        updated_at = '', ),
                    place_id = '',
                    place_src = '',
                    private = True,
                    published_at = '',
                    quality = 56,
                    resolution = 56,
                    scan = True,
                    stack = 56,
                    taken_at = '',
                    taken_at_local = '',
                    taken_src = '',
                    time_zone = '',
                    title = '',
                    title_src = '',
                    type = '',
                    type_src = '',
                    uid = '',
                    year = 56,
                    checked_at = '',
                    created_at = '',
                    deleted_at = '',
                    edited_at = '',
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
                    id = 56,
                    labels = [
                        photoprism_client.models.entity/photo_label.entity.PhotoLabel(
                            label = photoprism_client.models.entity/label.entity.Label(
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
                                updated_at = '', ),
                            label_id = 56,
                            label_src = '',
                            photo_id = 56,
                            uncertainty = 56, )
                        ],
                    updated_at = '', ),
                photo_id = 56,
                uncertainty = 56
            )
        else:
            return EntityPhotoLabel(
        )
        """

    def testEntityPhotoLabel(self):
        """Test EntityPhotoLabel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
