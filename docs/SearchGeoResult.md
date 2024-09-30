# SearchGeoResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional]
**favorite** | **bool** |  | [optional]
**hash** | **str** |  | [optional]
**height** | **int** |  | [optional]
**lat** | **float** |  | [optional]
**lng** | **float** |  | [optional]
**taken_at** | **str** |  | [optional]
**taken_at_local** | **str** |  | [optional]
**title** | **str** |  | [optional]
**type** | **str** |  | [optional]
**uid** | **str** |  | [optional]
**width** | **int** |  | [optional]

## Example

```python
from photoprism_client.models.search_geo_result import SearchGeoResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchGeoResult from a JSON string
search_geo_result_instance = SearchGeoResult.from_json(json)
# print the JSON string representation of the object
print(SearchGeoResult.to_json())

# convert the object into a dict
search_geo_result_dict = search_geo_result_instance.to_dict()
# create an instance of SearchGeoResult from a dict
search_geo_result_from_dict = SearchGeoResult.from_dict(search_geo_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


