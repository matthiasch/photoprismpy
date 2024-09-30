# photoprism_client.SubjectsApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_marker_subject**](SubjectsApi.md#clear_marker_subject) | **DELETE** /api/v1/markers/{uid}/subject | removes an existing marker subject association
[**dislike_subject**](SubjectsApi.md#dislike_subject) | **DELETE** /api/v1/subjects/{uid}/like | removes the favorite flag from a subject
[**get_subject**](SubjectsApi.md#get_subject) | **GET** /api/v1/subjects/{uid} | returns a subject as JSON
[**like_subject**](SubjectsApi.md#like_subject) | **POST** /api/v1/subjects/{uid}/like | flags a subject as favorite
[**search_subjects**](SubjectsApi.md#search_subjects) | **GET** /api/v1/subjects | finds and returns subjects as JSON
[**update_marker**](SubjectsApi.md#update_marker) | **PUT** /api/v1/markers/{uid} | updates an existing file area marker to assign faces or other subjects
[**update_subject**](SubjectsApi.md#update_subject) | **PUT** /api/v1/subjects/{uid} | updates subject properties


# **clear_marker_subject**
> EntityMarker clear_marker_subject(uid)

removes an existing marker subject association

### Example


```python
import photoprism_client
from photoprism_client.models.entity_marker import EntityMarker
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
    api_instance = photoprism_client.SubjectsApi(api_client)
    uid = 'uid_example' # str | marker uid

    try:
        # removes an existing marker subject association
        api_response = api_instance.clear_marker_subject(uid)
        print("The response of SubjectsApi->clear_marker_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsApi->clear_marker_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| marker uid |

### Return type

[**EntityMarker**](EntityMarker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dislike_subject**
> dislike_subject(uid)

removes the favorite flag from a subject

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
    api_instance = photoprism_client.SubjectsApi(api_client)
    uid = 'uid_example' # str | subject uid

    try:
        # removes the favorite flag from a subject
        api_instance.dislike_subject(uid)
    except Exception as e:
        print("Exception when calling SubjectsApi->dislike_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| subject uid |

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

# **get_subject**
> EntitySubject get_subject(uid)

returns a subject as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.entity_subject import EntitySubject
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
    api_instance = photoprism_client.SubjectsApi(api_client)
    uid = 'uid_example' # str | subject uid

    try:
        # returns a subject as JSON
        api_response = api_instance.get_subject(uid)
        print("The response of SubjectsApi->get_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsApi->get_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| subject uid |

### Return type

[**EntitySubject**](EntitySubject.md)

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

# **like_subject**
> like_subject(uid)

flags a subject as favorite

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
    api_instance = photoprism_client.SubjectsApi(api_client)
    uid = 'uid_example' # str | subject uid

    try:
        # flags a subject as favorite
        api_instance.like_subject(uid)
    except Exception as e:
        print("Exception when calling SubjectsApi->like_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| subject uid |

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

# **search_subjects**
> List[SearchSubject] search_subjects(count, offset=offset, order=order, hidden=hidden, files=files, q=q)

finds and returns subjects as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.search_subject import SearchSubject
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
    api_instance = photoprism_client.SubjectsApi(api_client)
    count = 56 # int | maximum number of results
    offset = 56 # int | search result offset (optional)
    order = 'order_example' # str | sort order (optional)
    hidden = 'hidden_example' # str | show hidden (optional)
    files = 56 # int | minimum number of files (optional)
    q = 'q_example' # str | search query (optional)

    try:
        # finds and returns subjects as JSON
        api_response = api_instance.search_subjects(count, offset=offset, order=order, hidden=hidden, files=files, q=q)
        print("The response of SubjectsApi->search_subjects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsApi->search_subjects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| maximum number of results |
 **offset** | **int**| search result offset | [optional]
 **order** | **str**| sort order | [optional]
 **hidden** | **str**| show hidden | [optional]
 **files** | **int**| minimum number of files | [optional]
 **q** | **str**| search query | [optional]

### Return type

[**List[SearchSubject]**](SearchSubject.md)

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

# **update_marker**
> EntityMarker update_marker(uid, marker)

updates an existing file area marker to assign faces or other subjects

### Example


```python
import photoprism_client
from photoprism_client.models.entity_marker import EntityMarker
from photoprism_client.models.form_marker import FormMarker
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
    api_instance = photoprism_client.SubjectsApi(api_client)
    uid = 'uid_example' # str | marker uid
    marker = photoprism_client.FormMarker() # FormMarker | properties to be updated

    try:
        # updates an existing file area marker to assign faces or other subjects
        api_response = api_instance.update_marker(uid, marker)
        print("The response of SubjectsApi->update_marker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsApi->update_marker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| marker uid |
 **marker** | [**FormMarker**](FormMarker.md)| properties to be updated |

### Return type

[**EntityMarker**](EntityMarker.md)

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
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subject**
> EntitySubject update_subject(uid, subject)

updates subject properties

### Example


```python
import photoprism_client
from photoprism_client.models.entity_subject import EntitySubject
from photoprism_client.models.form_subject import FormSubject
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
    api_instance = photoprism_client.SubjectsApi(api_client)
    uid = 'uid_example' # str | subject uid
    subject = photoprism_client.FormSubject() # FormSubject | properties to be updated (only submit values that should be changed)

    try:
        # updates subject properties
        api_response = api_instance.update_subject(uid, subject)
        print("The response of SubjectsApi->update_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsApi->update_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| subject uid |
 **subject** | [**FormSubject**](FormSubject.md)| properties to be updated (only submit values that should be changed) |

### Return type

[**EntitySubject**](EntitySubject.md)

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

