# photoprism_client.LabelsApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_photo_label**](LabelsApi.md#add_photo_label) | **POST** /api/v1/photos/{uid}/label | adds a label to a photo
[**batch_labels_delete**](LabelsApi.md#batch_labels_delete) | **POST** /api/v1/batch/labels/delete | deletes multiple labels
[**dislike_label**](LabelsApi.md#dislike_label) | **DELETE** /api/v1/labels/{uid}/like | removes favorite flag from a label
[**label_cover**](LabelsApi.md#label_cover) | **GET** /api/v1/labels/{uid}/t/{token}/{size} | returns a label cover image
[**like_label**](LabelsApi.md#like_label) | **POST** /api/v1/labels/{uid}/like | sets favorite flag for a label
[**remove_photo_label**](LabelsApi.md#remove_photo_label) | **DELETE** /api/v1/photos/{uid}/label/{id} | removes a label from a photo
[**search_labels**](LabelsApi.md#search_labels) | **GET** /api/v1/labels | finds and returns labels as JSON
[**update_label**](LabelsApi.md#update_label) | **PUT** /api/v1/labels/{uid} | updates label name
[**update_photo_label**](LabelsApi.md#update_photo_label) | **PUT** /api/v1/photos/{uid}/label/{id} | changes a photo label


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
    api_instance = photoprism_client.LabelsApi(api_client)
    uid = 'uid_example' # str | photo uid
    label = photoprism_client.FormLabel() # FormLabel | label properties

    try:
        # adds a label to a photo
        api_response = api_instance.add_photo_label(uid, label)
        print("The response of LabelsApi->add_photo_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->add_photo_label: %s\n" % e)
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

# **batch_labels_delete**
> I18nResponse batch_labels_delete(labels)

deletes multiple labels

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
    api_instance = photoprism_client.LabelsApi(api_client)
    labels = photoprism_client.FormSelection() # FormSelection | Label Selection

    try:
        # deletes multiple labels
        api_response = api_instance.batch_labels_delete(labels)
        print("The response of LabelsApi->batch_labels_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->batch_labels_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labels** | [**FormSelection**](FormSelection.md)| Label Selection |

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dislike_label**
> dislike_label(uid)

removes favorite flag from a label

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
    api_instance = photoprism_client.LabelsApi(api_client)
    uid = 'uid_example' # str | Label UID

    try:
        # removes favorite flag from a label
        api_instance.dislike_label(uid)
    except Exception as e:
        print("Exception when calling LabelsApi->dislike_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Label UID |

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
    api_instance = photoprism_client.LabelsApi(api_client)
    uid = 'uid_example' # str | Label UID
    token = 'token_example' # str | user-specific security token provided with session or 'public' when running PhotoPrism in public mode
    size = 'size_example' # str | thumbnail size

    try:
        # returns a label cover image
        api_response = api_instance.label_cover(uid, token, size)
        print("The response of LabelsApi->label_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->label_cover: %s\n" % e)
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

# **like_label**
> like_label(uid)

sets favorite flag for a label

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
    api_instance = photoprism_client.LabelsApi(api_client)
    uid = 'uid_example' # str | Label UID

    try:
        # sets favorite flag for a label
        api_instance.like_label(uid)
    except Exception as e:
        print("Exception when calling LabelsApi->like_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Label UID |

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
    api_instance = photoprism_client.LabelsApi(api_client)
    uid = 'uid_example' # str | photo uid
    id = 'id_example' # str | label id

    try:
        # removes a label from a photo
        api_response = api_instance.remove_photo_label(uid, id)
        print("The response of LabelsApi->remove_photo_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->remove_photo_label: %s\n" % e)
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

# **search_labels**
> SearchLabel search_labels(count, offset=offset, all=all, q=q)

finds and returns labels as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.search_label import SearchLabel
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
    api_instance = photoprism_client.LabelsApi(api_client)
    count = 56 # int | maximum number of results
    offset = 56 # int | search result offset (optional)
    all = True # bool | show all (optional)
    q = 'q_example' # str | search query (optional)

    try:
        # finds and returns labels as JSON
        api_response = api_instance.search_labels(count, offset=offset, all=all, q=q)
        print("The response of LabelsApi->search_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->search_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| maximum number of results |
 **offset** | **int**| search result offset | [optional]
 **all** | **bool**| show all | [optional]
 **q** | **str**| search query | [optional]

### Return type

[**SearchLabel**](SearchLabel.md)

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

# **update_label**
> EntityLabel update_label(uid, label)

updates label name

### Example


```python
import photoprism_client
from photoprism_client.models.entity_label import EntityLabel
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
    api_instance = photoprism_client.LabelsApi(api_client)
    uid = 'uid_example' # str | Label UID
    label = photoprism_client.FormLabel() # FormLabel | Label Name

    try:
        # updates label name
        api_response = api_instance.update_label(uid, label)
        print("The response of LabelsApi->update_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->update_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Label UID |
 **label** | [**FormLabel**](FormLabel.md)| Label Name |

### Return type

[**EntityLabel**](EntityLabel.md)

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
    api_instance = photoprism_client.LabelsApi(api_client)
    uid = 'uid_example' # str | photo uid
    id = 'id_example' # str | label id
    label = photoprism_client.FormLabel() # FormLabel | properties to be updated (currently supports: uncertainty)

    try:
        # changes a photo label
        api_response = api_instance.update_photo_label(uid, id, label)
        print("The response of LabelsApi->update_photo_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->update_photo_label: %s\n" % e)
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

