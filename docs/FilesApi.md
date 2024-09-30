# photoprism_client.FilesApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_markers_post**](FilesApi.md#api_v1_markers_post) | **POST** /api/v1/markers |
[**change_file_orientation**](FilesApi.md#change_file_orientation) | **PUT** /api/v1/photos/{uid}/files/{fileuid}/orientation | changes the orientation of a file
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /api/v1/photos/{uid}/files/{fileuid} | removes a file from storage
[**get_download**](FilesApi.md#get_download) | **GET** /api/v1/dl/{hash} | returns the raw file data
[**get_file**](FilesApi.md#get_file) | **GET** /api/v1/files/{hash} | returns file details as JSON
[**get_photo_download**](FilesApi.md#get_photo_download) | **GET** /api/v1/photos/{uid}/dl | returns the primary file matching that belongs to the photo
[**get_thumb**](FilesApi.md#get_thumb) | **GET** /api/v1/t/{thumb}/{token}/{size} | returns a thumbnail image with the requested size
[**get_video**](FilesApi.md#get_video) | **GET** /api/v1/videos/{hash}/{token}/{format} | returns a video, optionally limited to a byte range for streaming
[**users_uid_upload_token_post**](FilesApi.md#users_uid_upload_token_post) | **POST** /users/{uid}/upload/{token} |
[**zip_create**](FilesApi.md#zip_create) | **POST** /api/v1/zip | creates a zip file archive for download
[**zip_download**](FilesApi.md#zip_download) | **GET** /api/v1/zip/{filename} | downloads a zip file archive


# **api_v1_markers_post**
> api_v1_markers_post()



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
    api_instance = photoprism_client.FilesApi(api_client)

    try:
        api_instance.api_v1_markers_post()
    except Exception as e:
        print("Exception when calling FilesApi->api_v1_markers_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_file_orientation**
> EntityPhoto change_file_orientation(uid, fileuid, file)

changes the orientation of a file

### Example


```python
import photoprism_client
from photoprism_client.models.entity_photo import EntityPhoto
from photoprism_client.models.form_file import FormFile
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
    api_instance = photoprism_client.FilesApi(api_client)
    uid = 'uid_example' # str | photo uid
    fileuid = 'fileuid_example' # str | file uid
    file = photoprism_client.FormFile() # FormFile | file orientation

    try:
        # changes the orientation of a file
        api_response = api_instance.change_file_orientation(uid, fileuid, file)
        print("The response of FilesApi->change_file_orientation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->change_file_orientation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| photo uid |
 **fileuid** | **str**| file uid |
 **file** | [**FormFile**](FormFile.md)| file orientation |

### Return type

[**EntityPhoto**](EntityPhoto.md)

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

# **delete_file**
> EntityPhoto delete_file(uid, fileuid)

removes a file from storage

### Example


```python
import photoprism_client
from photoprism_client.models.entity_photo import EntityPhoto
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
    api_instance = photoprism_client.FilesApi(api_client)
    uid = 'uid_example' # str | photo uid
    fileuid = 'fileuid_example' # str | file uid

    try:
        # removes a file from storage
        api_response = api_instance.delete_file(uid, fileuid)
        print("The response of FilesApi->delete_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| photo uid |
 **fileuid** | **str**| file uid |

### Return type

[**EntityPhoto**](EntityPhoto.md)

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
**500** | Internal Server Error |  -  |

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
    api_instance = photoprism_client.FilesApi(api_client)
    hash = 'hash_example' # str | File Hash

    try:
        # returns the raw file data
        api_response = api_instance.get_download(hash)
        print("The response of FilesApi->get_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_download: %s\n" % e)
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

# **get_file**
> EntityFile get_file(hash)

returns file details as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.entity_file import EntityFile
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
    api_instance = photoprism_client.FilesApi(api_client)
    hash = 'hash_example' # str | hash (string) SHA-1 hash of the file

    try:
        # returns file details as JSON
        api_response = api_instance.get_file(hash)
        print("The response of FilesApi->get_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| hash (string) SHA-1 hash of the file |

### Return type

[**EntityFile**](EntityFile.md)

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
    api_instance = photoprism_client.FilesApi(api_client)
    uid = 'uid_example' # str | photo uid

    try:
        # returns the primary file matching that belongs to the photo
        api_response = api_instance.get_photo_download(uid)
        print("The response of FilesApi->get_photo_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_photo_download: %s\n" % e)
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
    api_instance = photoprism_client.FilesApi(api_client)
    thumb = 'thumb_example' # str | SHA1 file hash, optionally with a crop area suffixed, e.g. '-016014058037'
    token = 'token_example' # str | user-specific security token provided with session or 'public' when running PhotoPrism in public mode
    size = 'size_example' # str | thumbnail size

    try:
        # returns a thumbnail image with the requested size
        api_response = api_instance.get_thumb(thumb, token, size)
        print("The response of FilesApi->get_thumb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_thumb: %s\n" % e)
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
    api_instance = photoprism_client.FilesApi(api_client)
    hash = 'hash_example' # str | SHA1 video file hash
    token = 'token_example' # str | user-specific security token provided with session
    format = 'format_example' # str | video format

    try:
        # returns a video, optionally limited to a byte range for streaming
        api_response = api_instance.get_video(hash, token, format)
        print("The response of FilesApi->get_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_video: %s\n" % e)
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

# **users_uid_upload_token_post**
> users_uid_upload_token_post()



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
    api_instance = photoprism_client.FilesApi(api_client)

    try:
        api_instance.users_uid_upload_token_post()
    except Exception as e:
        print("Exception when calling FilesApi->users_uid_upload_token_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = photoprism_client.FilesApi(api_client)
    photos = photoprism_client.FormSelection() # FormSelection | Photo Selection

    try:
        # creates a zip file archive for download
        api_response = api_instance.zip_create(photos)
        print("The response of FilesApi->zip_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->zip_create: %s\n" % e)
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
    api_instance = photoprism_client.FilesApi(api_client)
    filename = 'filename_example' # str | zip filename

    try:
        # downloads a zip file archive
        api_response = api_instance.zip_download(filename)
        print("The response of FilesApi->zip_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->zip_download: %s\n" % e)
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

