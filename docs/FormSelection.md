# FormSelection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**albums** | **List[str]** |  | [optional]
**all** | **bool** |  | [optional]
**files** | **List[str]** |  | [optional]
**labels** | **List[str]** |  | [optional]
**photos** | **List[str]** |  | [optional]
**places** | **List[str]** |  | [optional]
**subjects** | **List[str]** |  | [optional]

## Example

```python
from photoprism_client.models.form_selection import FormSelection

# TODO update the JSON string below
json = "{}"
# create an instance of FormSelection from a JSON string
form_selection_instance = FormSelection.from_json(json)
# print the JSON string representation of the object
print(FormSelection.to_json())

# convert the object into a dict
form_selection_dict = form_selection_instance.to_dict()
# create an instance of FormSelection from a dict
form_selection_from_dict = FormSelection.from_dict(form_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


