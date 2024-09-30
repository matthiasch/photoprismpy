# SearchAlbum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | [optional]
**category** | **str** |  | [optional]
**country** | **str** |  | [optional]
**created_at** | **str** |  | [optional]
**day** | **int** |  | [optional]
**deleted_at** | **str** |  | [optional]
**description** | **str** |  | [optional]
**favorite** | **bool** |  | [optional]
**filter** | **str** |  | [optional]
**link_count** | **int** |  | [optional]
**location** | **str** |  | [optional]
**month** | **int** |  | [optional]
**notes** | **str** |  | [optional]
**order** | **str** |  | [optional]
**parent_uid** | **str** |  | [optional]
**path** | **str** |  | [optional]
**photo_count** | **int** |  | [optional]
**private** | **bool** |  | [optional]
**slug** | **str** |  | [optional]
**state** | **str** |  | [optional]
**template** | **str** |  | [optional]
**thumb** | **str** |  | [optional]
**thumb_src** | **str** |  | [optional]
**title** | **str** |  | [optional]
**type** | **str** |  | [optional]
**uid** | **str** |  | [optional]
**updated_at** | **str** |  | [optional]
**year** | **int** |  | [optional]

## Example

```python
from photoprism_client.models.search_album import SearchAlbum

# TODO update the JSON string below
json = "{}"
# create an instance of SearchAlbum from a JSON string
search_album_instance = SearchAlbum.from_json(json)
# print the JSON string representation of the object
print(SearchAlbum.to_json())

# convert the object into a dict
search_album_dict = search_album_instance.to_dict()
# create an instance of SearchAlbum from a dict
search_album_from_dict = SearchAlbum.from_dict(search_album_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


