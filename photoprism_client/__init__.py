# coding: utf-8

# flake8: noqa

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from photoprism_client.api.albums_api import AlbumsApi
from photoprism_client.api.authentication_api import AuthenticationApi
from photoprism_client.api.config_api import ConfigApi
from photoprism_client.api.download_api import DownloadApi
from photoprism_client.api.errors_api import ErrorsApi
from photoprism_client.api.faces_api import FacesApi
from photoprism_client.api.files_api import FilesApi
from photoprism_client.api.folders_api import FoldersApi
from photoprism_client.api.images_api import ImagesApi
from photoprism_client.api.labels_api import LabelsApi
from photoprism_client.api.library_api import LibraryApi
from photoprism_client.api.links_api import LinksApi
from photoprism_client.api.markers_api import MarkersApi
from photoprism_client.api.photos_api import PhotosApi
from photoprism_client.api.server_api import ServerApi
from photoprism_client.api.services_api import ServicesApi
from photoprism_client.api.settings_api import SettingsApi
from photoprism_client.api.stacks_api import StacksApi
from photoprism_client.api.subjects_api import SubjectsApi
from photoprism_client.api.users_api import UsersApi
from photoprism_client.api.videos_api import VideosApi

# import ApiClient
from photoprism_client.api_response import ApiResponse
from photoprism_client.api_client import ApiClient
from photoprism_client.configuration import Configuration
from photoprism_client.exceptions import OpenApiException
from photoprism_client.exceptions import ApiTypeError
from photoprism_client.exceptions import ApiValueError
from photoprism_client.exceptions import ApiKeyError
from photoprism_client.exceptions import ApiAttributeError
from photoprism_client.exceptions import ApiException

# import models into sdk package
from photoprism_client.models.config_category_label import ConfigCategoryLabel
from photoprism_client.models.config_client_config import ConfigClientConfig
from photoprism_client.models.config_client_counts import ConfigClientCounts
from photoprism_client.models.config_client_disable import ConfigClientDisable
from photoprism_client.models.config_client_position import ConfigClientPosition
from photoprism_client.models.config_options import ConfigOptions
from photoprism_client.models.config_thumb_size import ConfigThumbSize
from photoprism_client.models.customize_download_name import CustomizeDownloadName
from photoprism_client.models.customize_download_settings import CustomizeDownloadSettings
from photoprism_client.models.customize_feature_settings import CustomizeFeatureSettings
from photoprism_client.models.customize_import_settings import CustomizeImportSettings
from photoprism_client.models.customize_index_settings import CustomizeIndexSettings
from photoprism_client.models.customize_maps_settings import CustomizeMapsSettings
from photoprism_client.models.customize_search_settings import CustomizeSearchSettings
from photoprism_client.models.customize_settings import CustomizeSettings
from photoprism_client.models.customize_share_settings import CustomizeShareSettings
from photoprism_client.models.customize_stack_settings import CustomizeStackSettings
from photoprism_client.models.customize_template_settings import CustomizeTemplateSettings
from photoprism_client.models.customize_ui_settings import CustomizeUISettings
from photoprism_client.models.entity_album import EntityAlbum
from photoprism_client.models.entity_camera import EntityCamera
from photoprism_client.models.entity_cell import EntityCell
from photoprism_client.models.entity_country import EntityCountry
from photoprism_client.models.entity_details import EntityDetails
from photoprism_client.models.entity_error import EntityError
from photoprism_client.models.entity_face import EntityFace
from photoprism_client.models.entity_file import EntityFile
from photoprism_client.models.entity_label import EntityLabel
from photoprism_client.models.entity_lens import EntityLens
from photoprism_client.models.entity_link import EntityLink
from photoprism_client.models.entity_marker import EntityMarker
from photoprism_client.models.entity_person import EntityPerson
from photoprism_client.models.entity_photo import EntityPhoto
from photoprism_client.models.entity_photo_label import EntityPhotoLabel
from photoprism_client.models.entity_place import EntityPlace
from photoprism_client.models.entity_service import EntityService
from photoprism_client.models.entity_subject import EntitySubject
from photoprism_client.models.env_resources import EnvResources
from photoprism_client.models.env_resources_memory import EnvResourcesMemory
from photoprism_client.models.form_album import FormAlbum
from photoprism_client.models.form_details import FormDetails
from photoprism_client.models.form_face import FormFace
from photoprism_client.models.form_file import FormFile
from photoprism_client.models.form_label import FormLabel
from photoprism_client.models.form_link import FormLink
from photoprism_client.models.form_marker import FormMarker
from photoprism_client.models.form_photo import FormPhoto
from photoprism_client.models.form_selection import FormSelection
from photoprism_client.models.form_service import FormService
from photoprism_client.models.form_subject import FormSubject
from photoprism_client.models.i18n_response import I18nResponse
from photoprism_client.models.search_album import SearchAlbum
from photoprism_client.models.search_face import SearchFace
from photoprism_client.models.search_geo_result import SearchGeoResult
from photoprism_client.models.search_label import SearchLabel
from photoprism_client.models.search_photo import SearchPhoto
from photoprism_client.models.search_subject import SearchSubject
from photoprism_client.models.sql_null_time import SqlNullTime
from photoprism_client.models.time_duration import TimeDuration
