# photoprism_client.FoldersApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_cover**](FoldersApi.md#folder_cover) | **GET** /api/v1/folders/t/{uid}/{token}/{size} | returns a folder cover image


# **folder_cover**
> bytearray folder_cover(uid, token, size)

returns a folder cover image

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
    api_instance = photoprism_client.FoldersApi(api_client)
    uid = 'uid_example' # str | folder uid
    token = 'token_example' # str | user-specific security token provided with session or 'public' when running PhotoPrism in public mode
    size = 'size_example' # str | thumbnail size

    try:
        # returns a folder cover image
        api_response = api_instance.folder_cover(uid, token, size)
        print("The response of FoldersApi->folder_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->folder_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| folder uid |
 **token** | **str**| user-specific security token provided with session or &#39;public&#39; when running PhotoPrism in public mode |
 **size** | **str**| thumbnail size |

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg, image/svg+xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

