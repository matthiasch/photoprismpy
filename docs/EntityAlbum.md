# EntityAlbum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | [optional]
**category** | **str** |  | [optional]
**country** | **str** |  | [optional]
**created_at** | **str** |  | [optional]
**created_by** | **str** |  | [optional]
**day** | **int** |  | [optional]
**deleted_at** | **str** |  | [optional]
**description** | **str** |  | [optional]
**favorite** | **bool** |  | [optional]
**filter** | **str** |  | [optional]
**id** | **int** |  | [optional]
**location** | **str** |  | [optional]
**month** | **int** |  | [optional]
**notes** | **str** |  | [optional]
**order** | **str** |  | [optional]
**parent_uid** | **str** |  | [optional]
**path** | **str** |  | [optional]
**private** | **bool** |  | [optional]
**published_at** | **str** |  | [optional]
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
from photoprism_client.models.entity_album import EntityAlbum

# TODO update the JSON string below
json = "{}"
# create an instance of EntityAlbum from a JSON string
entity_album_instance = EntityAlbum.from_json(json)
# print the JSON string representation of the object
print(EntityAlbum.to_json())

# convert the object into a dict
entity_album_dict = entity_album_instance.to_dict()
# create an instance of EntityAlbum from a dict
entity_album_from_dict = EntityAlbum.from_dict(entity_album_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


