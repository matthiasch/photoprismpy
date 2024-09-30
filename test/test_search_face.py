# coding: utf-8

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from photoprism_client.models.search_face import SearchFace

class TestSearchFace(unittest.TestCase):
    """SearchFace unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchFace:
        """Test SearchFace
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchFace`
        """
        model = SearchFace()
        if include_optional:
            return SearchFace(
                collision_radius = 1.337,
                collisions = 56,
                created_at = '',
                face_dist = 1.337,
                file_uid = '',
                hidden = True,
                id = '',
                invalid = True,
                marker_uid = '',
                matched_at = '',
                name = '',
                review = True,
                sample_radius = 1.337,
                samples = 56,
                score = 56,
                size = 56,
                src = '',
                subj_src = '',
                subj_uid = '',
                thumb = '',
                updated_at = ''
            )
        else:
            return SearchFace(
        )
        """

    def testSearchFace(self):
        """Test SearchFace"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()