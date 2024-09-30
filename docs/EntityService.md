# EntityService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acc_error** | **str** |  | [optional]
**acc_errors** | **int** |  | [optional]
**acc_key** | **str** |  | [optional]
**acc_name** | **str** |  | [optional]
**acc_owner** | **str** |  | [optional]
**acc_pass** | **str** |  | [optional]
**acc_share** | **bool** |  | [optional]
**acc_sync** | **bool** |  | [optional]
**acc_timeout** | **str** |  | [optional]
**acc_type** | **str** |  | [optional]
**acc_url** | **str** |  | [optional]
**acc_user** | **str** |  | [optional]
**created_at** | **str** |  | [optional]
**deleted_at** | **str** |  | [optional]
**id** | **int** |  | [optional]
**retry_limit** | **int** |  | [optional]
**share_expires** | **int** |  | [optional]
**share_path** | **str** |  | [optional]
**share_size** | **str** |  | [optional]
**sync_date** | [**SqlNullTime**](SqlNullTime.md) |  | [optional]
**sync_download** | **bool** |  | [optional]
**sync_filenames** | **bool** |  | [optional]
**sync_interval** | **int** |  | [optional]
**sync_path** | **str** |  | [optional]
**sync_raw** | **bool** |  | [optional]
**sync_status** | **str** |  | [optional]
**sync_upload** | **bool** |  | [optional]
**updated_at** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.entity_service import EntityService

# TODO update the JSON string below
json = "{}"
# create an instance of EntityService from a JSON string
entity_service_instance = EntityService.from_json(json)
# print the JSON string representation of the object
print(EntityService.to_json())

# convert the object into a dict
entity_service_dict = entity_service_instance.to_dict()
# create an instance of EntityService from a dict
entity_service_from_dict = EntityService.from_dict(entity_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


