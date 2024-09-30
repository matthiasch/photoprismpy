# EntityCell


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional]
**created_at** | **str** |  | [optional]
**id** | **str** |  | [optional]
**name** | **str** |  | [optional]
**place** | [**EntityPlace**](EntityPlace.md) |  | [optional]
**postcode** | **str** |  | [optional]
**street** | **str** |  | [optional]
**updated_at** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.entity_cell import EntityCell

# TODO update the JSON string below
json = "{}"
# create an instance of EntityCell from a JSON string
entity_cell_instance = EntityCell.from_json(json)
# print the JSON string representation of the object
print(EntityCell.to_json())

# convert the object into a dict
entity_cell_dict = entity_cell_instance.to_dict()
# create an instance of EntityCell from a dict
entity_cell_from_dict = EntityCell.from_dict(entity_cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


