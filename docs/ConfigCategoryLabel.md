# ConfigCategoryLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional]
**slug** | **str** |  | [optional]
**uid** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.config_category_label import ConfigCategoryLabel

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigCategoryLabel from a JSON string
config_category_label_instance = ConfigCategoryLabel.from_json(json)
# print the JSON string representation of the object
print(ConfigCategoryLabel.to_json())

# convert the object into a dict
config_category_label_dict = config_category_label_instance.to_dict()
# create an instance of ConfigCategoryLabel from a dict
config_category_label_from_dict = ConfigCategoryLabel.from_dict(config_category_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


