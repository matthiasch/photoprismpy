# FormService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acc_error** | **str** |  | [optional]
**acc_key** | **str** |  | [optional]
**acc_name** | **str** |  | [optional]
**acc_owner** | **str** |  | [optional]
**acc_pass** | **str** |  | [optional]
**acc_share** | **bool** | Manual upload enabled, see SharePath, ShareSize, and ShareExpires. | [optional]
**acc_sync** | **bool** | Background sync enabled, see SyncDownload and SyncUpload. | [optional]
**acc_timeout** | **str** | Request timeout: default, high, medium, low, none | [optional]
**acc_type** | **str** |  | [optional]
**acc_url** | **str** |  | [optional]
**acc_user** | **str** |  | [optional]
**retry_limit** | **int** | Maximum number of failed requests. | [optional]
**share_expires** | **int** |  | [optional]
**share_path** | **str** |  | [optional]
**share_size** | **str** |  | [optional]
**sync_download** | **bool** |  | [optional]
**sync_filenames** | **bool** |  | [optional]
**sync_interval** | **int** |  | [optional]
**sync_path** | **str** |  | [optional]
**sync_raw** | **bool** |  | [optional]
**sync_upload** | **bool** |  | [optional]

## Example

```python
from photoprism_client.models.form_service import FormService

# TODO update the JSON string below
json = "{}"
# create an instance of FormService from a JSON string
form_service_instance = FormService.from_json(json)
# print the JSON string representation of the object
print(FormService.to_json())

# convert the object into a dict
form_service_dict = form_service_instance.to_dict()
# create an instance of FormService from a dict
form_service_from_dict = FormService.from_dict(form_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


