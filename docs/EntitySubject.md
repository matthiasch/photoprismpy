# EntitySubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | **str** |  | [optional]
**alias** | **str** |  | [optional]
**bio** | **str** |  | [optional]
**created_at** | **str** |  | [optional]
**deleted_at** | **str** |  | [optional]
**excluded** | **bool** |  | [optional]
**favorite** | **bool** |  | [optional]
**file_count** | **int** |  | [optional]
**hidden** | **bool** |  | [optional]
**name** | **str** |  | [optional]
**notes** | **str** |  | [optional]
**photo_count** | **int** |  | [optional]
**private** | **bool** |  | [optional]
**slug** | **str** |  | [optional]
**src** | **str** |  | [optional]
**thumb** | **str** |  | [optional]
**thumb_src** | **str** |  | [optional]
**type** | **str** |  | [optional]
**uid** | **str** |  | [optional]
**updated_at** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.entity_subject import EntitySubject

# TODO update the JSON string below
json = "{}"
# create an instance of EntitySubject from a JSON string
entity_subject_instance = EntitySubject.from_json(json)
# print the JSON string representation of the object
print(EntitySubject.to_json())

# convert the object into a dict
entity_subject_dict = entity_subject_instance.to_dict()
# create an instance of EntitySubject from a dict
entity_subject_from_dict = EntitySubject.from_dict(entity_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


