# FormAlbum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | [optional]
**category** | **str** |  | [optional]
**country** | **str** |  | [optional]
**description** | **str** |  | [optional]
**favorite** | **bool** |  | [optional]
**filter** | **str** |  | [optional]
**location** | **str** |  | [optional]
**notes** | **str** |  | [optional]
**order** | **str** |  | [optional]
**private** | **bool** |  | [optional]
**template** | **str** |  | [optional]
**thumb** | **str** |  | [optional]
**thumb_src** | **str** |  | [optional]
**title** | **str** |  | [optional]
**type** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.form_album import FormAlbum

# TODO update the JSON string below
json = "{}"
# create an instance of FormAlbum from a JSON string
form_album_instance = FormAlbum.from_json(json)
# print the JSON string representation of the object
print(FormAlbum.to_json())

# convert the object into a dict
form_album_dict = form_album_instance.to_dict()
# create an instance of FormAlbum from a dict
form_album_from_dict = FormAlbum.from_dict(form_album_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


