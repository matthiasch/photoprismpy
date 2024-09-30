# photoprism_client.AuthenticationApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_oauth_revoke_post**](AuthenticationApi.md#api_v1_oauth_revoke_post) | **POST** /api/v1/oauth/revoke |
[**api_v1_oauth_token_post**](AuthenticationApi.md#api_v1_oauth_token_post) | **POST** /api/v1/oauth/token |
[**api_v1_session_post**](AuthenticationApi.md#api_v1_session_post) | **POST** /api/v1/session |
[**api_v1_sessions_post**](AuthenticationApi.md#api_v1_sessions_post) | **POST** /api/v1/sessions |
[**api_v1_users_uid_password_put**](AuthenticationApi.md#api_v1_users_uid_password_put) | **PUT** /api/v1/users/{uid}/password |
[**api_v1_users_uid_sessions_get**](AuthenticationApi.md#api_v1_users_uid_sessions_get) | **GET** /api/v1/users/{uid}/sessions |


# **api_v1_oauth_revoke_post**
> api_v1_oauth_revoke_post()



### Example


```python
import photoprism_client
from photoprism_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://demo.photoprism.app
# See configuration.py for a list of all supported configuration parameters.
configuration = photoprism_client.Configuration(
    host = "http://demo.photoprism.app"
)


# Enter a context with an instance of the API client
with photoprism_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = photoprism_client.AuthenticationApi(api_client)

    try:
        api_instance.api_v1_oauth_revoke_post()
    except Exception as e:
        print("Exception when calling AuthenticationApi->api_v1_oauth_revoke_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_oauth_token_post**
> api_v1_oauth_token_post()



### Example


```python
import photoprism_client
from photoprism_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://demo.photoprism.app
# See configuration.py for a list of all supported configuration parameters.
configuration = photoprism_client.Configuration(
    host = "http://demo.photoprism.app"
)


# Enter a context with an instance of the API client
with photoprism_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = photoprism_client.AuthenticationApi(api_client)

    try:
        api_instance.api_v1_oauth_token_post()
    except Exception as e:
        print("Exception when calling AuthenticationApi->api_v1_oauth_token_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_session_post**
> api_v1_session_post()



### Example


```python
import photoprism_client
from photoprism_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://demo.photoprism.app
# See configuration.py for a list of all supported configuration parameters.
configuration = photoprism_client.Configuration(
    host = "http://demo.photoprism.app"
)


# Enter a context with an instance of the API client
with photoprism_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = photoprism_client.AuthenticationApi(api_client)

    try:
        api_instance.api_v1_session_post()
    except Exception as e:
        print("Exception when calling AuthenticationApi->api_v1_session_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_sessions_post**
> api_v1_sessions_post()



### Example


```python
import photoprism_client
from photoprism_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://demo.photoprism.app
# See configuration.py for a list of all supported configuration parameters.
configuration = photoprism_client.Configuration(
    host = "http://demo.photoprism.app"
)


# Enter a context with an instance of the API client
with photoprism_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = photoprism_client.AuthenticationApi(api_client)

    try:
        api_instance.api_v1_sessions_post()
    except Exception as e:
        print("Exception when calling AuthenticationApi->api_v1_sessions_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_uid_password_put**
> api_v1_users_uid_password_put()



### Example


```python
import photoprism_client
from photoprism_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://demo.photoprism.app
# See configuration.py for a list of all supported configuration parameters.
configuration = photoprism_client.Configuration(
    host = "http://demo.photoprism.app"
)


# Enter a context with an instance of the API client
with photoprism_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = photoprism_client.AuthenticationApi(api_client)

    try:
        api_instance.api_v1_users_uid_password_put()
    except Exception as e:
        print("Exception when calling AuthenticationApi->api_v1_users_uid_password_put: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_uid_sessions_get**
> api_v1_users_uid_sessions_get()



### Example


```python
import photoprism_client
from photoprism_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://demo.photoprism.app
# See configuration.py for a list of all supported configuration parameters.
configuration = photoprism_client.Configuration(
    host = "http://demo.photoprism.app"
)


# Enter a context with an instance of the API client
with photoprism_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = photoprism_client.AuthenticationApi(api_client)

    try:
        api_instance.api_v1_users_uid_sessions_get()
    except Exception as e:
        print("Exception when calling AuthenticationApi->api_v1_users_uid_sessions_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

