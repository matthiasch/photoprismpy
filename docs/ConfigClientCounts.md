# ConfigClientCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**albums** | **int** |  | [optional]
**all** | **int** |  | [optional]
**archived** | **int** |  | [optional]
**cameras** | **int** |  | [optional]
**countries** | **int** |  | [optional]
**favorites** | **int** |  | [optional]
**files** | **int** |  | [optional]
**folders** | **int** |  | [optional]
**hidden** | **int** |  | [optional]
**label_max_photos** | **int** |  | [optional]
**labels** | **int** |  | [optional]
**lenses** | **int** |  | [optional]
**live** | **int** |  | [optional]
**moments** | **int** |  | [optional]
**months** | **int** |  | [optional]
**people** | **int** |  | [optional]
**photos** | **int** |  | [optional]
**places** | **int** |  | [optional]
**private** | **int** |  | [optional]
**private_albums** | **int** |  | [optional]
**private_folders** | **int** |  | [optional]
**private_moments** | **int** |  | [optional]
**private_months** | **int** |  | [optional]
**private_states** | **int** |  | [optional]
**review** | **int** |  | [optional]
**states** | **int** |  | [optional]
**stories** | **int** |  | [optional]
**videos** | **int** |  | [optional]

## Example

```python
from photoprism_client.models.config_client_counts import ConfigClientCounts

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClientCounts from a JSON string
config_client_counts_instance = ConfigClientCounts.from_json(json)
# print the JSON string representation of the object
print(ConfigClientCounts.to_json())

# convert the object into a dict
config_client_counts_dict = config_client_counts_instance.to_dict()
# create an instance of ConfigClientCounts from a dict
config_client_counts_from_dict = ConfigClientCounts.from_dict(config_client_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


