# CustomizeMapsSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**animate** | **int** |  | [optional]
**style** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.customize_maps_settings import CustomizeMapsSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizeMapsSettings from a JSON string
customize_maps_settings_instance = CustomizeMapsSettings.from_json(json)
# print the JSON string representation of the object
print(CustomizeMapsSettings.to_json())

# convert the object into a dict
customize_maps_settings_dict = customize_maps_settings_instance.to_dict()
# create an instance of CustomizeMapsSettings from a dict
customize_maps_settings_from_dict = CustomizeMapsSettings.from_dict(customize_maps_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


