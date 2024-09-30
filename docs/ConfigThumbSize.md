# ConfigThumbSize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**h** | **int** |  | [optional]
**size** | **str** |  | [optional]
**usage** | **str** |  | [optional]
**w** | **int** |  | [optional]

## Example

```python
from photoprism_client.models.config_thumb_size import ConfigThumbSize

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigThumbSize from a JSON string
config_thumb_size_instance = ConfigThumbSize.from_json(json)
# print the JSON string representation of the object
print(ConfigThumbSize.to_json())

# convert the object into a dict
config_thumb_size_dict = config_thumb_size_instance.to_dict()
# create an instance of ConfigThumbSize from a dict
config_thumb_size_from_dict = ConfigThumbSize.from_dict(config_thumb_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


