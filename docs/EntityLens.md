# EntityLens


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
from photoprism_client.models.entity_lens import EntityLens

# TODO update the JSON string below
json = "{}"
# create an instance of EntityLens from a JSON string
entity_lens_instance = EntityLens.from_json(json)
# print the JSON string representation of the object
print(EntityLens.to_json())

# convert the object into a dict
entity_lens_dict = entity_lens_instance.to_dict()
# create an instance of EntityLens from a dict
entity_lens_from_dict = EntityLens.from_dict(entity_lens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


