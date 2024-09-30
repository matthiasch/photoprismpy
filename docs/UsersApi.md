# photoprism_client.UsersApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_users_uid_avatar_post**](UsersApi.md#api_v1_users_uid_avatar_post) | **POST** /api/v1/users/{uid}/avatar |
[**api_v1_users_uid_passcode_activate_post**](UsersApi.md#api_v1_users_uid_passcode_activate_post) | **POST** /api/v1/users/{uid}/passcode/activate |
[**api_v1_users_uid_passcode_confirm_post**](UsersApi.md#api_v1_users_uid_passcode_confirm_post) | **POST** /api/v1/users/{uid}/passcode/confirm |
[**api_v1_users_uid_passcode_deactivate_post**](UsersApi.md#api_v1_users_uid_passcode_deactivate_post) | **POST** /api/v1/users/{uid}/passcode/deactivate |
[**api_v1_users_uid_passcode_post**](UsersApi.md#api_v1_users_uid_passcode_post) | **POST** /api/v1/users/{uid}/passcode |
[**api_v1_users_uid_password_put**](UsersApi.md#api_v1_users_uid_password_put) | **PUT** /api/v1/users/{uid}/password |
[**api_v1_users_uid_put**](UsersApi.md#api_v1_users_uid_put) | **PUT** /api/v1/users/{uid} |
[**api_v1_users_uid_sessions_get**](UsersApi.md#api_v1_users_uid_sessions_get) | **GET** /api/v1/users/{uid}/sessions |
[**users_uid_upload_token_post**](UsersApi.md#users_uid_upload_token_post) | **POST** /users/{uid}/upload/{token} |


# **api_v1_users_uid_avatar_post**
> api_v1_users_uid_avatar_post()



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
    api_instance = photoprism_client.UsersApi(api_client)

    try:
        api_instance.api_v1_users_uid_avatar_post()
    except Exception as e:
        print("Exception when calling UsersApi->api_v1_users_uid_avatar_post: %s\n" % e)
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

# **api_v1_users_uid_passcode_activate_post**
> api_v1_users_uid_passcode_activate_post()



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
    api_instance = photoprism_client.UsersApi(api_client)

    try:
        api_instance.api_v1_users_uid_passcode_activate_post()
    except Exception as e:
        print("Exception when calling UsersApi->api_v1_users_uid_passcode_activate_post: %s\n" % e)
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

# **api_v1_users_uid_passcode_confirm_post**
> api_v1_users_uid_passcode_confirm_post()



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
    api_instance = photoprism_client.UsersApi(api_client)

    try:
        api_instance.api_v1_users_uid_passcode_confirm_post()
    except Exception as e:
        print("Exception when calling UsersApi->api_v1_users_uid_passcode_confirm_post: %s\n" % e)
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

# **api_v1_users_uid_passcode_deactivate_post**
> api_v1_users_uid_passcode_deactivate_post()



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
    api_instance = photoprism_client.UsersApi(api_client)

    try:
        api_instance.api_v1_users_uid_passcode_deactivate_post()
    except Exception as e:
        print("Exception when calling UsersApi->api_v1_users_uid_passcode_deactivate_post: %s\n" % e)
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

# **api_v1_users_uid_passcode_post**
> api_v1_users_uid_passcode_post()



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
    api_instance = photoprism_client.UsersApi(api_client)

    try:
        api_instance.api_v1_users_uid_passcode_post()
    except Exception as e:
        print("Exception when calling UsersApi->api_v1_users_uid_passcode_post: %s\n" % e)
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
    api_instance = photoprism_client.UsersApi(api_client)

    try:
        api_instance.api_v1_users_uid_password_put()
    except Exception as e:
        print("Exception when calling UsersApi->api_v1_users_uid_password_put: %s\n" % e)
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

# **api_v1_users_uid_put**
> api_v1_users_uid_put()



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
    api_instance = photoprism_client.UsersApi(api_client)

    try:
        api_instance.api_v1_users_uid_put()
    except Exception as e:
        print("Exception when calling UsersApi->api_v1_users_uid_put: %s\n" % e)
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
    api_instance = photoprism_client.UsersApi(api_client)

    try:
        api_instance.api_v1_users_uid_sessions_get()
    except Exception as e:
        print("Exception when calling UsersApi->api_v1_users_uid_sessions_get: %s\n" % e)
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

# **users_uid_upload_token_post**
> users_uid_upload_token_post()



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
    api_instance = photoprism_client.UsersApi(api_client)

    try:
        api_instance.users_uid_upload_token_post()
    except Exception as e:
        print("Exception when calling UsersApi->users_uid_upload_token_post: %s\n" % e)
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

