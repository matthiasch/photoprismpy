# CustomizeIndexSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**convert** | **bool** |  | [optional]
**path** | **str** |  | [optional]
**rescan** | **bool** |  | [optional]
**skip_archived** | **bool** |  | [optional]

## Example

```python
from photoprism_client.models.customize_index_settings import CustomizeIndexSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizeIndexSettings from a JSON string
customize_index_settings_instance = CustomizeIndexSettings.from_json(json)
# print the JSON string representation of the object
print(CustomizeIndexSettings.to_json())

# convert the object into a dict
customize_index_settings_dict = customize_index_settings_instance.to_dict()
# create an instance of CustomizeIndexSettings from a dict
customize_index_settings_from_dict = CustomizeIndexSettings.from_dict(customize_index_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


