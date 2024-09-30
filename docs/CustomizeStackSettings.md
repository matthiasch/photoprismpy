# CustomizeStackSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | **bool** |  | [optional]
**name** | **bool** |  | [optional]
**uuid** | **bool** |  | [optional]

## Example

```python
from photoprism_client.models.customize_stack_settings import CustomizeStackSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizeStackSettings from a JSON string
customize_stack_settings_instance = CustomizeStackSettings.from_json(json)
# print the JSON string representation of the object
print(CustomizeStackSettings.to_json())

# convert the object into a dict
customize_stack_settings_dict = customize_stack_settings_instance.to_dict()
# create an instance of CustomizeStackSettings from a dict
customize_stack_settings_from_dict = CustomizeStackSettings.from_dict(customize_stack_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


