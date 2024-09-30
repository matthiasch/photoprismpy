# CustomizeFeatureSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **bool** |  | [optional]
**albums** | **bool** |  | [optional]
**archive** | **bool** |  | [optional]
**delete** | **bool** |  | [optional]
**download** | **bool** |  | [optional]
**edit** | **bool** |  | [optional]
**estimates** | **bool** |  | [optional]
**favorites** | **bool** |  | [optional]
**files** | **bool** |  | [optional]
**folders** | **bool** |  | [optional]
**var_import** | **bool** |  | [optional]
**labels** | **bool** |  | [optional]
**library** | **bool** |  | [optional]
**logs** | **bool** |  | [optional]
**moments** | **bool** |  | [optional]
**people** | **bool** |  | [optional]
**places** | **bool** |  | [optional]
**private** | **bool** |  | [optional]
**ratings** | **bool** |  | [optional]
**reactions** | **bool** |  | [optional]
**review** | **bool** |  | [optional]
**search** | **bool** |  | [optional]
**services** | **bool** |  | [optional]
**settings** | **bool** |  | [optional]
**share** | **bool** |  | [optional]
**upload** | **bool** |  | [optional]
**videos** | **bool** |  | [optional]

## Example

```python
from photoprism_client.models.customize_feature_settings import CustomizeFeatureSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizeFeatureSettings from a JSON string
customize_feature_settings_instance = CustomizeFeatureSettings.from_json(json)
# print the JSON string representation of the object
print(CustomizeFeatureSettings.to_json())

# convert the object into a dict
customize_feature_settings_dict = customize_feature_settings_instance.to_dict()
# create an instance of CustomizeFeatureSettings from a dict
customize_feature_settings_from_dict = CustomizeFeatureSettings.from_dict(customize_feature_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


