# EntityLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional]
**created_at** | **str** |  | [optional]
**created_by** | **str** |  | [optional]
**expires** | **int** |  | [optional]
**max_views** | **int** |  | [optional]
**modified_at** | **str** |  | [optional]
**perm** | **int** |  | [optional]
**share_uid** | **str** |  | [optional]
**slug** | **str** |  | [optional]
**token** | **str** |  | [optional]
**uid** | **str** |  | [optional]
**verify_password** | **bool** |  | [optional]
**views** | **int** |  | [optional]

## Example

```python
from photoprism_client.models.entity_link import EntityLink

# TODO update the JSON string below
json = "{}"
# create an instance of EntityLink from a JSON string
entity_link_instance = EntityLink.from_json(json)
# print the JSON string representation of the object
print(EntityLink.to_json())

# convert the object into a dict
entity_link_dict = entity_link_instance.to_dict()
# create an instance of EntityLink from a dict
entity_link_from_dict = EntityLink.from_dict(entity_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


