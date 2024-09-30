# EntityError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional]
**level** | **str** |  | [optional]
**message** | **str** |  | [optional]
**time** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.entity_error import EntityError

# TODO update the JSON string below
json = "{}"
# create an instance of EntityError from a JSON string
entity_error_instance = EntityError.from_json(json)
# print the JSON string representation of the object
print(EntityError.to_json())

# convert the object into a dict
entity_error_dict = entity_error_instance.to_dict()
# create an instance of EntityError from a dict
entity_error_from_dict = EntityError.from_dict(entity_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


