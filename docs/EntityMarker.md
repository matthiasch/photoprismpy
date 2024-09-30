# EntityMarker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**face_dist** | **float** |  | [optional]
**face_id** | **str** |  | [optional]
**file_uid** | **str** |  | [optional]
**h** | **float** |  | [optional]
**invalid** | **bool** |  | [optional]
**matched_at** | **str** |  | [optional]
**name** | **str** |  | [optional]
**q** | **int** |  | [optional]
**review** | **bool** |  | [optional]
**score** | **int** |  | [optional]
**size** | **int** |  | [optional]
**src** | **str** |  | [optional]
**subj_src** | **str** |  | [optional]
**subj_uid** | **str** |  | [optional]
**thumb** | **str** |  | [optional]
**type** | **str** |  | [optional]
**uid** | **str** |  | [optional]
**w** | **float** |  | [optional]
**x** | **float** |  | [optional]
**y** | **float** |  | [optional]
**created_at** | **str** |  | [optional]
**updated_at** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.entity_marker import EntityMarker

# TODO update the JSON string below
json = "{}"
# create an instance of EntityMarker from a JSON string
entity_marker_instance = EntityMarker.from_json(json)
# print the JSON string representation of the object
print(EntityMarker.to_json())

# convert the object into a dict
entity_marker_dict = entity_marker_instance.to_dict()
# create an instance of EntityMarker from a dict
entity_marker_from_dict = EntityMarker.from_dict(entity_marker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


