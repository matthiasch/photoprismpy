# EntityFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **float** |  | [optional]
**chroma** | **int** |  | [optional]
**codec** | **str** |  | [optional]
**color_profile** | **str** |  | [optional]
**colors** | **str** |  | [optional]
**created_at** | **str** |  | [optional]
**created_in** | **int** |  | [optional]
**deleted_at** | **str** |  | [optional]
**diff** | **int** |  | [optional]
**duration** | [**TimeDuration**](TimeDuration.md) |  | [optional]
**error** | **str** |  | [optional]
**fps** | **float** |  | [optional]
**file_type** | **str** |  | [optional]
**frames** | **int** |  | [optional]
**hdr** | **bool** |  | [optional]
**hash** | **str** |  | [optional]
**height** | **int** |  | [optional]
**instance_id** | **str** |  | [optional]
**luminance** | **str** |  | [optional]
**main_color** | **str** |  | [optional]
**media_id** | **str** |  | [optional]
**media_type** | **str** |  | [optional]
**media_utc** | **int** |  | [optional]
**mime** | **str** |  | [optional]
**missing** | **bool** |  | [optional]
**mod_time** | **int** |  | [optional]
**name** | **str** |  | [optional]
**orientation** | **int** |  | [optional]
**orientation_src** | **str** |  | [optional]
**original_name** | **str** |  | [optional]
**photo_uid** | **str** |  | [optional]
**portrait** | **bool** |  | [optional]
**primary** | **bool** |  | [optional]
**projection** | **str** |  | [optional]
**published_at** | **str** |  | [optional]
**root** | **str** |  | [optional]
**sidecar** | **bool** |  | [optional]
**size** | **int** |  | [optional]
**software** | **str** |  | [optional]
**taken_at** | **str** |  | [optional]
**time_index** | **str** |  | [optional]
**uid** | **str** |  | [optional]
**updated_at** | **str** |  | [optional]
**updated_in** | **int** |  | [optional]
**video** | **bool** |  | [optional]
**watermark** | **bool** |  | [optional]
**width** | **int** |  | [optional]

## Example

```python
from photoprism_client.models.entity_file import EntityFile

# TODO update the JSON string below
json = "{}"
# create an instance of EntityFile from a JSON string
entity_file_instance = EntityFile.from_json(json)
# print the JSON string representation of the object
print(EntityFile.to_json())

# convert the object into a dict
entity_file_dict = entity_file_instance.to_dict()
# create an instance of EntityFile from a dict
entity_file_from_dict = EntityFile.from_dict(entity_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


