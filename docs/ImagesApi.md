# photoprism_client.ImagesApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**album_cover**](ImagesApi.md#album_cover) | **GET** /api/v1/albums/{uid}/t/{token}/{size} | returns an album cover image
[**download_album**](ImagesApi.md#download_album) | **GET** /api/v1/albums/{uid}/dl | streams the album contents as zip archiv
[**folder_cover**](ImagesApi.md#folder_cover) | **GET** /api/v1/folders/t/{uid}/{token}/{size} | returns a folder cover image
[**get_download**](ImagesApi.md#get_download) | **GET** /api/v1/dl/{hash} | returns the raw file data
[**get_photo_download**](ImagesApi.md#get_photo_download) | **GET** /api/v1/photos/{uid}/dl | returns the primary file matching that belongs to the photo
[**get_thumb**](ImagesApi.md#get_thumb) | **GET** /api/v1/t/{thumb}/{token}/{size} | returns a thumbnail image with the requested size
[**label_cover**](ImagesApi.md#label_cover) | **GET** /api/v1/labels/{uid}/t/{token}/{size} | returns a label cover image


# **album_cover**
> bytearray album_cover(uid, token, size)

returns an album cover image

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
    api_instance = photoprism_client.ImagesApi(api_client)
    uid = 'uid_example' # str | Album UID
    token = 'token_example' # str | user-specific security token provided with session or 'public' when running PhotoPrism in public mode
    size = 'size_example' # str | thumbnail size

    try:
        # returns an album cover image
        api_response = api_instance.album_cover(uid, token, size)
        print("The response of ImagesApi->album_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->album_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Album UID |
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

# **download_album**
> bytearray download_album(uid)

streams the album contents as zip archiv

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
    api_instance = photoprism_client.ImagesApi(api_client)
    uid = 'uid_example' # str | Album UID

    try:
        # streams the album contents as zip archiv
        api_response = api_instance.download_album(uid)
        print("The response of ImagesApi->download_album:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->download_album: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Album UID |

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
    api_instance = photoprism_client.ImagesApi(api_client)
    uid = 'uid_example' # str | folder uid
    token = 'token_example' # str | user-specific security token provided with session or 'public' when running PhotoPrism in public mode
    size = 'size_example' # str | thumbnail size

    try:
        # returns a folder cover image
        api_response = api_instance.folder_cover(uid, token, size)
        print("The response of ImagesApi->folder_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->folder_cover: %s\n" % e)
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

# **get_download**
> bytearray get_download(hash)

returns the raw file data

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
    api_instance = photoprism_client.ImagesApi(api_client)
    hash = 'hash_example' # str | File Hash

    try:
        # returns the raw file data
        api_response = api_instance.get_download(hash)
        print("The response of ImagesApi->get_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| File Hash |

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_photo_download**
> bytearray get_photo_download(uid)

returns the primary file matching that belongs to the photo

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
    api_instance = photoprism_client.ImagesApi(api_client)
    uid = 'uid_example' # str | photo uid

    try:
        # returns the primary file matching that belongs to the photo
        api_response = api_instance.get_photo_download(uid)
        print("The response of ImagesApi->get_photo_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_photo_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| photo uid |

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thumb**
> bytearray get_thumb(thumb, token, size)

returns a thumbnail image with the requested size

Fore more information see: - https://docs.photoprism.app/developer-guide/api/thumbnails/#image-endpoint-uri

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
    api_instance = photoprism_client.ImagesApi(api_client)
    thumb = 'thumb_example' # str | SHA1 file hash, optionally with a crop area suffixed, e.g. '-016014058037'
    token = 'token_example' # str | user-specific security token provided with session or 'public' when running PhotoPrism in public mode
    size = 'size_example' # str | thumbnail size

    try:
        # returns a thumbnail image with the requested size
        api_response = api_instance.get_thumb(thumb, token, size)
        print("The response of ImagesApi->get_thumb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_thumb: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thumb** | **str**| SHA1 file hash, optionally with a crop area suffixed, e.g. &#39;-016014058037&#39; |
 **token** | **str**| user-specific security token provided with session or &#39;public&#39; when running PhotoPrism in public mode |
 **size** | **str**| thumbnail size |

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_cover**
> bytearray label_cover(uid, token, size)

returns a label cover image

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
    api_instance = photoprism_client.ImagesApi(api_client)
    uid = 'uid_example' # str | Label UID
    token = 'token_example' # str | user-specific security token provided with session or 'public' when running PhotoPrism in public mode
    size = 'size_example' # str | thumbnail size

    try:
        # returns a label cover image
        api_response = api_instance.label_cover(uid, token, size)
        print("The response of ImagesApi->label_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->label_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Label UID |
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

