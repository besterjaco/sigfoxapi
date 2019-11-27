# sigfox_api_client.DeviceTypesApi

All URIs are relative to *https://api.sigfox.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_callback**](DeviceTypesApi.md#create_callback) | **POST** /device-types/{id}/callbacks | Create a callback
[**create_device_type**](DeviceTypesApi.md#create_device_type) | **POST** /device-types/ | Create a device type
[**delete_callback**](DeviceTypesApi.md#delete_callback) | **DELETE** /device-types/{id}/callbacks/{callbackId} | Delete a callback
[**device_type_bulk_restart**](DeviceTypesApi.md#device_type_bulk_restart) | **POST** /device-types/{id}/bulk/restart | Restart the devices of a device type
[**device_types_delete**](DeviceTypesApi.md#device_types_delete) | **DELETE** /device-types/{id} | Delete a device type
[**device_types_seq_number_disengage**](DeviceTypesApi.md#device_types_seq_number_disengage) | **PUT** /device-types/{id}/disengage | Disengage sequence number check for the next message
[**enable_callback**](DeviceTypesApi.md#enable_callback) | **PUT** /device-types/{id}/callbacks/{callbackId}/enable | Enable or disable a callback
[**enable_downlink_callback**](DeviceTypesApi.md#enable_downlink_callback) | **PUT** /device-types/{id}/callbacks/{callbackId}/downlink | Selects a downlink callback
[**get_callback_messages_error_list_for_device_type**](DeviceTypesApi.md#get_callback_messages_error_list_for_device_type) | **GET** /device-types/{id}/callbacks-not-delivered | Retrieve a list of callback errors
[**get_device_messages_list_for_device_type**](DeviceTypesApi.md#get_device_messages_list_for_device_type) | **GET** /device-types/{id}/messages | Retrieve a list of messages
[**get_device_type**](DeviceTypesApi.md#get_device_type) | **GET** /device-types/{id} | Retrieve information about a device type
[**get_device_type_bulk_restart_job**](DeviceTypesApi.md#get_device_type_bulk_restart_job) | **GET** /device-types/bulk/restart/{jobId} | Retrieve the device type async job status for restart action
[**list_callbacks**](DeviceTypesApi.md#list_callbacks) | **GET** /device-types/{id}/callbacks | Retrieve a list of callbacks
[**list_device_types**](DeviceTypesApi.md#list_device_types) | **GET** /device-types/ | Retrieve a list of device types
[**update_callback**](DeviceTypesApi.md#update_callback) | **PUT** /device-types/{id}/callbacks/{callbackId} | Update a callback
[**update_device_type**](DeviceTypesApi.md#update_device_type) | **PUT** /device-types/{id} | Update a device type

# **create_callback**
> object create_callback(body, id)

Create a callback

Create a new callback for a given device type. 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.CreateCallback() # CreateCallback | 
id = 'id_example' # str | The Device Type identifier from which callbacks will be retrieve

try:
    # Create a callback
    api_response = api_instance.create_callback(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->create_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCallback**](CreateCallback.md)|  | 
 **id** | **str**| The Device Type identifier from which callbacks will be retrieve | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_type**
> object create_device_type(body)

Create a device type

Create a new device type 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.DeviceTypeCreate() # DeviceTypeCreate | The device type to create

try:
    # Create a device type
    api_response = api_instance.create_device_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->create_device_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceTypeCreate**](DeviceTypeCreate.md)| The device type to create | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_callback**
> delete_callback(id, callback_id)

Delete a callback

Delete a callback for a given device type. 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device Type identifier from which callbacks will be retrieve
callback_id = 'callback_id_example' # str | The Callback identifier

try:
    # Delete a callback
    api_instance.delete_callback(id, callback_id)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->delete_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device Type identifier from which callbacks will be retrieve | 
 **callback_id** | **str**| The Callback identifier | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type_bulk_restart**
> object device_type_bulk_restart(id)

Restart the devices of a device type

Restart the devices of a device type with a asynchronous job. 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device Type identifier

try:
    # Restart the devices of a device type
    api_response = api_instance.device_type_bulk_restart(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->device_type_bulk_restart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device Type identifier | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_types_delete**
> device_types_delete(id)

Delete a device type

Delete a given device type. 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device Type identifier (hexademical format)

try:
    # Delete a device type
    api_instance.device_types_delete(id)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->device_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device Type identifier (hexademical format) | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_types_seq_number_disengage**
> device_types_seq_number_disengage(id)

Disengage sequence number check for the next message

Disable the sequence number check for the next message of each device of a device type. 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device Type identifier

try:
    # Disengage sequence number check for the next message
    api_instance.device_types_seq_number_disengage(id)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->device_types_seq_number_disengage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device Type identifier | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_callback**
> enable_callback(id, callback_id, enabled)

Enable or disable a callback

Enable or disable a callback for a given device type. 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device Type identifier from which callbacks will be retrieve
callback_id = 'callback_id_example' # str | The Callback identifier
enabled = true # bool | True to enable the callback, false to disable it

try:
    # Enable or disable a callback
    api_instance.enable_callback(id, callback_id, enabled)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->enable_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device Type identifier from which callbacks will be retrieve | 
 **callback_id** | **str**| The Callback identifier | 
 **enabled** | **bool**| True to enable the callback, false to disable it | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_downlink_callback**
> enable_downlink_callback(id, callback_id)

Selects a downlink callback

Selects a downlink callback for a device type. The callback will be selected as the downlink one, the one that was previously selected will no longer be used for downlink. 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device Type identifier from which callbacks will be retrieve
callback_id = 'callback_id_example' # str | The Callback identifier

try:
    # Selects a downlink callback
    api_instance.enable_downlink_callback(id, callback_id)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->enable_downlink_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device Type identifier from which callbacks will be retrieve | 
 **callback_id** | **str**| The Callback identifier | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_callback_messages_error_list_for_device_type**
> object get_callback_messages_error_list_for_device_type(id, since=since, before=before, limit=limit, offset=offset)

Retrieve a list of callback errors

Retrieve a list of undelivered callback messages for a given device types. 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device Type identifier
since = 789 # int | Starting timestamp (in milliseconds since Unix Epoch). (optional)
before = 789 # int | Ending timestamp (in milliseconds since Unix Epoch). (optional)
limit = 56 # int | Defines the maximum number of items to return (optional)
offset = 56 # int | Defines the number of items to skip (optional)

try:
    # Retrieve a list of callback errors
    api_response = api_instance.get_callback_messages_error_list_for_device_type(id, since=since, before=before, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->get_callback_messages_error_list_for_device_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device Type identifier | 
 **since** | **int**| Starting timestamp (in milliseconds since Unix Epoch). | [optional] 
 **before** | **int**| Ending timestamp (in milliseconds since Unix Epoch). | [optional] 
 **limit** | **int**| Defines the maximum number of items to return | [optional] 
 **offset** | **int**| Defines the number of items to skip | [optional] 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_messages_list_for_device_type**
> object get_device_messages_list_for_device_type(id, fields=fields, since=since, before=before, limit=limit, offset=offset)

Retrieve a list of messages

Retrieve a list of messages for a given device types with a 3-day history. 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device Type identifier
fields = 'fields_example' # str | Defines the other available API user's fields to be returned in the response.  (optional)
since = 789 # int | Starting timestamp (in milliseconds since Unix Epoch). (optional)
before = 789 # int | Ending timestamp (in milliseconds since Unix Epoch). (optional)
limit = 56 # int | Defines the maximum number of items to return (optional)
offset = 56 # int | Defines the number of items to skip (optional)

try:
    # Retrieve a list of messages
    api_response = api_instance.get_device_messages_list_for_device_type(id, fields=fields, since=since, before=before, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->get_device_messages_list_for_device_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device Type identifier | 
 **fields** | **str**| Defines the other available API user&#x27;s fields to be returned in the response.  | [optional] 
 **since** | **int**| Starting timestamp (in milliseconds since Unix Epoch). | [optional] 
 **before** | **int**| Ending timestamp (in milliseconds since Unix Epoch). | [optional] 
 **limit** | **int**| Defines the maximum number of items to return | [optional] 
 **offset** | **int**| Defines the number of items to skip | [optional] 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type**
> DeviceType get_device_type(id, fields=fields)

Retrieve information about a device type

Retrieve information about a device type. 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device Type identifier (hexademical format)
fields = 'fields_example' # str | Defines the other available API user's fields to be returned in the response.  (optional)

try:
    # Retrieve information about a device type
    api_response = api_instance.get_device_type(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->get_device_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device Type identifier (hexademical format) | 
 **fields** | **str**| Defines the other available API user&#x27;s fields to be returned in the response.  | [optional] 

### Return type

[**DeviceType**](DeviceType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type_bulk_restart_job**
> ActionJob get_device_type_bulk_restart_job(job_id)

Retrieve the device type async job status for restart action

Retrieve the async job status of a device type's asynchronous job for a restart devices action. 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job's identidier (hexademical format)

try:
    # Retrieve the device type async job status for restart action
    api_response = api_instance.get_device_type_bulk_restart_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->get_device_type_bulk_restart_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job&#x27;s identidier (hexademical format) | 

### Return type

[**ActionJob**](ActionJob.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_callbacks**
> object list_callbacks(id)

Retrieve a list of callbacks

Retrieve a list of callbacks for a given device type according to visibility permissions and request filters. 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device Type identifier from which callbacks will be retrieve

try:
    # Retrieve a list of callbacks
    api_response = api_instance.list_callbacks(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->list_callbacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device Type identifier from which callbacks will be retrieve | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_device_types**
> object list_device_types(name=name, group_ids=group_ids, deep=deep, contract_id=contract_id, payload_type=payload_type, sort=sort, fields=fields, limit=limit, offset=offset, page_id=page_id)

Retrieve a list of device types

Retrieve a list of device types according to visibility permissions and request filters. 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
name = 'name_example' # str | Search returns all Device Type names containing the value. Example: ?name=sig  (optional)
group_ids = ['group_ids_example'] # list[str] | Search for device types which are attached to a Group. Example: ?groupIds=57309674171c857460043087,57309674171c857460043088  (optional)
deep = true # bool | If a group identifier is specified, also includes its subgroups. (optional)
contract_id = 'contract_id_example' # str | Searches for device types which are attached to the given contract. (optional)
payload_type = 56 # int | Searches device types by payload type   - 2 -> Regular (raw payload)   - 3 -> Custom grammar   - 4 -> Geolocation   - 5 -> Display in ASCII   - 6 -> Radio planning frame   - 9 -> Sensitv2  (optional)
sort = 'sort_example' # str | The field on which the list will be sorted. (field to sort ascending or -field to sort descending). (optional)
fields = 'fields_example' # str | Defines the other available API user's fields to be returned in the response.  (optional)
limit = 56 # int | Defines the maximum number of items to return (optional)
offset = 56 # int | Defines the number of items to skip (optional)
page_id = 'page_id_example' # str | Token representing the page to retrieve (optional)

try:
    # Retrieve a list of device types
    api_response = api_instance.list_device_types(name=name, group_ids=group_ids, deep=deep, contract_id=contract_id, payload_type=payload_type, sort=sort, fields=fields, limit=limit, offset=offset, page_id=page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->list_device_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Search returns all Device Type names containing the value. Example: ?name&#x3D;sig  | [optional] 
 **group_ids** | [**list[str]**](str.md)| Search for device types which are attached to a Group. Example: ?groupIds&#x3D;57309674171c857460043087,57309674171c857460043088  | [optional] 
 **deep** | **bool**| If a group identifier is specified, also includes its subgroups. | [optional] 
 **contract_id** | **str**| Searches for device types which are attached to the given contract. | [optional] 
 **payload_type** | **int**| Searches device types by payload type   - 2 -&gt; Regular (raw payload)   - 3 -&gt; Custom grammar   - 4 -&gt; Geolocation   - 5 -&gt; Display in ASCII   - 6 -&gt; Radio planning frame   - 9 -&gt; Sensitv2  | [optional] 
 **sort** | **str**| The field on which the list will be sorted. (field to sort ascending or -field to sort descending). | [optional] 
 **fields** | **str**| Defines the other available API user&#x27;s fields to be returned in the response.  | [optional] 
 **limit** | **int**| Defines the maximum number of items to return | [optional] 
 **offset** | **int**| Defines the number of items to skip | [optional] 
 **page_id** | **str**| Token representing the page to retrieve | [optional] 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_callback**
> update_callback(body, id, callback_id)

Update a callback

Update a callback for a given device type 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.UpdateCallback() # UpdateCallback | The callback to update
id = 'id_example' # str | The Device Type identifier from which callbacks will be retrieve
callback_id = 'callback_id_example' # str | The Callback identifier

try:
    # Update a callback
    api_instance.update_callback(body, id, callback_id)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->update_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCallback**](UpdateCallback.md)| The callback to update | 
 **id** | **str**| The Device Type identifier from which callbacks will be retrieve | 
 **callback_id** | **str**| The Callback identifier | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_type**
> update_device_type(body, id)

Update a device type

Update a given device type. 

### Example
```python
from __future__ import print_function
import time
import sigfox_api_client
from sigfox_api_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sigfox_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sigfox_api_client.DeviceTypesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.DeviceTypeUpdate() # DeviceTypeUpdate | The device type to update
id = 'id_example' # str | The Device Type identifier (hexademical format)

try:
    # Update a device type
    api_instance.update_device_type(body, id)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->update_device_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceTypeUpdate**](DeviceTypeUpdate.md)| The device type to update | 
 **id** | **str**| The Device Type identifier (hexademical format) | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

