# photoprism_client.SettingsApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_options**](SettingsApi.md#get_config_options) | **GET** /api/v1/config/options | returns backend config options
[**get_settings**](SettingsApi.md#get_settings) | **GET** /api/v1/settings | returns the user app settings as JSON
[**save_config_options**](SettingsApi.md#save_config_options) | **POST** /api/v1/config/options | updates backend config options
[**save_settings**](SettingsApi.md#save_settings) | **POST** /api/v1/settings | saves the user app settings


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
    api_instance = photoprism_client.SettingsApi(api_client)

    try:
        # returns backend config options
        api_response = api_instance.get_config_options()
        print("The response of SettingsApi->get_config_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_config_options: %s\n" % e)
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

# **get_settings**
> CustomizeSettings get_settings()

returns the user app settings as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.customize_settings import CustomizeSettings
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
    api_instance = photoprism_client.SettingsApi(api_client)

    try:
        # returns the user app settings as JSON
        api_response = api_instance.get_settings()
        print("The response of SettingsApi->get_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CustomizeSettings**](CustomizeSettings.md)

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
    api_instance = photoprism_client.SettingsApi(api_client)
    options = photoprism_client.ConfigOptions() # ConfigOptions | properties to be updated (only submit values that should be changed)

    try:
        # updates backend config options
        api_response = api_instance.save_config_options(options)
        print("The response of SettingsApi->save_config_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->save_config_options: %s\n" % e)
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

# **save_settings**
> CustomizeSettings save_settings(settings)

saves the user app settings

### Example


```python
import photoprism_client
from photoprism_client.models.customize_settings import CustomizeSettings
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
    api_instance = photoprism_client.SettingsApi(api_client)
    settings = photoprism_client.CustomizeSettings() # CustomizeSettings | user settings

    try:
        # saves the user app settings
        api_response = api_instance.save_settings(settings)
        print("The response of SettingsApi->save_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->save_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**CustomizeSettings**](CustomizeSettings.md)| user settings |

### Return type

[**CustomizeSettings**](CustomizeSettings.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

