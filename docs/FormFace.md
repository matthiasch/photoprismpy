# FormFace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hidden** | **bool** |  | [optional]
**subj_uid** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.form_face import FormFace

# TODO update the JSON string below
json = "{}"
# create an instance of FormFace from a JSON string
form_face_instance = FormFace.from_json(json)
# print the JSON string representation of the object
print(FormFace.to_json())

# convert the object into a dict
form_face_dict = form_face_instance.to_dict()
# create an instance of FormFace from a dict
form_face_from_dict = FormFace.from_dict(form_face_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


