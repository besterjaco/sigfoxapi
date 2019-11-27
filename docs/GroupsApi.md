# sigfox_api_client.GroupsApi

All URIs are relative to *https://api.sigfox.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](GroupsApi.md#create_group) | **POST** /groups/ | Create a group
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /groups/{id} | Delete a group
[**get_callback_messages_error_list_for_group**](GroupsApi.md#get_callback_messages_error_list_for_group) | **GET** /groups/{id}/callbacks-not-delivered | Retrieve a list of undelivered callbacks
[**get_group**](GroupsApi.md#get_group) | **GET** /groups/{id} | Retrieve information about a group
[**list_geolocation_payload**](GroupsApi.md#list_geolocation_payload) | **GET** /groups/{id}/geoloc-payloads | Retrieve a list of geolocation payload
[**list_groups**](GroupsApi.md#list_groups) | **GET** /groups/ | Retrieve a list of groups according to visibility permissions and request filters.
[**update_group**](GroupsApi.md#update_group) | **PUT** /groups/{id} | Update a group

# **create_group**
> object create_group(body)

Create a group

Create a new group. 

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
api_instance = sigfox_api_client.GroupsApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.CommonGroupCreate() # CommonGroupCreate | 

try:
    # Create a group
    api_response = api_instance.create_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommonGroupCreate**](CommonGroupCreate.md)|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(id)

Delete a group

Delete a given group. 

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
api_instance = sigfox_api_client.GroupsApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Group identifier

try:
    # Delete a group
    api_instance.delete_group(id)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Group identifier | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_callback_messages_error_list_for_group**
> object get_callback_messages_error_list_for_group(id, since=since, before=before, limit=limit, offset=offset)

Retrieve a list of undelivered callbacks

Retrieve a list of undelivered callbacks and errors for a given group, in reverse chronological order (most recent message first). 

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
api_instance = sigfox_api_client.GroupsApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Group identifier
since = 789 # int | Starting timestamp (in milliseconds since Unix Epoch) (optional)
before = 789 # int | Ending timestamp (in milliseconds since Unix Epoch) (optional)
limit = 56 # int | The maximum number of items to return (optional)
offset = 56 # int | The number of items to skip (optional)

try:
    # Retrieve a list of undelivered callbacks
    api_response = api_instance.get_callback_messages_error_list_for_group(id, since=since, before=before, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_callback_messages_error_list_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Group identifier | 
 **since** | **int**| Starting timestamp (in milliseconds since Unix Epoch) | [optional] 
 **before** | **int**| Ending timestamp (in milliseconds since Unix Epoch) | [optional] 
 **limit** | **int**| The maximum number of items to return | [optional] 
 **offset** | **int**| The number of items to skip | [optional] 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(id, fields=fields)

Retrieve information about a group

Retrieve information about a given group. 

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
api_instance = sigfox_api_client.GroupsApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Group identifier
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)

try:
    # Retrieve information about a group
    api_response = api_instance.get_group(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Group identifier | 
 **fields** | **str**| Defines the other available fields to be returned in the response.  | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_geolocation_payload**
> object list_geolocation_payload(id, limit=limit, offset=offset, page_id=page_id)

Retrieve a list of geolocation payload

Retrieve a list of geolocation payload according to request filters. 

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
api_instance = sigfox_api_client.GroupsApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Group identifier
limit = 56 # int | The maximum number of items to return (optional)
offset = 56 # int | The number of items to skip (optional)
page_id = 'page_id_example' # str | Token representing the page to retrieve (optional)

try:
    # Retrieve a list of geolocation payload
    api_response = api_instance.list_geolocation_payload(id, limit=limit, offset=offset, page_id=page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->list_geolocation_payload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Group identifier | 
 **limit** | **int**| The maximum number of items to return | [optional] 
 **offset** | **int**| The number of items to skip | [optional] 
 **page_id** | **str**| Token representing the page to retrieve | [optional] 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> object list_groups(parent_ids=parent_ids, deep=deep, name=name, types=types, fields=fields, sort=sort, limit=limit, offset=offset, page_id=page_id)

Retrieve a list of groups according to visibility permissions and request filters.

Retrieve a list of groups according to visibility permissions and request filters.    If parentIds is provided, retrieve all direct sub-groups under the given parents. If parentIds is not provided, retrieve all direct sub-groups under the API user's group.   If deep is true, retrieve all sub-groups under either given parent groups or the API user group. 

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
api_instance = sigfox_api_client.GroupsApi(sigfox_api_client.ApiClient(configuration))
parent_ids = ['parent_ids_example'] # list[str] | The parent group's identifiers from which the children will be fetched (optional)
deep = true # bool | Retrieve all sub-groups (optional)
name = 'name_example' # str | Searches for groups containing the given text in their name (optional)
types = [56] # list[int] | Group's type - 0 -> SO - 2 -> Other - 5 -> SVNO - 6 -> Partners - 7 -> NIP - 8 -> DIST - 9 -> Channel - 10 -> Starter - 11 -> Partner  (optional)
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)
sort = 'sort_example' # str | The field on which the list will be sorted. (field to sort ascending or -field to sort descending) (optional)
limit = 56 # int | The maximum number of items to return (optional)
offset = 56 # int | The number of items to skip (optional)
page_id = 'page_id_example' # str | Token representing the page to retrieve (optional)

try:
    # Retrieve a list of groups according to visibility permissions and request filters.
    api_response = api_instance.list_groups(parent_ids=parent_ids, deep=deep, name=name, types=types, fields=fields, sort=sort, limit=limit, offset=offset, page_id=page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->list_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_ids** | [**list[str]**](str.md)| The parent group&#x27;s identifiers from which the children will be fetched | [optional] 
 **deep** | **bool**| Retrieve all sub-groups | [optional] 
 **name** | **str**| Searches for groups containing the given text in their name | [optional] 
 **types** | [**list[int]**](int.md)| Group&#x27;s type - 0 -&gt; SO - 2 -&gt; Other - 5 -&gt; SVNO - 6 -&gt; Partners - 7 -&gt; NIP - 8 -&gt; DIST - 9 -&gt; Channel - 10 -&gt; Starter - 11 -&gt; Partner  | [optional] 
 **fields** | **str**| Defines the other available fields to be returned in the response.  | [optional] 
 **sort** | **str**| The field on which the list will be sorted. (field to sort ascending or -field to sort descending) | [optional] 
 **limit** | **int**| The maximum number of items to return | [optional] 
 **offset** | **int**| The number of items to skip | [optional] 
 **page_id** | **str**| Token representing the page to retrieve | [optional] 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> update_group(body, id)

Update a group

Update a given group. 

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
api_instance = sigfox_api_client.GroupsApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.CommonGroupUpdate() # CommonGroupUpdate | The group to update
id = 'id_example' # str | The Group identifier

try:
    # Update a group
    api_instance.update_group(body, id)
except ApiException as e:
    print("Exception when calling GroupsApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommonGroupUpdate**](CommonGroupUpdate.md)| The group to update | 
 **id** | **str**| The Group identifier | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

