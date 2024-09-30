# I18nResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional]
**details** | **str** |  | [optional]
**error** | **str** |  | [optional]
**message** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.i18n_response import I18nResponse

# TODO update the JSON string below
json = "{}"
# create an instance of I18nResponse from a JSON string
i18n_response_instance = I18nResponse.from_json(json)
# print the JSON string representation of the object
print(I18nResponse.to_json())

# convert the object into a dict
i18n_response_dict = i18n_response_instance.to_dict()
# create an instance of I18nResponse from a dict
i18n_response_from_dict = I18nResponse.from_dict(i18n_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


