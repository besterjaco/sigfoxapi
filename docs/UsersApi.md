# sigfox_api_client.UsersApi

All URIs are relative to *https://api.sigfox.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_roles**](UsersApi.md#add_user_roles) | **PUT** /users/{id}/profiles | add user roles to a user
[**create_user**](UsersApi.md#create_user) | **POST** /users/ | Create a user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{id} | Delete a user
[**delete_user_role**](UsersApi.md#delete_user_role) | **DELETE** /users/{id}/profiles/{profileId} | Delete profiles or a given profile associated to the groupId
[**get_user**](UsersApi.md#get_user) | **GET** /users/{id} | Retrieve information about a user
[**list_users**](UsersApi.md#list_users) | **GET** /users/ | Retrieve a list of users according to visibility permissions and request filters
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{id} | Update a user

# **add_user_roles**
> add_user_roles(body, id)

add user roles to a user

add user roles to a user. 

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
api_instance = sigfox_api_client.UsersApi(sigfox_api_client.ApiClient(configuration))
body = NULL # object | user roles array to add
id = 'id_example' # str | The User identifier

try:
    # add user roles to a user
    api_instance.add_user_roles(body, id)
except ApiException as e:
    print("Exception when calling UsersApi->add_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| user roles array to add | 
 **id** | **str**| The User identifier | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> CreateResponse create_user(body)

Create a user

Create a new user. 

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
api_instance = sigfox_api_client.UsersApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.UserCreation() # UserCreation | The user to create

try:
    # Create a user
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreation**](UserCreation.md)| The user to create | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(id)

Delete a user

Delete a given user. 

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
api_instance = sigfox_api_client.UsersApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The User identifier

try:
    # Delete a user
    api_instance.delete_user(id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The User identifier | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_role**
> delete_user_role(id, profile_id, group_id=group_id)

Delete profiles or a given profile associated to the groupId

Delete profiles or a given profile associated to the groupId 

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
api_instance = sigfox_api_client.UsersApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The User identifier
profile_id = 'profile_id_example' # str | The profile identifier
group_id = 'group_id_example' # str | The group identifier (optional)

try:
    # Delete profiles or a given profile associated to the groupId
    api_instance.delete_user_role(id, profile_id, group_id=group_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The User identifier | 
 **profile_id** | **str**| The profile identifier | 
 **group_id** | **str**| The group identifier | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(id, fields=fields)

Retrieve information about a user

Retrieve information about a given user. The id can also be the user's email address. 

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
api_instance = sigfox_api_client.UsersApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The User identifier
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)

try:
    # Retrieve information about a user
    api_response = api_instance.get_user(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The User identifier | 
 **fields** | **str**| Defines the other available fields to be returned in the response.  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> object list_users(fields=fields, text=text, profile_id=profile_id, group_ids=group_ids, deep=deep, sort=sort, limit=limit, offset=offset, page_id=page_id)

Retrieve a list of users according to visibility permissions and request filters

Retrieve a list of users according to visibility permissions and request filters. 

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
api_instance = sigfox_api_client.UsersApi(sigfox_api_client.ApiClient(configuration))
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)
text = 'text_example' # str | Searches for users containing the given text in their name or email (optional)
profile_id = 'profile_id_example' # str | Searches for users who have the given profile affected (optional)
group_ids = ['group_ids_example'] # list[str] | Searches for users who are attached to the given groups (optional)
deep = true # bool | Deep search in the sub group hierarchy (optional)
sort = 'sort_example' # str | The field on which the list will be sorted. (field to sort ascending or -field to sort descending) sort by name will sort on lowercase and ascii string version of \"<firstName> <lastName>\"  (optional)
limit = 56 # int | The maximum number of items to return (optional)
offset = 56 # int | The number of items to skip (optional)
page_id = 'page_id_example' # str | Token representing the page to retrieve (optional)

try:
    # Retrieve a list of users according to visibility permissions and request filters
    api_response = api_instance.list_users(fields=fields, text=text, profile_id=profile_id, group_ids=group_ids, deep=deep, sort=sort, limit=limit, offset=offset, page_id=page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Defines the other available fields to be returned in the response.  | [optional] 
 **text** | **str**| Searches for users containing the given text in their name or email | [optional] 
 **profile_id** | **str**| Searches for users who have the given profile affected | [optional] 
 **group_ids** | [**list[str]**](str.md)| Searches for users who are attached to the given groups | [optional] 
 **deep** | **bool**| Deep search in the sub group hierarchy | [optional] 
 **sort** | **str**| The field on which the list will be sorted. (field to sort ascending or -field to sort descending) sort by name will sort on lowercase and ascii string version of \&quot;&lt;firstName&gt; &lt;lastName&gt;\&quot;  | [optional] 
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

# **update_user**
> UpdateResponse update_user(body, id)

Update a user

Update a given user. 

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
api_instance = sigfox_api_client.UsersApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.UserUpdate() # UserUpdate | The user to update
id = 'id_example' # str | The User identifier

try:
    # Update a user
    api_response = api_instance.update_user(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserUpdate**](UserUpdate.md)| The user to update | 
 **id** | **str**| The User identifier | 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

