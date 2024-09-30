# FormLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_comment** | **bool** |  | [optional]
**can_edit** | **bool** |  | [optional]
**expires** | **int** |  | [optional]
**max_views** | **int** |  | [optional]
**password** | **str** |  | [optional]
**slug** | **str** |  | [optional]
**token** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.form_link import FormLink

# TODO update the JSON string below
json = "{}"
# create an instance of FormLink from a JSON string
form_link_instance = FormLink.from_json(json)
# print the JSON string representation of the object
print(FormLink.to_json())

# convert the object into a dict
form_link_dict = form_link_instance.to_dict()
# create an instance of FormLink from a dict
form_link_from_dict = FormLink.from_dict(form_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


