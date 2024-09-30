# SearchFace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collision_radius** | **float** |  | [optional]
**collisions** | **int** |  | [optional]
**created_at** | **str** |  | [optional]
**face_dist** | **float** |  | [optional]
**file_uid** | **str** |  | [optional]
**hidden** | **bool** |  | [optional]
**id** | **str** |  | [optional]
**invalid** | **bool** |  | [optional]
**marker_uid** | **str** |  | [optional]
**matched_at** | **str** |  | [optional]
**name** | **str** |  | [optional]
**review** | **bool** |  | [optional]
**sample_radius** | **float** |  | [optional]
**samples** | **int** |  | [optional]
**score** | **int** |  | [optional]
**size** | **int** |  | [optional]
**src** | **str** |  | [optional]
**subj_src** | **str** |  | [optional]
**subj_uid** | **str** |  | [optional]
**thumb** | **str** |  | [optional]
**updated_at** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.search_face import SearchFace

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFace from a JSON string
search_face_instance = SearchFace.from_json(json)
# print the JSON string representation of the object
print(SearchFace.to_json())

# convert the object into a dict
search_face_dict = search_face_instance.to_dict()
# create an instance of SearchFace from a dict
search_face_from_dict = SearchFace.from_dict(search_face_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


