# EntityLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional]
**custom_slug** | **str** |  | [optional]
**deleted_at** | **str** |  | [optional]
**description** | **str** |  | [optional]
**favorite** | **bool** |  | [optional]
**id** | **int** |  | [optional]
**name** | **str** |  | [optional]
**notes** | **str** |  | [optional]
**photo_count** | **int** |  | [optional]
**priority** | **int** |  | [optional]
**published_at** | **str** |  | [optional]
**slug** | **str** |  | [optional]
**thumb** | **str** |  | [optional]
**thumb_src** | **str** |  | [optional]
**uid** | **str** |  | [optional]
**updated_at** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.entity_label import EntityLabel

# TODO update the JSON string below
json = "{}"
# create an instance of EntityLabel from a JSON string
entity_label_instance = EntityLabel.from_json(json)
# print the JSON string representation of the object
print(EntityLabel.to_json())

# convert the object into a dict
entity_label_dict = entity_label_instance.to_dict()
# create an instance of EntityLabel from a dict
entity_label_from_dict = EntityLabel.from_dict(entity_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


