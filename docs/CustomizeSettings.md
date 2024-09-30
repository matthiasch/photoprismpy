# CustomizeSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download** | [**CustomizeDownloadSettings**](CustomizeDownloadSettings.md) |  | [optional]
**features** | [**CustomizeFeatureSettings**](CustomizeFeatureSettings.md) |  | [optional]
**var_import** | [**CustomizeImportSettings**](CustomizeImportSettings.md) |  | [optional]
**index** | [**CustomizeIndexSettings**](CustomizeIndexSettings.md) |  | [optional]
**maps** | [**CustomizeMapsSettings**](CustomizeMapsSettings.md) |  | [optional]
**search** | [**CustomizeSearchSettings**](CustomizeSearchSettings.md) |  | [optional]
**share** | [**CustomizeShareSettings**](CustomizeShareSettings.md) |  | [optional]
**stack** | [**CustomizeStackSettings**](CustomizeStackSettings.md) |  | [optional]
**templates** | [**CustomizeTemplateSettings**](CustomizeTemplateSettings.md) |  | [optional]
**ui** | [**CustomizeUISettings**](CustomizeUISettings.md) |  | [optional]

## Example

```python
from photoprism_client.models.customize_settings import CustomizeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizeSettings from a JSON string
customize_settings_instance = CustomizeSettings.from_json(json)
# print the JSON string representation of the object
print(CustomizeSettings.to_json())

# convert the object into a dict
customize_settings_dict = customize_settings_instance.to_dict()
# create an instance of CustomizeSettings from a dict
customize_settings_from_dict = CustomizeSettings.from_dict(customize_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


