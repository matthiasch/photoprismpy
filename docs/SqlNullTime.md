# SqlNullTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** |  | [optional]
**valid** | **bool** | Valid is true if Time is not NULL | [optional]

## Example

```python
from photoprism_client.models.sql_null_time import SqlNullTime

# TODO update the JSON string below
json = "{}"
# create an instance of SqlNullTime from a JSON string
sql_null_time_instance = SqlNullTime.from_json(json)
# print the JSON string representation of the object
print(SqlNullTime.to_json())

# convert the object into a dict
sql_null_time_dict = sql_null_time_instance.to_dict()
# create an instance of SqlNullTime from a dict
sql_null_time_from_dict = SqlNullTime.from_dict(sql_null_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


