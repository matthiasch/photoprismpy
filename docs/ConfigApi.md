# photoprism_client.ConfigApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_config**](ConfigApi.md#get_client_config) | **GET** /api/v1/config | returns the client configuration values as JSON
[**get_config_options**](ConfigApi.md#get_config_options) | **GET** /api/v1/config/options | returns backend config options
[**save_config_options**](ConfigApi.md#save_config_options) | **POST** /api/v1/config/options | updates backend config options


# **get_client_config**
> ConfigClientConfig get_client_config()

returns the client configuration values as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.config_client_config import ConfigClientConfig
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
    api_instance = photoprism_client.ConfigApi(api_client)

    try:
        # returns the client configuration values as JSON
        api_response = api_instance.get_client_config()
        print("The response of ConfigApi->get_client_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->get_client_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ConfigClientConfig**](ConfigClientConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_options**
> ConfigOptions get_config_options()

returns backend config options

### Example


```python
import photoprism_client
from photoprism_client.models.config_options import ConfigOptions
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
    api_instance = photoprism_client.ConfigApi(api_client)

    try:
        # returns backend config options
        api_response = api_instance.get_config_options()
        print("The response of ConfigApi->get_config_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->get_config_options: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ConfigOptions**](ConfigOptions.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_config_options**
> ConfigOptions save_config_options(options)

updates backend config options

### Example


```python
import photoprism_client
from photoprism_client.models.config_options import ConfigOptions
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
    api_instance = photoprism_client.ConfigApi(api_client)
    options = photoprism_client.ConfigOptions() # ConfigOptions | properties to be updated (only submit values that should be changed)

    try:
        # updates backend config options
        api_response = api_instance.save_config_options(options)
        print("The response of ConfigApi->save_config_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->save_config_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**ConfigOptions**](ConfigOptions.md)| properties to be updated (only submit values that should be changed) |

### Return type

[**ConfigOptions**](ConfigOptions.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

