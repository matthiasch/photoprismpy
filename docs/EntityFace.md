# EntityFace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collision_radius** | **float** |  | [optional]
**collisions** | **int** |  | [optional]
**created_at** | **str** |  | [optional]
**hidden** | **bool** |  | [optional]
**id** | **str** |  | [optional]
**kind** | **int** |  | [optional]
**matched_at** | **str** |  | [optional]
**sample_radius** | **float** |  | [optional]
**samples** | **int** |  | [optional]
**src** | **str** |  | [optional]
**subj_uid** | **str** |  | [optional]
**updated_at** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.entity_face import EntityFace

# TODO update the JSON string below
json = "{}"
# create an instance of EntityFace from a JSON string
entity_face_instance = EntityFace.from_json(json)
# print the JSON string representation of the object
print(EntityFace.to_json())

# convert the object into a dict
entity_face_dict = entity_face_instance.to_dict()
# create an instance of EntityFace from a dict
entity_face_from_dict = EntityFace.from_dict(entity_face_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


