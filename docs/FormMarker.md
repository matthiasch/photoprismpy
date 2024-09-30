# FormMarker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_uid** | **str** |  | [optional]
**h** | **float** |  | [optional]
**invalid** | **bool** |  | [optional]
**marker_review** | **bool** |  | [optional]
**name** | **str** |  | [optional]
**src** | **str** |  | [optional]
**subj_src** | **str** |  | [optional]
**type** | **str** |  | [optional]
**w** | **float** |  | [optional]
**x** | **float** |  | [optional]
**y** | **float** |  | [optional]

## Example

```python
from photoprism_client.models.form_marker import FormMarker

# TODO update the JSON string below
json = "{}"
# create an instance of FormMarker from a JSON string
form_marker_instance = FormMarker.from_json(json)
# print the JSON string representation of the object
print(FormMarker.to_json())

# convert the object into a dict
form_marker_dict = form_marker_instance.to_dict()
# create an instance of FormMarker from a dict
form_marker_from_dict = FormMarker.from_dict(form_marker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


