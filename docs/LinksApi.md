# photoprism_client.LinksApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_entity_uid_links_post**](LinksApi.md#api_v1_entity_uid_links_post) | **POST** /api/v1/{entity}/{uid}/links |
[**create_album_link**](LinksApi.md#create_album_link) | **POST** /api/v1/albums/{uid}/links | adds a new album share link and return it as JSON
[**delete_album_link**](LinksApi.md#delete_album_link) | **DELETE** /api/v1/albums/{uid}/links/{linkuid} | deletes an album share link
[**get_album_links**](LinksApi.md#get_album_links) | **GET** /api/v1/albums/{uid}/links | returns all share links for the given UID as JSON
[**update_album_link**](LinksApi.md#update_album_link) | **PUT** /api/v1/albums/{uid}/links/{linkuid} | updates an album share link and return it as JSON


# **api_v1_entity_uid_links_post**
> api_v1_entity_uid_links_post()



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
    api_instance = photoprism_client.LinksApi(api_client)

    try:
        api_instance.api_v1_entity_uid_links_post()
    except Exception as e:
        print("Exception when calling LinksApi->api_v1_entity_uid_links_post: %s\n" % e)
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

# **create_album_link**
> EntityLink create_album_link(uid, link)

adds a new album share link and return it as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.entity_link import EntityLink
from photoprism_client.models.form_link import FormLink
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
    api_instance = photoprism_client.LinksApi(api_client)
    uid = 'uid_example' # str | album uid
    link = photoprism_client.FormLink() # FormLink | link properties (currently supported: slug, expires)

    try:
        # adds a new album share link and return it as JSON
        api_response = api_instance.create_album_link(uid, link)
        print("The response of LinksApi->create_album_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->create_album_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| album uid |
 **link** | [**FormLink**](FormLink.md)| link properties (currently supported: slug, expires) |

### Return type

[**EntityLink**](EntityLink.md)

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
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_album_link**
> EntityLink delete_album_link(uid, linkuid)

deletes an album share link

### Example


```python
import photoprism_client
from photoprism_client.models.entity_link import EntityLink
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
    api_instance = photoprism_client.LinksApi(api_client)
    uid = 'uid_example' # str | album
    linkuid = 'linkuid_example' # str | link uid

    try:
        # deletes an album share link
        api_response = api_instance.delete_album_link(uid, linkuid)
        print("The response of LinksApi->delete_album_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->delete_album_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| album |
 **linkuid** | **str**| link uid |

### Return type

[**EntityLink**](EntityLink.md)

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
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_album_links**
> EntityLink get_album_links(uid)

returns all share links for the given UID as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.entity_link import EntityLink
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
    api_instance = photoprism_client.LinksApi(api_client)
    uid = 'uid_example' # str | album uid

    try:
        # returns all share links for the given UID as JSON
        api_response = api_instance.get_album_links(uid)
        print("The response of LinksApi->get_album_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->get_album_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| album uid |

### Return type

[**EntityLink**](EntityLink.md)

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

# **update_album_link**
> EntityLink update_album_link(uid, linkuid, link)

updates an album share link and return it as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.entity_link import EntityLink
from photoprism_client.models.form_link import FormLink
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
    api_instance = photoprism_client.LinksApi(api_client)
    uid = 'uid_example' # str | album uid
    linkuid = 'linkuid_example' # str | link uid
    link = photoprism_client.FormLink() # FormLink | properties to be updated (currently supported: slug, expires, token)

    try:
        # updates an album share link and return it as JSON
        api_response = api_instance.update_album_link(uid, linkuid, link)
        print("The response of LinksApi->update_album_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->update_album_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| album uid |
 **linkuid** | **str**| link uid |
 **link** | [**FormLink**](FormLink.md)| properties to be updated (currently supported: slug, expires, token) |

### Return type

[**EntityLink**](EntityLink.md)

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
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

