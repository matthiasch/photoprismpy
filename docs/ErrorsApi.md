# photoprism_client.ErrorsApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_errors**](ErrorsApi.md#delete_errors) | **DELETE** /api/v1/errors | removes all entries from the error logs
[**get_errors**](ErrorsApi.md#get_errors) | **GET** /api/v1/errors | searches the error logs and returns the results as JSON


# **delete_errors**
> delete_errors()

removes all entries from the error logs

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
    api_instance = photoprism_client.ErrorsApi(api_client)

    try:
        # removes all entries from the error logs
        api_instance.delete_errors()
    except Exception as e:
        print("Exception when calling ErrorsApi->delete_errors: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_errors**
> EntityError get_errors(count, offset=offset, q=q)

searches the error logs and returns the results as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.entity_error import EntityError
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
    api_instance = photoprism_client.ErrorsApi(api_client)
    count = 56 # int | maximum number of results
    offset = 56 # int | search result offset (optional)
    q = 'q_example' # str | search query (optional)

    try:
        # searches the error logs and returns the results as JSON
        api_response = api_instance.get_errors(count, offset=offset, q=q)
        print("The response of ErrorsApi->get_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorsApi->get_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| maximum number of results |
 **offset** | **int**| search result offset | [optional]
 **q** | **str**| search query | [optional]

### Return type

[**EntityError**](EntityError.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

