# ConfigClientDisable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backups** | **bool** |  | [optional]
**classification** | **bool** |  | [optional]
**darktable** | **bool** |  | [optional]
**exiftool** | **bool** |  | [optional]
**faces** | **bool** |  | [optional]
**ffmpeg** | **bool** |  | [optional]
**heifconvert** | **bool** |  | [optional]
**imagemagick** | **bool** |  | [optional]
**jpegxl** | **bool** |  | [optional]
**places** | **bool** |  | [optional]
**raw** | **bool** |  | [optional]
**rawtherapee** | **bool** |  | [optional]
**restart** | **bool** |  | [optional]
**settings** | **bool** |  | [optional]
**sips** | **bool** |  | [optional]
**tensorflow** | **bool** |  | [optional]
**vectors** | **bool** |  | [optional]
**vips** | **bool** |  | [optional]
**webdav** | **bool** |  | [optional]

## Example

```python
from photoprism_client.models.config_client_disable import ConfigClientDisable

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClientDisable from a JSON string
config_client_disable_instance = ConfigClientDisable.from_json(json)
# print the JSON string representation of the object
print(ConfigClientDisable.to_json())

# convert the object into a dict
config_client_disable_dict = config_client_disable_instance.to_dict()
# create an instance of ConfigClientDisable from a dict
config_client_disable_from_dict = ConfigClientDisable.from_dict(config_client_disable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


