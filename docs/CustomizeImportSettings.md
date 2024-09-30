# CustomizeImportSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move** | **bool** |  | [optional]
**path** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.customize_import_settings import CustomizeImportSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizeImportSettings from a JSON string
customize_import_settings_instance = CustomizeImportSettings.from_json(json)
# print the JSON string representation of the object
print(CustomizeImportSettings.to_json())

# convert the object into a dict
customize_import_settings_dict = customize_import_settings_instance.to_dict()
# create an instance of CustomizeImportSettings from a dict
customize_import_settings_from_dict = CustomizeImportSettings.from_dict(customize_import_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


