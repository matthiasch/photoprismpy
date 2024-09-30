# EntityDetails


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
**software** | **str** |  | [optional]
**software_src** | **str** |  | [optional]
**subject** | **str** |  | [optional]
**subject_src** | **str** |  | [optional]
**created_at** | **str** |  | [optional]
**photo_id** | **int** |  | [optional]
**updated_at** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.entity_details import EntityDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EntityDetails from a JSON string
entity_details_instance = EntityDetails.from_json(json)
# print the JSON string representation of the object
print(EntityDetails.to_json())

# convert the object into a dict
entity_details_dict = entity_details_instance.to_dict()
# create an instance of EntityDetails from a dict
entity_details_from_dict = EntityDetails.from_dict(entity_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


