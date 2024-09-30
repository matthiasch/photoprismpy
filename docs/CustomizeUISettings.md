# CustomizeUISettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** |  | [optional]
**scrollbar** | **bool** |  | [optional]
**theme** | **str** |  | [optional]
**time_zone** | **str** |  | [optional]
**zoom** | **bool** |  | [optional]

## Example

```python
from photoprism_client.models.customize_ui_settings import CustomizeUISettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizeUISettings from a JSON string
customize_ui_settings_instance = CustomizeUISettings.from_json(json)
# print the JSON string representation of the object
print(CustomizeUISettings.to_json())

# convert the object into a dict
customize_ui_settings_dict = customize_ui_settings_instance.to_dict()
# create an instance of CustomizeUISettings from a dict
customize_ui_settings_from_dict = CustomizeUISettings.from_dict(customize_ui_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


