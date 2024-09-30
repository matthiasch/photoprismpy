# EnvResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cores** | **int** |  | [optional]
**memory** | [**EnvResourcesMemory**](EnvResourcesMemory.md) |  | [optional]
**routines** | **int** |  | [optional]

## Example

```python
from photoprism_client.models.env_resources import EnvResources

# TODO update the JSON string below
json = "{}"
# create an instance of EnvResources from a JSON string
env_resources_instance = EnvResources.from_json(json)
# print the JSON string representation of the object
print(EnvResources.to_json())

# convert the object into a dict
env_resources_dict = env_resources_instance.to_dict()
# create an instance of EnvResources from a dict
env_resources_from_dict = EnvResources.from_dict(env_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


