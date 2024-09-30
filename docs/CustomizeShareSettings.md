# CustomizeShareSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.customize_share_settings import CustomizeShareSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizeShareSettings from a JSON string
customize_share_settings_instance = CustomizeShareSettings.from_json(json)
# print the JSON string representation of the object
print(CustomizeShareSettings.to_json())

# convert the object into a dict
customize_share_settings_dict = customize_share_settings_instance.to_dict()
# create an instance of CustomizeShareSettings from a dict
customize_share_settings_from_dict = CustomizeShareSettings.from_dict(customize_share_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


