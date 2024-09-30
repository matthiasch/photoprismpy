# photoprism_client.MarkersApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_marker_subject**](MarkersApi.md#clear_marker_subject) | **DELETE** /api/v1/markers/{uid}/subject | removes an existing marker subject association
[**update_marker**](MarkersApi.md#update_marker) | **PUT** /api/v1/markers/{uid} | updates an existing file area marker to assign faces or other subjects


# **clear_marker_subject**
> EntityMarker clear_marker_subject(uid)

removes an existing marker subject association

### Example


```python
import photoprism_client
from photoprism_client.models.entity_marker import EntityMarker
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
    api_instance = photoprism_client.MarkersApi(api_client)
    uid = 'uid_example' # str | marker uid

    try:
        # removes an existing marker subject association
        api_response = api_instance.clear_marker_subject(uid)
        print("The response of MarkersApi->clear_marker_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkersApi->clear_marker_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| marker uid |

### Return type

[**EntityMarker**](EntityMarker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_marker**
> EntityMarker update_marker(uid, marker)

updates an existing file area marker to assign faces or other subjects

### Example


```python
import photoprism_client
from photoprism_client.models.entity_marker import EntityMarker
from photoprism_client.models.form_marker import FormMarker
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
    api_instance = photoprism_client.MarkersApi(api_client)
    uid = 'uid_example' # str | marker uid
    marker = photoprism_client.FormMarker() # FormMarker | properties to be updated

    try:
        # updates an existing file area marker to assign faces or other subjects
        api_response = api_instance.update_marker(uid, marker)
        print("The response of MarkersApi->update_marker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkersApi->update_marker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| marker uid |
 **marker** | [**FormMarker**](FormMarker.md)| properties to be updated |

### Return type

[**EntityMarker**](EntityMarker.md)

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
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

