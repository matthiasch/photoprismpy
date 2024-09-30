# FormLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional]
**priority** | **int** |  | [optional]
**uncertainty** | **int** |  | [optional]

## Example

```python
from photoprism_client.models.form_label import FormLabel

# TODO update the JSON string below
json = "{}"
# create an instance of FormLabel from a JSON string
form_label_instance = FormLabel.from_json(json)
# print the JSON string representation of the object
print(FormLabel.to_json())

# convert the object into a dict
form_label_dict = form_label_instance.to_dict()
# create an instance of FormLabel from a dict
form_label_from_dict = FormLabel.from_dict(form_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


