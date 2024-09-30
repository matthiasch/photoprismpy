# photoprism_client.AlbumsApi

All URIs are relative to *http://demo.photoprism.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_photos_to_album**](AlbumsApi.md#add_photos_to_album) | **POST** /api/v1/albums/{uid}/photos | adds photos to an album
[**album_cover**](AlbumsApi.md#album_cover) | **GET** /api/v1/albums/{uid}/t/{token}/{size} | returns an album cover image
[**batch_albums_delete**](AlbumsApi.md#batch_albums_delete) | **POST** /api/v1/batch/albums/delete | permanently removes multiple albums
[**clone_albums**](AlbumsApi.md#clone_albums) | **POST** /api/v1/albums/{uid}/clone | creates a new album containing pictures from other albums
[**create_album**](AlbumsApi.md#create_album) | **POST** /api/v1/albums | creates a new album
[**create_album_link**](AlbumsApi.md#create_album_link) | **POST** /api/v1/albums/{uid}/links | adds a new album share link and return it as JSON
[**delete_album**](AlbumsApi.md#delete_album) | **DELETE** /api/v1/albums/{uid} | deletes an existing album
[**delete_album_link**](AlbumsApi.md#delete_album_link) | **DELETE** /api/v1/albums/{uid}/links/{linkuid} | deletes an album share link
[**dislike_album**](AlbumsApi.md#dislike_album) | **DELETE** /api/v1/albums/{uid}/like | removes the favorite flag from an album
[**download_album**](AlbumsApi.md#download_album) | **GET** /api/v1/albums/{uid}/dl | streams the album contents as zip archiv
[**get_album**](AlbumsApi.md#get_album) | **GET** /api/v1/albums/{uid} | returns album details as JSON
[**get_album_links**](AlbumsApi.md#get_album_links) | **GET** /api/v1/albums/{uid}/links | returns all share links for the given UID as JSON
[**get_moments_time**](AlbumsApi.md#get_moments_time) | **GET** /api/v1/moments/time | returns monthly albums as JSON
[**like_album**](AlbumsApi.md#like_album) | **POST** /api/v1/albums/{uid}/like | sets the favorite flag for an album
[**remove_photos_from_album**](AlbumsApi.md#remove_photos_from_album) | **DELETE** /api/v1/albums/{uid}/photos | removes photos from an album
[**search_albums**](AlbumsApi.md#search_albums) | **GET** /api/v1/albums | finds albums and returns them as JSON
[**update_album**](AlbumsApi.md#update_album) | **PUT** /api/v1/albums/{uid} | updates album metadata like title and description
[**update_album_link**](AlbumsApi.md#update_album_link) | **PUT** /api/v1/albums/{uid}/links/{linkuid} | updates an album share link and return it as JSON


# **add_photos_to_album**
> Dict[str, object] add_photos_to_album(uid, photos)

adds photos to an album

### Example


```python
import photoprism_client
from photoprism_client.models.form_selection import FormSelection
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
    api_instance = photoprism_client.AlbumsApi(api_client)
    uid = 'uid_example' # str | Album UID
    photos = photoprism_client.FormSelection() # FormSelection | Photo Selection

    try:
        # adds photos to an album
        api_response = api_instance.add_photos_to_album(uid, photos)
        print("The response of AlbumsApi->add_photos_to_album:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->add_photos_to_album: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Album UID |
 **photos** | [**FormSelection**](FormSelection.md)| Photo Selection |

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = photoprism_client.AlbumsApi(api_client)
    uid = 'uid_example' # str | Album UID
    token = 'token_example' # str | user-specific security token provided with session or 'public' when running PhotoPrism in public mode
    size = 'size_example' # str | thumbnail size

    try:
        # returns an album cover image
        api_response = api_instance.album_cover(uid, token, size)
        print("The response of AlbumsApi->album_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->album_cover: %s\n" % e)
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

# **batch_albums_delete**
> I18nResponse batch_albums_delete(albums)

permanently removes multiple albums

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
    api_instance = photoprism_client.AlbumsApi(api_client)
    albums = photoprism_client.FormSelection() # FormSelection | Album Selection

    try:
        # permanently removes multiple albums
        api_response = api_instance.batch_albums_delete(albums)
        print("The response of AlbumsApi->batch_albums_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->batch_albums_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **albums** | [**FormSelection**](FormSelection.md)| Album Selection |

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

# **clone_albums**
> Dict[str, object] clone_albums(uid, albums)

creates a new album containing pictures from other albums

### Example


```python
import photoprism_client
from photoprism_client.models.form_selection import FormSelection
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
    api_instance = photoprism_client.AlbumsApi(api_client)
    uid = 'uid_example' # str | UID of the album to which the pictures are to be added
    albums = photoprism_client.FormSelection() # FormSelection | Album Selection

    try:
        # creates a new album containing pictures from other albums
        api_response = api_instance.clone_albums(uid, albums)
        print("The response of AlbumsApi->clone_albums:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->clone_albums: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| UID of the album to which the pictures are to be added |
 **albums** | [**FormSelection**](FormSelection.md)| Album Selection |

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_album**
> EntityAlbum create_album(album)

creates a new album

### Example


```python
import photoprism_client
from photoprism_client.models.entity_album import EntityAlbum
from photoprism_client.models.form_album import FormAlbum
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
    api_instance = photoprism_client.AlbumsApi(api_client)
    album = photoprism_client.FormAlbum() # FormAlbum | properties of the album to be created (currently supports Title and Favorite)

    try:
        # creates a new album
        api_response = api_instance.create_album(album)
        print("The response of AlbumsApi->create_album:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->create_album: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **album** | [**FormAlbum**](FormAlbum.md)| properties of the album to be created (currently supports Title and Favorite) |

### Return type

[**EntityAlbum**](EntityAlbum.md)

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
    api_instance = photoprism_client.AlbumsApi(api_client)
    uid = 'uid_example' # str | album uid
    link = photoprism_client.FormLink() # FormLink | link properties (currently supported: slug, expires)

    try:
        # adds a new album share link and return it as JSON
        api_response = api_instance.create_album_link(uid, link)
        print("The response of AlbumsApi->create_album_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->create_album_link: %s\n" % e)
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

# **delete_album**
> delete_album(uid)

deletes an existing album

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
    api_instance = photoprism_client.AlbumsApi(api_client)
    uid = 'uid_example' # str | Album UID

    try:
        # deletes an existing album
        api_instance.delete_album(uid)
    except Exception as e:
        print("Exception when calling AlbumsApi->delete_album: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Album UID |

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
    api_instance = photoprism_client.AlbumsApi(api_client)
    uid = 'uid_example' # str | album
    linkuid = 'linkuid_example' # str | link uid

    try:
        # deletes an album share link
        api_response = api_instance.delete_album_link(uid, linkuid)
        print("The response of AlbumsApi->delete_album_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->delete_album_link: %s\n" % e)
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

# **dislike_album**
> dislike_album(uid)

removes the favorite flag from an album

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
    api_instance = photoprism_client.AlbumsApi(api_client)
    uid = 'uid_example' # str | Album UID

    try:
        # removes the favorite flag from an album
        api_instance.dislike_album(uid)
    except Exception as e:
        print("Exception when calling AlbumsApi->dislike_album: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Album UID |

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
    api_instance = photoprism_client.AlbumsApi(api_client)
    uid = 'uid_example' # str | Album UID

    try:
        # streams the album contents as zip archiv
        api_response = api_instance.download_album(uid)
        print("The response of AlbumsApi->download_album:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->download_album: %s\n" % e)
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

# **get_album**
> EntityAlbum get_album(uid)

returns album details as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.entity_album import EntityAlbum
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
    api_instance = photoprism_client.AlbumsApi(api_client)
    uid = 'uid_example' # str | Album UID

    try:
        # returns album details as JSON
        api_response = api_instance.get_album(uid)
        print("The response of AlbumsApi->get_album:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->get_album: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Album UID |

### Return type

[**EntityAlbum**](EntityAlbum.md)

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
    api_instance = photoprism_client.AlbumsApi(api_client)
    uid = 'uid_example' # str | album uid

    try:
        # returns all share links for the given UID as JSON
        api_response = api_instance.get_album_links(uid)
        print("The response of AlbumsApi->get_album_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->get_album_links: %s\n" % e)
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

# **get_moments_time**
> EntityAlbum get_moments_time()

returns monthly albums as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.entity_album import EntityAlbum
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
    api_instance = photoprism_client.AlbumsApi(api_client)

    try:
        # returns monthly albums as JSON
        api_response = api_instance.get_moments_time()
        print("The response of AlbumsApi->get_moments_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->get_moments_time: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EntityAlbum**](EntityAlbum.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **like_album**
> like_album(uid)

sets the favorite flag for an album

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
    api_instance = photoprism_client.AlbumsApi(api_client)
    uid = 'uid_example' # str | Album UID

    try:
        # sets the favorite flag for an album
        api_instance.like_album(uid)
    except Exception as e:
        print("Exception when calling AlbumsApi->like_album: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Album UID |

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

# **remove_photos_from_album**
> Dict[str, object] remove_photos_from_album(uid, photos)

removes photos from an album

### Example


```python
import photoprism_client
from photoprism_client.models.form_selection import FormSelection
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
    api_instance = photoprism_client.AlbumsApi(api_client)
    uid = 'uid_example' # str | Album UID
    photos = photoprism_client.FormSelection() # FormSelection | Photo Selection

    try:
        # removes photos from an album
        api_response = api_instance.remove_photos_from_album(uid, photos)
        print("The response of AlbumsApi->remove_photos_from_album:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->remove_photos_from_album: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Album UID |
 **photos** | [**FormSelection**](FormSelection.md)| Photo Selection |

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_albums**
> List[SearchAlbum] search_albums(count, offset=offset, order=order, q=q)

finds albums and returns them as JSON

### Example


```python
import photoprism_client
from photoprism_client.models.search_album import SearchAlbum
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
    api_instance = photoprism_client.AlbumsApi(api_client)
    count = 56 # int | maximum number of results
    offset = 56 # int | search result offset (optional)
    order = 'order_example' # str | sort order (optional)
    q = 'q_example' # str | search query (optional)

    try:
        # finds albums and returns them as JSON
        api_response = api_instance.search_albums(count, offset=offset, order=order, q=q)
        print("The response of AlbumsApi->search_albums:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->search_albums: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| maximum number of results |
 **offset** | **int**| search result offset | [optional]
 **order** | **str**| sort order | [optional]
 **q** | **str**| search query | [optional]

### Return type

[**List[SearchAlbum]**](SearchAlbum.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_album**
> EntityAlbum update_album(uid, album)

updates album metadata like title and description

### Example


```python
import photoprism_client
from photoprism_client.models.entity_album import EntityAlbum
from photoprism_client.models.form_album import FormAlbum
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
    api_instance = photoprism_client.AlbumsApi(api_client)
    uid = 'uid_example' # str | Album UID
    album = photoprism_client.FormAlbum() # FormAlbum | properties to be updated

    try:
        # updates album metadata like title and description
        api_response = api_instance.update_album(uid, album)
        print("The response of AlbumsApi->update_album:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->update_album: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Album UID |
 **album** | [**FormAlbum**](FormAlbum.md)| properties to be updated |

### Return type

[**EntityAlbum**](EntityAlbum.md)

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
    api_instance = photoprism_client.AlbumsApi(api_client)
    uid = 'uid_example' # str | album uid
    linkuid = 'linkuid_example' # str | link uid
    link = photoprism_client.FormLink() # FormLink | properties to be updated (currently supported: slug, expires, token)

    try:
        # updates an album share link and return it as JSON
        api_response = api_instance.update_album_link(uid, linkuid, link)
        print("The response of AlbumsApi->update_album_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->update_album_link: %s\n" % e)
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

