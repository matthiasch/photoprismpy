# coding: utf-8

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from photoprism_client.models.form_subject import FormSubject

class TestFormSubject(unittest.TestCase):
    """FormSubject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FormSubject:
        """Test FormSubject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FormSubject`
        """
        model = FormSubject()
        if include_optional:
            return FormSubject(
                about = '',
                alias = '',
                bio = '',
                excluded = True,
                favorite = True,
                hidden = True,
                name = '',
                notes = '',
                private = True
            )
        else:
            return FormSubject(
        )
        """

    def testFormSubject(self):
        """Test FormSubject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
