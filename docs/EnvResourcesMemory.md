# EnvResourcesMemory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free** | **int** |  | [optional]
**info** | **str** |  | [optional]
**reserved** | **int** |  | [optional]
**total** | **int** |  | [optional]
**used** | **int** |  | [optional]

## Example

```python
from photoprism_client.models.env_resources_memory import EnvResourcesMemory

# TODO update the JSON string below
json = "{}"
# create an instance of EnvResourcesMemory from a JSON string
env_resources_memory_instance = EnvResourcesMemory.from_json(json)
# print the JSON string representation of the object
print(EnvResourcesMemory.to_json())

# convert the object into a dict
env_resources_memory_dict = env_resources_memory_instance.to_dict()
# create an instance of EnvResourcesMemory from a dict
env_resources_memory_from_dict = EnvResourcesMemory.from_dict(env_resources_memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


