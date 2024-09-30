# photoprism_client.DownloadApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zip_create**](DownloadApi.md#zip_create) | **POST** /api/v1/zip | creates a zip file archive for download
[**zip_download**](DownloadApi.md#zip_download) | **GET** /api/v1/zip/{filename} | downloads a zip file archive


# **zip_create**
> I18nResponse zip_create(photos)

creates a zip file archive for download

### Example


```python
import photoprism_client
from photoprism_client.models.form_selection import FormSelection
from photoprism_client.models.i18n_response import I18nResponse
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
    api_instance = photoprism_client.DownloadApi(api_client)
    photos = photoprism_client.FormSelection() # FormSelection | Photo Selection

    try:
        # creates a zip file archive for download
        api_response = api_instance.zip_create(photos)
        print("The response of DownloadApi->zip_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadApi->zip_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photos** | [**FormSelection**](FormSelection.md)| Photo Selection |

### Return type

[**I18nResponse**](I18nResponse.md)

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

# **zip_download**
> bytearray zip_download(filename)

downloads a zip file archive

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
    api_instance = photoprism_client.DownloadApi(api_client)
    filename = 'filename_example' # str | zip filename

    try:
        # downloads a zip file archive
        api_response = api_instance.zip_download(filename)
        print("The response of DownloadApi->zip_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadApi->zip_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| zip filename |

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

