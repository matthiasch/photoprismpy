# SearchPhoto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**altitude** | **int** |  | [optional]
**camera_id** | **int** | Camera | [optional]
**camera_make** | **str** |  | [optional]
**camera_model** | **str** |  | [optional]
**camera_serial** | **str** |  | [optional]
**camera_src** | **str** |  | [optional]
**cell_accuracy** | **int** |  | [optional]
**cell_id** | **str** | Cell | [optional]
**checked_at** | **str** |  | [optional]
**color** | **int** |  | [optional]
**country** | **str** |  | [optional]
**created_at** | **str** |  | [optional]
**day** | **int** |  | [optional]
**deleted_at** | **str** |  | [optional]
**description** | **str** |  | [optional]
**document_id** | **str** |  | [optional]
**duration** | [**TimeDuration**](TimeDuration.md) |  | [optional]
**edited_at** | **str** |  | [optional]
**exposure** | **str** |  | [optional]
**f_number** | **float** |  | [optional]
**faces** | **int** |  | [optional]
**favorite** | **bool** |  | [optional]
**file_name** | **str** |  | [optional]
**file_root** | **str** |  | [optional]
**file_uid** | **str** |  | [optional]
**files** | [**List[EntityFile]**](EntityFile.md) |  | [optional]
**focal_length** | **int** |  | [optional]
**hash** | **str** |  | [optional]
**height** | **int** |  | [optional]
**id** | **str** |  | [optional]
**instance_id** | **str** |  | [optional]
**iso** | **int** |  | [optional]
**lat** | **float** |  | [optional]
**lens_id** | **int** | Lens | [optional]
**lens_make** | **str** |  | [optional]
**lens_model** | **str** |  | [optional]
**lng** | **float** |  | [optional]
**merged** | **bool** |  | [optional]
**month** | **int** |  | [optional]
**name** | **str** |  | [optional]
**original_name** | **str** |  | [optional]
**panorama** | **bool** |  | [optional]
**path** | **str** |  | [optional]
**place_city** | **str** |  | [optional]
**place_country** | **str** |  | [optional]
**place_id** | **str** |  | [optional]
**place_label** | **str** |  | [optional]
**place_src** | **str** |  | [optional]
**place_state** | **str** |  | [optional]
**portrait** | **bool** |  | [optional]
**private** | **bool** |  | [optional]
**quality** | **int** |  | [optional]
**resolution** | **int** |  | [optional]
**scan** | **bool** |  | [optional]
**stack** | **int** |  | [optional]
**taken_at** | **str** |  | [optional]
**taken_at_local** | **str** |  | [optional]
**taken_src** | **str** |  | [optional]
**time_zone** | **str** |  | [optional]
**title** | **str** |  | [optional]
**type** | **str** |  | [optional]
**type_src** | **str** |  | [optional]
**uid** | **str** |  | [optional]
**updated_at** | **str** |  | [optional]
**width** | **int** |  | [optional]
**year** | **int** |  | [optional]

## Example

```python
from photoprism_client.models.search_photo import SearchPhoto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPhoto from a JSON string
search_photo_instance = SearchPhoto.from_json(json)
# print the JSON string representation of the object
print(SearchPhoto.to_json())

# convert the object into a dict
search_photo_dict = search_photo_instance.to_dict()
# create an instance of SearchPhoto from a dict
search_photo_from_dict = SearchPhoto.from_dict(search_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


