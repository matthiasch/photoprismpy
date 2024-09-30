# ConfigClientConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | **str** |  | [optional]
**acl** | **Dict[str, Dict[str, bool]]** |  | [optional]
**album_categories** | **List[str]** |  | [optional]
**albums** | [**List[EntityAlbum]**](EntityAlbum.md) |  | [optional]
**api_uri** | **str** |  | [optional]
**app_color** | **str** |  | [optional]
**app_icon** | **str** |  | [optional]
**app_mode** | **str** |  | [optional]
**app_name** | **str** |  | [optional]
**auth_mode** | **str** |  | [optional]
**base_uri** | **str** |  | [optional]
**cameras** | [**List[EntityCamera]**](EntityCamera.md) |  | [optional]
**categories** | [**List[ConfigCategoryLabel]**](ConfigCategoryLabel.md) |  | [optional]
**clip** | **int** |  | [optional]
**colors** | **List[Dict[str, str]]** |  | [optional]
**content_uri** | **str** |  | [optional]
**copyright** | **str** |  | [optional]
**count** | [**ConfigClientCounts**](ConfigClientCounts.md) |  | [optional]
**countries** | [**List[EntityCountry]**](EntityCountry.md) |  | [optional]
**css_uri** | **str** |  | [optional]
**customer** | **str** |  | [optional]
**debug** | **bool** |  | [optional]
**demo** | **bool** |  | [optional]
**disable** | [**ConfigClientDisable**](ConfigClientDisable.md) |  | [optional]
**download_token** | **str** |  | [optional]
**edition** | **str** |  | [optional]
**experimental** | **bool** |  | [optional]
**ext** | **Dict[str, object]** |  | [optional]
**flags** | **str** |  | [optional]
**js_uri** | **str** |  | [optional]
**legal_info** | **str** |  | [optional]
**legal_url** | **str** |  | [optional]
**lenses** | [**List[EntityLens]**](EntityLens.md) |  | [optional]
**login_uri** | **str** |  | [optional]
**manifest_uri** | **str** |  | [optional]
**map_key** | **str** |  | [optional]
**membership** | **str** |  | [optional]
**mode** | **str** |  | [optional]
**name** | **str** |  | [optional]
**password_length** | **int** |  | [optional]
**password_reset_uri** | **str** |  | [optional]
**people** | [**List[EntityPerson]**](EntityPerson.md) |  | [optional]
**pos** | [**ConfigClientPosition**](ConfigClientPosition.md) |  | [optional]
**preview_token** | **str** |  | [optional]
**public** | **bool** |  | [optional]
**readonly** | **bool** |  | [optional]
**register_uri** | **str** |  | [optional]
**restart** | **bool** |  | [optional]
**server** | [**EnvResources**](EnvResources.md) |  | [optional]
**settings** | [**CustomizeSettings**](CustomizeSettings.md) |  | [optional]
**site_author** | **str** |  | [optional]
**site_caption** | **str** |  | [optional]
**site_description** | **str** |  | [optional]
**site_domain** | **str** |  | [optional]
**site_preview** | **str** |  | [optional]
**site_title** | **str** |  | [optional]
**site_url** | **str** |  | [optional]
**sponsor** | **bool** |  | [optional]
**static_uri** | **str** |  | [optional]
**test** | **bool** |  | [optional]
**thumbs** | [**List[ConfigThumbSize]**](ConfigThumbSize.md) |  | [optional]
**tier** | **int** |  | [optional]
**trace** | **bool** |  | [optional]
**upload_nsfw** | **bool** |  | [optional]
**users_path** | **str** |  | [optional]
**version** | **str** |  | [optional]
**video_uri** | **str** |  | [optional]
**wallpaper_uri** | **str** |  | [optional]
**years** | **List[int]** |  | [optional]

## Example

```python
from photoprism_client.models.config_client_config import ConfigClientConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClientConfig from a JSON string
config_client_config_instance = ConfigClientConfig.from_json(json)
# print the JSON string representation of the object
print(ConfigClientConfig.to_json())

# convert the object into a dict
config_client_config_dict = config_client_config_instance.to_dict()
# create an instance of ConfigClientConfig from a dict
config_client_config_from_dict = ConfigClientConfig.from_dict(config_client_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


