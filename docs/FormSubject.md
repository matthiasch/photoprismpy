# FormSubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | **str** |  | [optional]
**alias** | **str** |  | [optional]
**bio** | **str** |  | [optional]
**excluded** | **bool** |  | [optional]
**favorite** | **bool** |  | [optional]
**hidden** | **bool** |  | [optional]
**name** | **str** |  | [optional]
**notes** | **str** |  | [optional]
**private** | **bool** |  | [optional]

## Example

```python
from photoprism_client.models.form_subject import FormSubject

# TODO update the JSON string below
json = "{}"
# create an instance of FormSubject from a JSON string
form_subject_instance = FormSubject.from_json(json)
# print the JSON string representation of the object
print(FormSubject.to_json())

# convert the object into a dict
form_subject_dict = form_subject_instance.to_dict()
# create an instance of FormSubject from a dict
form_subject_from_dict = FormSubject.from_dict(form_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


