# EntityPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional]
**favorite** | **bool** |  | [optional]
**hidden** | **bool** |  | [optional]
**name** | **str** |  | [optional]
**uid** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.entity_person import EntityPerson

# TODO update the JSON string below
json = "{}"
# create an instance of EntityPerson from a JSON string
entity_person_instance = EntityPerson.from_json(json)
# print the JSON string representation of the object
print(EntityPerson.to_json())

# convert the object into a dict
entity_person_dict = entity_person_instance.to_dict()
# create an instance of EntityPerson from a dict
entity_person_from_dict = EntityPerson.from_dict(entity_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


