# ConfigOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_color** | **str** |  | [optional]
**app_icon** | **str** |  | [optional]
**app_mode** | **str** |  | [optional]
**app_name** | **str** |  | [optional]
**auto_import** | **int** |  | [optional]
**auto_index** | **int** |  | [optional]
**backup_albums** | **bool** |  | [optional] [default to True]
**backup_database** | **bool** |  | [optional] [default to True]
**backup_retain** | **int** |  | [optional]
**backup_schedule** | **str** |  | [optional]
**cdn_url** | **str** |  | [optional]
**cdn_video** | **bool** |  | [optional]
**debug** | **bool** |  | [optional]
**default_locale** | **str** |  | [optional]
**default_tls** | **bool** |  | [optional]
**default_theme** | **str** |  | [optional]
**default_timezone** | **str** |  | [optional]
**detect_nsfw** | **bool** |  | [optional]
**disable_backups** | **bool** |  | [optional]
**disable_classification** | **bool** |  | [optional]
**disable_darktable** | **bool** |  | [optional]
**disable_exif_tool** | **bool** |  | [optional]
**disable_f_fmpeg** | **bool** |  | [optional]
**disable_faces** | **bool** |  | [optional]
**disable_heif_convert** | **bool** |  | [optional]
**disable_image_magick** | **bool** |  | [optional]
**disable_jpeg_xl** | **bool** |  | [optional]
**disable_oidc** | **bool** |  | [optional]
**disable_places** | **bool** |  | [optional]
**disable_raw** | **bool** |  | [optional]
**disable_raw_therapee** | **bool** |  | [optional]
**disable_sips** | **bool** |  | [optional]
**disable_tls** | **bool** |  | [optional]
**disable_tensor_flow** | **bool** |  | [optional]
**disable_vectors** | **bool** |  | [optional]
**disable_vips** | **bool** |  | [optional]
**disable_web_dav** | **bool** |  | [optional]
**exif_brute_force** | **bool** |  | [optional]
**experimental** | **bool** |  | [optional]
**f_fmpeg_bitrate** | **int** |  | [optional]
**f_fmpeg_encoder** | **str** |  | [optional]
**f_fmpeg_map_audio** | **str** |  | [optional]
**f_fmpeg_map_video** | **str** |  | [optional]
**f_fmpeg_size** | **int** |  | [optional]
**http_cache_max_age** | **int** |  | [optional]
**http_cache_public** | **bool** |  | [optional]
**http_video_max_age** | **int** |  | [optional]
**https_proxy** | **str** |  | [optional]
**https_proxy_insecure** | **bool** |  | [optional]
**index_schedule** | **str** |  | [optional]
**index_workers** | **int** |  | [optional]
**jpeg_quality** | **int** |  | [optional]
**jpeg_size** | **int** |  | [optional]
**legal_info** | **str** |  | [optional]
**legal_url** | **str** |  | [optional]
**oidc_icon** | **str** |  | [optional]
**oidc_provider** | **str** |  | [optional]
**oidc_redirect** | **bool** |  | [optional]
**oidc_register** | **bool** |  | [optional]
**originals_limit** | **int** |  | [optional]
**png_size** | **int** |  | [optional]
**prod** | **bool** |  | [optional]
**raw_presets** | **bool** |  | [optional]
**read_only** | **bool** |  | [optional]
**resolution_limit** | **int** |  | [optional]
**sidecar_yaml** | **bool** |  | [optional] [default to True]
**site_author** | **str** |  | [optional]
**site_caption** | **str** |  | [optional]
**site_description** | **str** |  | [optional]
**site_preview** | **str** |  | [optional]
**site_title** | **str** |  | [optional]
**site_url** | **str** |  | [optional]
**tls_cert** | **str** |  | [optional]
**tls_email** | **str** |  | [optional]
**tls_key** | **str** |  | [optional]
**test** | **bool** |  | [optional]
**thumb_color** | **str** |  | [optional]
**thumb_filter** | **str** |  | [optional]
**thumb_library** | **str** |  | [optional]
**thumb_size** | **int** |  | [optional]
**thumb_size_uncached** | **int** |  | [optional]
**thumb_uncached** | **bool** |  | [optional]
**trace** | **bool** |  | [optional]
**wakeup_interval** | [**TimeDuration**](TimeDuration.md) |  | [optional]
**wallpaper_uri** | **str** |  | [optional]

## Example

```python
from photoprism_client.models.config_options import ConfigOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigOptions from a JSON string
config_options_instance = ConfigOptions.from_json(json)
# print the JSON string representation of the object
print(ConfigOptions.to_json())

# convert the object into a dict
config_options_dict = config_options_instance.to_dict()
# create an instance of ConfigOptions from a dict
config_options_from_dict = ConfigOptions.from_dict(config_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


