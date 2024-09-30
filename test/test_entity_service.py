# coding: utf-8

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from photoprism_client.models.entity_service import EntityService

class TestEntityService(unittest.TestCase):
    """EntityService unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntityService:
        """Test EntityService
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntityService`
        """
        model = EntityService()
        if include_optional:
            return EntityService(
                acc_error = '',
                acc_errors = 56,
                acc_key = '',
                acc_name = '',
                acc_owner = '',
                acc_pass = '',
                acc_share = True,
                acc_sync = True,
                acc_timeout = '',
                acc_type = '',
                acc_url = '',
                acc_user = '',
                created_at = '',
                deleted_at = '',
                id = 56,
                retry_limit = 56,
                share_expires = 56,
                share_path = '',
                share_size = '',
                sync_date = photoprism_client.models.sql/null_time.sql.NullTime(
                    time = '',
                    valid = True, ),
                sync_download = True,
                sync_filenames = True,
                sync_interval = 56,
                sync_path = '',
                sync_raw = True,
                sync_status = '',
                sync_upload = True,
                updated_at = ''
            )
        else:
            return EntityService(
        )
        """

    def testEntityService(self):
        """Test EntityService"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
