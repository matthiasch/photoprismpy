# EntityCountry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional]
**id** | **str** |  | [optional]
**name** | **str** |  | [optional]
**notes** | **str** |  | [optional]
**slug** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.entity_country import EntityCountry

# TODO update the JSON string below
json = "{}"
# create an instance of EntityCountry from a JSON string
entity_country_instance = EntityCountry.from_json(json)
# print the JSON string representation of the object
print(EntityCountry.to_json())

# convert the object into a dict
entity_country_dict = entity_country_instance.to_dict()
# create an instance of EntityCountry from a dict
entity_country_from_dict = EntityCountry.from_dict(entity_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


