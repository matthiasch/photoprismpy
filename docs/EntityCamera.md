# EntityCamera


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional]
**id** | **int** |  | [optional]
**make** | **str** |  | [optional]
**model** | **str** |  | [optional]
**name** | **str** |  | [optional]
**notes** | **str** |  | [optional]
**slug** | **str** |  | [optional]
**type** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.entity_camera import EntityCamera

# TODO update the JSON string below
json = "{}"
# create an instance of EntityCamera from a JSON string
entity_camera_instance = EntityCamera.from_json(json)
# print the JSON string representation of the object
print(EntityCamera.to_json())

# convert the object into a dict
entity_camera_dict = entity_camera_instance.to_dict()
# create an instance of EntityCamera from a dict
entity_camera_from_dict = EntityCamera.from_dict(entity_camera_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


