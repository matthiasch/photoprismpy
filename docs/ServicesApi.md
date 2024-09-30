# photoprism_client.ServicesApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_service**](ServicesApi.md#add_service) | **POST** /api/v1/services | creates a new remote account configuration
[**delete_service**](ServicesApi.md#delete_service) | **DELETE** /api/v1/services/{id} | removes a remote account configuration
[**get_service**](ServicesApi.md#get_service) | **GET** /api/v1/services/{id} | returns an account as JSON
[**get_service_folders**](ServicesApi.md#get_service_folders) | **GET** /api/v1/services/{id}/folders | returns folders that belong to an account as JSON
[**search_services**](ServicesApi.md#search_services) | **GET** /api/v1/services | finds account settings and returns them as JSON
[**update_service**](ServicesApi.md#update_service) | **PUT** /api/v1/services/{id} | updates a remote account configuration


# **add_service**
> EntityService add_service(service)

creates a new remote account configuration

### Example


```python
import photoprism_client
from photoprism_client.models.entity_service import EntityService
from photoprism_client.models.form_service import FormService
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
    api_instance = photoprism_client.ServicesApi(api_client)
    service = photoprism_client.FormService() # FormService | properties of the service to be created

    try:
        # creates a new remote account configuration
        api_response = api_instance.add_service(service)
        print("The response of ServicesApi->add_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->add_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | [**FormService**](FormService.md)| properties of the service to be created |

### Return type

[**EntityService**](EntityService.md)

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

# **delete_service**
> delete_service(id)

removes a remote account configuration

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
    api_instance = photoprism_client.ServicesApi(api_client)
    id = 'id_example' # str | service id

    try:
        # removes a remote account configuration
        api_instance.delete_service(id)
    except Exception as e:
        print("Exception when calling ServicesApi->delete_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| service id |

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service**
> EntityService get_service(id)

returns an account as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.entity_service import EntityService
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
    api_instance = photoprism_client.ServicesApi(api_client)
    id = 'id_example' # str | service id

    try:
        # returns an account as JSON
        api_response = api_instance.get_service(id)
        print("The response of ServicesApi->get_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| service id |

### Return type

[**EntityService**](EntityService.md)

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

# **get_service_folders**
> List[object] get_service_folders(id)

returns folders that belong to an account as JSON

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
    api_instance = photoprism_client.ServicesApi(api_client)
    id = 'id_example' # str | service id

    try:
        # returns folders that belong to an account as JSON
        api_response = api_instance.get_service_folders(id)
        print("The response of ServicesApi->get_service_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| service id |

### Return type

**List[object]**

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

# **search_services**
> List[EntityService] search_services(count)

finds account settings and returns them as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.entity_service import EntityService
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
    api_instance = photoprism_client.ServicesApi(api_client)
    count = 56 # int | maximum number of results

    try:
        # finds account settings and returns them as JSON
        api_response = api_instance.search_services(count)
        print("The response of ServicesApi->search_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->search_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| maximum number of results |

### Return type

[**List[EntityService]**](EntityService.md)

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

# **update_service**
> EntityService update_service(id, service)

updates a remote account configuration

### Example


```python
import photoprism_client
from photoprism_client.models.entity_service import EntityService
from photoprism_client.models.form_service import FormService
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
    api_instance = photoprism_client.ServicesApi(api_client)
    id = 'id_example' # str | service id
    service = photoprism_client.FormService() # FormService | properties to be updated (only submit values that should be changed)

    try:
        # updates a remote account configuration
        api_response = api_instance.update_service(id, service)
        print("The response of ServicesApi->update_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->update_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| service id |
 **service** | [**FormService**](FormService.md)| properties to be updated (only submit values that should be changed) |

### Return type

[**EntityService**](EntityService.md)

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

