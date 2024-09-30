# photoprism_client.StacksApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**photo_primary**](StacksApi.md#photo_primary) | **POST** /api/v1/photos/{uid}/files/{fileuid}/primary | sets the primary file for a photo
[**photo_unstack**](StacksApi.md#photo_unstack) | **POST** /api/v1/photos/{uid}/files/{fileuid}/unstack | removes a file from an existing photo stack


# **photo_primary**
> EntityPhoto photo_primary(uid, fileuid)

sets the primary file for a photo

### Example


```python
import photoprism_client
from photoprism_client.models.entity_photo import EntityPhoto
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
    api_instance = photoprism_client.StacksApi(api_client)
    uid = 'uid_example' # str | photo uid
    fileuid = 'fileuid_example' # str | file uid

    try:
        # sets the primary file for a photo
        api_response = api_instance.photo_primary(uid, fileuid)
        print("The response of StacksApi->photo_primary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->photo_primary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| photo uid |
 **fileuid** | **str**| file uid |

### Return type

[**EntityPhoto**](EntityPhoto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **photo_unstack**
> EntityPhoto photo_unstack(uid, fileuid)

removes a file from an existing photo stack

### Example


```python
import photoprism_client
from photoprism_client.models.entity_photo import EntityPhoto
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
    api_instance = photoprism_client.StacksApi(api_client)
    uid = 'uid_example' # str | photo uid
    fileuid = 'fileuid_example' # str | file uid

    try:
        # removes a file from an existing photo stack
        api_response = api_instance.photo_unstack(uid, fileuid)
        print("The response of StacksApi->photo_unstack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->photo_unstack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| photo uid |
 **fileuid** | **str**| file uid |

### Return type

[**EntityPhoto**](EntityPhoto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

