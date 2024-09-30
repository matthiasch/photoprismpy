# photoprism_client.PhotosApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_photo_label**](PhotosApi.md#add_photo_label) | **POST** /api/v1/photos/{uid}/label | adds a label to a photo
[**approve_photo**](PhotosApi.md#approve_photo) | **POST** /api/v1/photos/{uid}/approve | marks a photo in review as approved
[**batch_photos_approve**](PhotosApi.md#batch_photos_approve) | **POST** /api/v1/batch/photos/approve | approves multiple photos that are currently under review
[**batch_photos_archive**](PhotosApi.md#batch_photos_archive) | **POST** /api/v1/batch/photos/archive | moves multiple photos to the archive
[**batch_photos_delete**](PhotosApi.md#batch_photos_delete) | **POST** /api/v1/batch/photos/delete | permanently removes multiple or all photos from the archive
[**batch_photos_private**](PhotosApi.md#batch_photos_private) | **POST** /api/v1/batch/photos/private | toggles private state of multiple photos
[**batch_photos_restore**](PhotosApi.md#batch_photos_restore) | **POST** /api/v1/batch/photos/restore | restores multiple photos from the archive
[**dislike_photo**](PhotosApi.md#dislike_photo) | **DELETE** /api/v1/photos/{uid}/like | removes the favorite flags from a photo
[**get_photo**](PhotosApi.md#get_photo) | **GET** /api/v1/photos/{uid} | returns picture details as JSON
[**get_photo_yaml**](PhotosApi.md#get_photo_yaml) | **GET** /api/v1/photos/{uid}/yaml | returns picture details as YAML
[**like_photo**](PhotosApi.md#like_photo) | **POST** /api/v1/photos/{uid}/like | flags a photo as favorite
[**photo_primary**](PhotosApi.md#photo_primary) | **POST** /api/v1/photos/{uid}/files/{fileuid}/primary | sets the primary file for a photo
[**photo_unstack**](PhotosApi.md#photo_unstack) | **POST** /api/v1/photos/{uid}/files/{fileuid}/unstack | removes a file from an existing photo stack
[**remove_photo_label**](PhotosApi.md#remove_photo_label) | **DELETE** /api/v1/photos/{uid}/label/{id} | removes a label from a photo
[**search_geo**](PhotosApi.md#search_geo) | **GET** /api/v1/geo | finds photos and returns results as JSON, so they can be displayed on a map or in a viewer
[**search_photos**](PhotosApi.md#search_photos) | **GET** /api/v1/photos | finds pictures and returns them as JSON
[**update_photo**](PhotosApi.md#update_photo) | **PUT** /api/v1/photos/{uid} | updates picture details and returns them as JSON
[**update_photo_label**](PhotosApi.md#update_photo_label) | **PUT** /api/v1/photos/{uid}/label/{id} | changes a photo label


# **add_photo_label**
> EntityPhoto add_photo_label(uid, label)

adds a label to a photo

### Example


```python
import photoprism_client
from photoprism_client.models.entity_photo import EntityPhoto
from photoprism_client.models.form_label import FormLabel
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
    api_instance = photoprism_client.PhotosApi(api_client)
    uid = 'uid_example' # str | photo uid
    label = photoprism_client.FormLabel() # FormLabel | label properties

    try:
        # adds a label to a photo
        api_response = api_instance.add_photo_label(uid, label)
        print("The response of PhotosApi->add_photo_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->add_photo_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| photo uid |
 **label** | [**FormLabel**](FormLabel.md)| label properties |

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

# **approve_photo**
> Dict[str, object] approve_photo(uid)

marks a photo in review as approved

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
    api_instance = photoprism_client.PhotosApi(api_client)
    uid = 'uid_example' # str | photo uid

    try:
        # marks a photo in review as approved
        api_response = api_instance.approve_photo(uid)
        print("The response of PhotosApi->approve_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->approve_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| photo uid |

### Return type

**Dict[str, object]**

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

# **batch_photos_approve**
> I18nResponse batch_photos_approve(photos)

approves multiple photos that are currently under review

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
    api_instance = photoprism_client.PhotosApi(api_client)
    photos = photoprism_client.FormSelection() # FormSelection | Photo Selection

    try:
        # approves multiple photos that are currently under review
        api_response = api_instance.batch_photos_approve(photos)
        print("The response of PhotosApi->batch_photos_approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->batch_photos_approve: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_photos_archive**
> I18nResponse batch_photos_archive(photos)

moves multiple photos to the archive

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
    api_instance = photoprism_client.PhotosApi(api_client)
    photos = photoprism_client.FormSelection() # FormSelection | Photo Selection

    try:
        # moves multiple photos to the archive
        api_response = api_instance.batch_photos_archive(photos)
        print("The response of PhotosApi->batch_photos_archive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->batch_photos_archive: %s\n" % e)
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

# **batch_photos_delete**
> I18nResponse batch_photos_delete(photos)

permanently removes multiple or all photos from the archive

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
    api_instance = photoprism_client.PhotosApi(api_client)
    photos = photoprism_client.FormSelection() # FormSelection | All or Photo Selection

    try:
        # permanently removes multiple or all photos from the archive
        api_response = api_instance.batch_photos_delete(photos)
        print("The response of PhotosApi->batch_photos_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->batch_photos_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photos** | [**FormSelection**](FormSelection.md)| All or Photo Selection |

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_photos_private**
> I18nResponse batch_photos_private(photos)

toggles private state of multiple photos

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
    api_instance = photoprism_client.PhotosApi(api_client)
    photos = photoprism_client.FormSelection() # FormSelection | Photo Selection

    try:
        # toggles private state of multiple photos
        api_response = api_instance.batch_photos_private(photos)
        print("The response of PhotosApi->batch_photos_private:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->batch_photos_private: %s\n" % e)
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

# **batch_photos_restore**
> I18nResponse batch_photos_restore(photos)

restores multiple photos from the archive

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
    api_instance = photoprism_client.PhotosApi(api_client)
    photos = photoprism_client.FormSelection() # FormSelection | Photo Selection

    try:
        # restores multiple photos from the archive
        api_response = api_instance.batch_photos_restore(photos)
        print("The response of PhotosApi->batch_photos_restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->batch_photos_restore: %s\n" % e)
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

# **dislike_photo**
> Dict[str, object] dislike_photo(uid)

removes the favorite flags from a photo

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
    api_instance = photoprism_client.PhotosApi(api_client)
    uid = 'uid_example' # str | photo uid

    try:
        # removes the favorite flags from a photo
        api_response = api_instance.dislike_photo(uid)
        print("The response of PhotosApi->dislike_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->dislike_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| photo uid |

### Return type

**Dict[str, object]**

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_photo**
> EntityPhoto get_photo(uid)

returns picture details as JSON

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
    api_instance = photoprism_client.PhotosApi(api_client)
    uid = 'uid_example' # str | Photo UID

    try:
        # returns picture details as JSON
        api_response = api_instance.get_photo(uid)
        print("The response of PhotosApi->get_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->get_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Photo UID |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_photo_yaml**
> bytearray get_photo_yaml(uid)

returns picture details as YAML

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
    api_instance = photoprism_client.PhotosApi(api_client)
    uid = 'uid_example' # str | photo uid

    try:
        # returns picture details as YAML
        api_response = api_instance.get_photo_yaml(uid)
        print("The response of PhotosApi->get_photo_yaml:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->get_photo_yaml: %s\n" % e)
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
 - **Accept**: text/x-yaml

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

# **like_photo**
> Dict[str, object] like_photo(uid)

flags a photo as favorite

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
    api_instance = photoprism_client.PhotosApi(api_client)
    uid = 'uid_example' # str | photo uid

    try:
        # flags a photo as favorite
        api_response = api_instance.like_photo(uid)
        print("The response of PhotosApi->like_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->like_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| photo uid |

### Return type

**Dict[str, object]**

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **photo_primary**
> EntityPhoto photo_primary(uid, fileuid)

sets the primary file for a photo

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
    api_instance = photoprism_client.PhotosApi(api_client)
    uid = 'uid_example' # str | photo uid
    fileuid = 'fileuid_example' # str | file uid

    try:
        # sets the primary file for a photo
        api_response = api_instance.photo_primary(uid, fileuid)
        print("The response of PhotosApi->photo_primary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->photo_primary: %s\n" % e)
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

# **photo_unstack**
> EntityPhoto photo_unstack(uid, fileuid)

removes a file from an existing photo stack

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
    api_instance = photoprism_client.PhotosApi(api_client)
    uid = 'uid_example' # str | photo uid
    fileuid = 'fileuid_example' # str | file uid

    try:
        # removes a file from an existing photo stack
        api_response = api_instance.photo_unstack(uid, fileuid)
        print("The response of PhotosApi->photo_unstack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->photo_unstack: %s\n" % e)
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_photo_label**
> EntityPhoto remove_photo_label(uid, id)

removes a label from a photo

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
    api_instance = photoprism_client.PhotosApi(api_client)
    uid = 'uid_example' # str | photo uid
    id = 'id_example' # str | label id

    try:
        # removes a label from a photo
        api_response = api_instance.remove_photo_label(uid, id)
        print("The response of PhotosApi->remove_photo_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->remove_photo_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| photo uid |
 **id** | **str**| label id |

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

# **search_geo**
> List[SearchGeoResult] search_geo(count, quality, offset=offset, public=public, q=q, s=s, path=path, video=video)

finds photos and returns results as JSON, so they can be displayed on a map or in a viewer

### Example


```python
import photoprism_client
from photoprism_client.models.search_geo_result import SearchGeoResult
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
    api_instance = photoprism_client.PhotosApi(api_client)
    count = 56 # int | maximum number of files
    quality = 56 # int | minimum quality score (1-7)
    offset = 56 # int | file offset (optional)
    public = True # bool | excludes private pictures (optional)
    q = 'q_example' # str | search query (optional)
    s = 's_example' # str | album uid (optional)
    path = 'path_example' # str | photo path (optional)
    video = True # bool | is type video (optional)

    try:
        # finds photos and returns results as JSON, so they can be displayed on a map or in a viewer
        api_response = api_instance.search_geo(count, quality, offset=offset, public=public, q=q, s=s, path=path, video=video)
        print("The response of PhotosApi->search_geo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->search_geo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| maximum number of files |
 **quality** | **int**| minimum quality score (1-7) |
 **offset** | **int**| file offset | [optional]
 **public** | **bool**| excludes private pictures | [optional]
 **q** | **str**| search query | [optional]
 **s** | **str**| album uid | [optional]
 **path** | **str**| photo path | [optional]
 **video** | **bool**| is type video | [optional]

### Return type

[**List[SearchGeoResult]**](SearchGeoResult.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_photos**
> List[SearchPhoto] search_photos(count, quality, offset=offset, order=order, merged=merged, public=public, q=q, s=s, path=path, video=video)

finds pictures and returns them as JSON

Fore more information see: - https://docs.photoprism.app/developer-guide/api/search/#get-apiv1photos

### Example


```python
import photoprism_client
from photoprism_client.models.search_photo import SearchPhoto
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
    api_instance = photoprism_client.PhotosApi(api_client)
    count = 56 # int | maximum number of files
    quality = 56 # int | minimum quality score (1-7)
    offset = 56 # int | file offset (optional)
    order = 'order_example' # str | sort order (optional)
    merged = True # bool | groups consecutive files that belong to the same photo (optional)
    public = True # bool | excludes private pictures (optional)
    q = 'q_example' # str | search query (optional)
    s = 's_example' # str | album uid (optional)
    path = 'path_example' # str | photo path (optional)
    video = True # bool | is type video (optional)

    try:
        # finds pictures and returns them as JSON
        api_response = api_instance.search_photos(count, quality, offset=offset, order=order, merged=merged, public=public, q=q, s=s, path=path, video=video)
        print("The response of PhotosApi->search_photos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->search_photos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| maximum number of files |
 **quality** | **int**| minimum quality score (1-7) |
 **offset** | **int**| file offset | [optional]
 **order** | **str**| sort order | [optional]
 **merged** | **bool**| groups consecutive files that belong to the same photo | [optional]
 **public** | **bool**| excludes private pictures | [optional]
 **q** | **str**| search query | [optional]
 **s** | **str**| album uid | [optional]
 **path** | **str**| photo path | [optional]
 **video** | **bool**| is type video | [optional]

### Return type

[**List[SearchPhoto]**](SearchPhoto.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_photo**
> EntityPhoto update_photo(uid, photo)

updates picture details and returns them as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.entity_photo import EntityPhoto
from photoprism_client.models.form_photo import FormPhoto
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
    api_instance = photoprism_client.PhotosApi(api_client)
    uid = 'uid_example' # str | Photo UID
    photo = photoprism_client.FormPhoto() # FormPhoto | properties to be updated (only submit values that should be changed)

    try:
        # updates picture details and returns them as JSON
        api_response = api_instance.update_photo(uid, photo)
        print("The response of PhotosApi->update_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->update_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Photo UID |
 **photo** | [**FormPhoto**](FormPhoto.md)| properties to be updated (only submit values that should be changed) |

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

# **update_photo_label**
> EntityPhoto update_photo_label(uid, id, label)

changes a photo label

### Example


```python
import photoprism_client
from photoprism_client.models.entity_photo import EntityPhoto
from photoprism_client.models.form_label import FormLabel
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
    api_instance = photoprism_client.PhotosApi(api_client)
    uid = 'uid_example' # str | photo uid
    id = 'id_example' # str | label id
    label = photoprism_client.FormLabel() # FormLabel | properties to be updated (currently supports: uncertainty)

    try:
        # changes a photo label
        api_response = api_instance.update_photo_label(uid, id, label)
        print("The response of PhotosApi->update_photo_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->update_photo_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| photo uid |
 **id** | **str**| label id |
 **label** | [**FormLabel**](FormLabel.md)| properties to be updated (currently supports: uncertainty) |

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

