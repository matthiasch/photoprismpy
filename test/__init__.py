
import photoprism_client


def _get_api_client(host='https://demo.photoprism.app',
                    my_ca=None,
                    username='demo',
                    auth_header="X-Auth-Token",
                    auth_key='123456-123456-123456-123456'
                    ):
    """
    Get default client connecting to 'https://demo.photoprism.app'
    """

    # Defining the host is optional and defaults to http://demo.photoprism.app
    # See configuration.py for a list of all supported configuration parameters.
    configuration = photoprism_client.Configuration(
        host=host,
        username=username,
        ssl_ca_cert=my_ca
    )

    api_client = photoprism_client.ApiClient(configuration,
                                             header_name=auth_header,
                                             header_value=auth_key)
    return api_client
