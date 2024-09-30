# CustomizeSearchSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_size** | **int** |  | [optional]

## Example

```python
from photoprism_client.models.customize_search_settings import CustomizeSearchSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizeSearchSettings from a JSON string
customize_search_settings_instance = CustomizeSearchSettings.from_json(json)
# print the JSON string representation of the object
print(CustomizeSearchSettings.to_json())

# convert the object into a dict
customize_search_settings_dict = customize_search_settings_instance.to_dict()
# create an instance of CustomizeSearchSettings from a dict
customize_search_settings_from_dict = CustomizeSearchSettings.from_dict(customize_search_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


