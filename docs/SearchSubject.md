# SearchSubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional]
**excluded** | **bool** |  | [optional]
**favorite** | **bool** |  | [optional]
**file_count** | **int** |  | [optional]
**hidden** | **bool** |  | [optional]
**marker_src** | **str** |  | [optional]
**marker_uid** | **str** |  | [optional]
**name** | **str** |  | [optional]
**photo_count** | **int** |  | [optional]
**private** | **bool** |  | [optional]
**slug** | **str** |  | [optional]
**thumb** | **str** |  | [optional]
**thumb_src** | **str** |  | [optional]
**type** | **str** |  | [optional]
**uid** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.search_subject import SearchSubject

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSubject from a JSON string
search_subject_instance = SearchSubject.from_json(json)
# print the JSON string representation of the object
print(SearchSubject.to_json())

# convert the object into a dict
search_subject_dict = search_subject_instance.to_dict()
# create an instance of SearchSubject from a dict
search_subject_from_dict = SearchSubject.from_dict(search_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


