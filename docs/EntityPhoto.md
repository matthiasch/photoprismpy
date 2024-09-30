# EntityPhoto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**albums** | [**List[EntityAlbum]**](EntityAlbum.md) |  | [optional]
**altitude** | **int** |  | [optional]
**camera** | [**EntityCamera**](EntityCamera.md) |  | [optional]
**camera_id** | **int** |  | [optional]
**camera_serial** | **str** |  | [optional]
**camera_src** | **str** |  | [optional]
**cell** | [**EntityCell**](EntityCell.md) |  | [optional]
**cell_accuracy** | **int** |  | [optional]
**cell_id** | **str** |  | [optional]
**color** | **int** |  | [optional]
**country** | **str** |  | [optional]
**created_by** | **str** |  | [optional]
**day** | **int** |  | [optional]
**description** | **str** |  | [optional]
**description_src** | **str** |  | [optional]
**details** | [**EntityDetails**](EntityDetails.md) |  | [optional]
**document_id** | **str** |  | [optional]
**duration** | [**TimeDuration**](TimeDuration.md) |  | [optional]
**estimated_at** | **str** |  | [optional]
**exposure** | **str** |  | [optional]
**f_number** | **float** |  | [optional]
**faces** | **int** |  | [optional]
**favorite** | **bool** |  | [optional]
**focal_length** | **int** |  | [optional]
**iso** | **int** |  | [optional]
**lat** | **float** |  | [optional]
**lens** | [**EntityLens**](EntityLens.md) |  | [optional]
**lens_id** | **int** |  | [optional]
**lng** | **float** |  | [optional]
**month** | **int** |  | [optional]
**name** | **str** |  | [optional]
**original_name** | **str** |  | [optional]
**panorama** | **bool** |  | [optional]
**path** | **str** |  | [optional]
**place** | [**EntityPlace**](EntityPlace.md) |  | [optional]
**place_id** | **str** |  | [optional]
**place_src** | **str** |  | [optional]
**private** | **bool** |  | [optional]
**published_at** | **str** |  | [optional]
**quality** | **int** |  | [optional]
**resolution** | **int** |  | [optional]
**scan** | **bool** |  | [optional]
**stack** | **int** |  | [optional]
**taken_at** | **str** |  | [optional]
**taken_at_local** | **str** |  | [optional]
**taken_src** | **str** |  | [optional]
**time_zone** | **str** |  | [optional]
**title** | **str** |  | [optional]
**title_src** | **str** |  | [optional]
**type** | **str** |  | [optional]
**type_src** | **str** |  | [optional]
**uid** | **str** |  | [optional]
**year** | **int** |  | [optional]
**checked_at** | **str** |  | [optional]
**created_at** | **str** |  | [optional]
**deleted_at** | **str** |  | [optional]
**edited_at** | **str** |  | [optional]
**files** | [**List[EntityFile]**](EntityFile.md) |  | [optional]
**id** | **int** |  | [optional]
**labels** | [**List[EntityPhotoLabel]**](EntityPhotoLabel.md) |  | [optional]
**updated_at** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.entity_photo import EntityPhoto

# TODO update the JSON string below
json = "{}"
# create an instance of EntityPhoto from a JSON string
entity_photo_instance = EntityPhoto.from_json(json)
# print the JSON string representation of the object
print(EntityPhoto.to_json())

# convert the object into a dict
entity_photo_dict = entity_photo_instance.to_dict()
# create an instance of EntityPhoto from a dict
entity_photo_from_dict = EntityPhoto.from_dict(entity_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


