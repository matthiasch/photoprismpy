# photoprism_client.VideosApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_video**](VideosApi.md#get_video) | **GET** /api/v1/videos/{hash}/{token}/{format} | returns a video, optionally limited to a byte range for streaming


# **get_video**
> bytearray get_video(hash, token, format)

returns a video, optionally limited to a byte range for streaming

Fore more information see: - https://docs.photoprism.app/developer-guide/api/thumbnails/#video-endpoint-uri

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
    api_instance = photoprism_client.VideosApi(api_client)
    hash = 'hash_example' # str | SHA1 video file hash
    token = 'token_example' # str | user-specific security token provided with session
    format = 'format_example' # str | video format

    try:
        # returns a video, optionally limited to a byte range for streaming
        api_response = api_instance.get_video(hash, token, format)
        print("The response of VideosApi->get_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->get_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| SHA1 video file hash |
 **token** | **str**| user-specific security token provided with session |
 **format** | **str**| video format |

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

