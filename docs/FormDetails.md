# FormDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artist** | **str** |  | [optional]
**artist_src** | **str** |  | [optional]
**copyright** | **str** |  | [optional]
**copyright_src** | **str** |  | [optional]
**keywords** | **str** |  | [optional]
**keywords_src** | **str** |  | [optional]
**license** | **str** |  | [optional]
**license_src** | **str** |  | [optional]
**notes** | **str** |  | [optional]
**notes_src** | **str** |  | [optional]
**photo_id** | **int** |  | [optional]
**subject** | **str** |  | [optional]
**subject_src** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.form_details import FormDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FormDetails from a JSON string
form_details_instance = FormDetails.from_json(json)
# print the JSON string representation of the object
print(FormDetails.to_json())

# convert the object into a dict
form_details_dict = form_details_instance.to_dict()
# create an instance of FormDetails from a dict
form_details_from_dict = FormDetails.from_dict(form_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


