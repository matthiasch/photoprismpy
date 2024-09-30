# EntityPlace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional]
**country** | **str** |  | [optional]
**created_at** | **str** |  | [optional]
**district** | **str** |  | [optional]
**favorite** | **bool** |  | [optional]
**keywords** | **str** |  | [optional]
**label** | **str** |  | [optional]
**photo_count** | **int** |  | [optional]
**place_id** | **str** |  | [optional]
**state** | **str** |  | [optional]
**updated_at** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.entity_place import EntityPlace

# TODO update the JSON string below
json = "{}"
# create an instance of EntityPlace from a JSON string
entity_place_instance = EntityPlace.from_json(json)
# print the JSON string representation of the object
print(EntityPlace.to_json())

# convert the object into a dict
entity_place_dict = entity_place_instance.to_dict()
# create an instance of EntityPlace from a dict
entity_place_from_dict = EntityPlace.from_dict(entity_place_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


