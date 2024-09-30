# SearchLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional]
**custom_slug** | **str** |  | [optional]
**deleted_at** | **str** |  | [optional]
**description** | **str** |  | [optional]
**favorite** | **bool** |  | [optional]
**id** | **int** |  | [optional]
**name** | **str** |  | [optional]
**notes** | **str** |  | [optional]
**photo_count** | **int** |  | [optional]
**priority** | **int** |  | [optional]
**slug** | **str** |  | [optional]
**thumb** | **str** |  | [optional]
**thumb_src** | **str** |  | [optional]
**uid** | **str** |  | [optional]
**updated_at** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.search_label import SearchLabel

# TODO update the JSON string below
json = "{}"
# create an instance of SearchLabel from a JSON string
search_label_instance = SearchLabel.from_json(json)
# print the JSON string representation of the object
print(SearchLabel.to_json())

# convert the object into a dict
search_label_dict = search_label_instance.to_dict()
# create an instance of SearchLabel from a dict
search_label_from_dict = SearchLabel.from_dict(search_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


