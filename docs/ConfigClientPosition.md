# ConfigClientPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cid** | **str** |  | [optional]
**lat** | **float** |  | [optional]
**lng** | **float** |  | [optional]
**uid** | **str** |  | [optional]
**utc** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.config_client_position import ConfigClientPosition

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClientPosition from a JSON string
config_client_position_instance = ConfigClientPosition.from_json(json)
# print the JSON string representation of the object
print(ConfigClientPosition.to_json())

# convert the object into a dict
config_client_position_dict = config_client_position_instance.to_dict()
# create an instance of ConfigClientPosition from a dict
config_client_position_from_dict = ConfigClientPosition.from_dict(config_client_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


