# photoprism_client.FacesApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_face**](FacesApi.md#get_face) | **GET** /api/v1/faces/{id} | returns a face as JSON
[**search_faces**](FacesApi.md#search_faces) | **GET** /api/v1/faces | finds and returns faces as JSON
[**update_face**](FacesApi.md#update_face) | **PUT** /api/v1/faces/{id} | updates face properties


# **get_face**
> EntityFace get_face(id)

returns a face as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.entity_face import EntityFace
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
    api_instance = photoprism_client.FacesApi(api_client)
    id = 'id_example' # str | face id

    try:
        # returns a face as JSON
        api_response = api_instance.get_face(id)
        print("The response of FacesApi->get_face:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FacesApi->get_face: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| face id |

### Return type

[**EntityFace**](EntityFace.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_faces**
> List[SearchFace] search_faces(count, offset=offset, order=order, hidden=hidden, unknown=unknown)

finds and returns faces as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.search_face import SearchFace
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
    api_instance = photoprism_client.FacesApi(api_client)
    count = 56 # int | maximum number of results
    offset = 56 # int | search result offset (optional)
    order = 'order_example' # str | sort order (optional)
    hidden = 'hidden_example' # str | show hidden (optional)
    unknown = 'unknown_example' # str | show unknown (optional)

    try:
        # finds and returns faces as JSON
        api_response = api_instance.search_faces(count, offset=offset, order=order, hidden=hidden, unknown=unknown)
        print("The response of FacesApi->search_faces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FacesApi->search_faces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| maximum number of results |
 **offset** | **int**| search result offset | [optional]
 **order** | **str**| sort order | [optional]
 **hidden** | **str**| show hidden | [optional]
 **unknown** | **str**| show unknown | [optional]

### Return type

[**List[SearchFace]**](SearchFace.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_face**
> EntityFace update_face(id, face)

updates face properties

### Example


```python
import photoprism_client
from photoprism_client.models.entity_face import EntityFace
from photoprism_client.models.form_face import FormFace
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
    api_instance = photoprism_client.FacesApi(api_client)
    id = 'id_example' # str | face id
    face = photoprism_client.FormFace() # FormFace | properties to be updated

    try:
        # updates face properties
        api_response = api_instance.update_face(id, face)
        print("The response of FacesApi->update_face:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FacesApi->update_face: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| face id |
 **face** | [**FormFace**](FormFace.md)| properties to be updated |

### Return type

[**EntityFace**](EntityFace.md)

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

