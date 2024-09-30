# CustomizeDownloadSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** |  | [optional]
**media_raw** | **bool** |  | [optional]
**media_sidecar** | **bool** |  | [optional]
**name** | [**CustomizeDownloadName**](CustomizeDownloadName.md) |  | [optional]
**originals** | **bool** |  | [optional]

## Example

```python
from photoprism_client.models.customize_download_settings import CustomizeDownloadSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizeDownloadSettings from a JSON string
customize_download_settings_instance = CustomizeDownloadSettings.from_json(json)
# print the JSON string representation of the object
print(CustomizeDownloadSettings.to_json())

# convert the object into a dict
customize_download_settings_dict = customize_download_settings_instance.to_dict()
# create an instance of CustomizeDownloadSettings from a dict
customize_download_settings_from_dict = CustomizeDownloadSettings.from_dict(customize_download_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


