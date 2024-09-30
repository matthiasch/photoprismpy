# EntityPhotoLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | [**EntityLabel**](EntityLabel.md) |  | [optional]
**label_id** | **int** |  | [optional]
**label_src** | **str** |  | [optional]
**photo** | [**EntityPhoto**](EntityPhoto.md) |  | [optional]
**photo_id** | **int** |  | [optional]
**uncertainty** | **int** |  | [optional]

## Example

```python
from photoprism_client.models.entity_photo_label import EntityPhotoLabel

# TODO update the JSON string below
json = "{}"
# create an instance of EntityPhotoLabel from a JSON string
entity_photo_label_instance = EntityPhotoLabel.from_json(json)
# print the JSON string representation of the object
print(EntityPhotoLabel.to_json())

# convert the object into a dict
entity_photo_label_dict = entity_photo_label_instance.to_dict()
# create an instance of EntityPhotoLabel from a dict
entity_photo_label_from_dict = EntityPhotoLabel.from_dict(entity_photo_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


