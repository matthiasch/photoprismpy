# FormPhoto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**altitude** | **int** |  | [optional]
**camera_id** | **int** |  | [optional]
**camera_src** | **str** |  | [optional]
**cell_accuracy** | **int** |  | [optional]
**cell_id** | **str** |  | [optional]
**country** | **str** |  | [optional]
**day** | **int** |  | [optional]
**description** | **str** |  | [optional]
**description_src** | **str** |  | [optional]
**details** | [**FormDetails**](FormDetails.md) |  | [optional]
**exposure** | **str** |  | [optional]
**f_number** | **float** |  | [optional]
**favorite** | **bool** |  | [optional]
**focal_length** | **int** |  | [optional]
**iso** | **int** |  | [optional]
**lat** | **float** |  | [optional]
**lens_id** | **int** |  | [optional]
**lng** | **float** |  | [optional]
**month** | **int** |  | [optional]
**original_name** | **str** |  | [optional]
**panorama** | **bool** |  | [optional]
**place_id** | **str** |  | [optional]
**place_src** | **str** |  | [optional]
**private** | **bool** |  | [optional]
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
**year** | **int** |  | [optional]

## Example

```python
from photoprism_client.models.form_photo import FormPhoto

# TODO update the JSON string below
json = "{}"
# create an instance of FormPhoto from a JSON string
form_photo_instance = FormPhoto.from_json(json)
# print the JSON string representation of the object
print(FormPhoto.to_json())

# convert the object into a dict
form_photo_dict = form_photo_instance.to_dict()
# create an instance of FormPhoto from a dict
form_photo_from_dict = FormPhoto.from_dict(form_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


