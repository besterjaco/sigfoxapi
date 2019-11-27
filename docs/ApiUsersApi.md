# sigfox_api_client.ApiUsersApi

All URIs are relative to *https://api.sigfox.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_profile_to_api_user**](ApiUsersApi.md#add_profile_to_api_user) | **PUT** /api-users/{id}/profiles | Associate profiles to an API user.
[**create_api_user**](ApiUsersApi.md#create_api_user) | **POST** /api-users/ | Create an API user
[**delete_api_user**](ApiUsersApi.md#delete_api_user) | **DELETE** /api-users/{id} | Delete an API user
[**delete_profile_of_api_user**](ApiUsersApi.md#delete_profile_of_api_user) | **DELETE** /api-users/{id}/profiles/{profileId} | Delete a profile to a given API user.
[**get_api_user**](ApiUsersApi.md#get_api_user) | **GET** /api-users/{id} | Retrieve information about an API user
[**list_api_users**](ApiUsersApi.md#list_api_users) | **GET** /api-users/ | Retrieve a list of API users
[**renew_credential**](ApiUsersApi.md#renew_credential) | **PUT** /api-users/{id}/renew-credential | Generate a new password for an API user
[**update_api_user**](ApiUsersApi.md#update_api_user) | **PUT** /api-users/{id} | Update an API user

# **add_profile_to_api_user**
> add_profile_to_api_user(body, id)

Associate profiles to an API user.

Associate new profiles to a given API user.

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
api_instance = sigfox_api_client.ApiUsersApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.ProfileIds() # ProfileIds | The API profile to update
id = 'id_example' # str | The API user identifier

try:
    # Associate profiles to an API user.
    api_instance.add_profile_to_api_user(body, id)
except ApiException as e:
    print("Exception when calling ApiUsersApi->add_profile_to_api_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProfileIds**](ProfileIds.md)| The API profile to update | 
 **id** | **str**| The API user identifier | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_user**
> object create_api_user(body)

Create an API user

Create a new API user. 

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
api_instance = sigfox_api_client.ApiUsersApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.ApiUserCreation() # ApiUserCreation | 

try:
    # Create an API user
    api_response = api_instance.create_api_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiUsersApi->create_api_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiUserCreation**](ApiUserCreation.md)|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_user**
> delete_api_user(id)

Delete an API user

Delete a given API user. 

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
api_instance = sigfox_api_client.ApiUsersApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The API user identifier

try:
    # Delete an API user
    api_instance.delete_api_user(id)
except ApiException as e:
    print("Exception when calling ApiUsersApi->delete_api_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The API user identifier | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_profile_of_api_user**
> delete_profile_of_api_user(id, profile_id)

Delete a profile to a given API user.

Delete a profile to a given API user. 

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
api_instance = sigfox_api_client.ApiUsersApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The API user identifier
profile_id = 'profile_id_example' # str | The profile identifier

try:
    # Delete a profile to a given API user.
    api_instance.delete_profile_of_api_user(id, profile_id)
except ApiException as e:
    print("Exception when calling ApiUsersApi->delete_profile_of_api_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The API user identifier | 
 **profile_id** | **str**| The profile identifier | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_user**
> ApiUser get_api_user(id, fields=fields)

Retrieve information about an API user

Retrieve information about a given API user. 

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
api_instance = sigfox_api_client.ApiUsersApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The API user identifier
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)

try:
    # Retrieve information about an API user
    api_response = api_instance.get_api_user(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiUsersApi->get_api_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The API user identifier | 
 **fields** | **str**| Defines the other available fields to be returned in the response.  | [optional] 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_users**
> object list_api_users(fields=fields, profile_id=profile_id, group_ids=group_ids, limit=limit, offset=offset)

Retrieve a list of API users

Retrieve a list of API users according to visibility permissions and request filters. 

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
api_instance = sigfox_api_client.ApiUsersApi(sigfox_api_client.ApiClient(configuration))
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)
profile_id = 'profile_id_example' # str | Searches for API users with the given profile (optional)
group_ids = ['group_ids_example'] # list[str] | Searches for API users who are attached to the given groups (optional)
limit = 56 # int | Defines the maximum number of items to return (optional)
offset = 56 # int | Defines the number of items to skip (optional)

try:
    # Retrieve a list of API users
    api_response = api_instance.list_api_users(fields=fields, profile_id=profile_id, group_ids=group_ids, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiUsersApi->list_api_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Defines the other available fields to be returned in the response.  | [optional] 
 **profile_id** | **str**| Searches for API users with the given profile | [optional] 
 **group_ids** | [**list[str]**](str.md)| Searches for API users who are attached to the given groups | [optional] 
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

# **renew_credential**
> object renew_credential(id)

Generate a new password for an API user

Generate a new password for a given API user. 

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
api_instance = sigfox_api_client.ApiUsersApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The API user identifier

try:
    # Generate a new password for an API user
    api_response = api_instance.renew_credential(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiUsersApi->renew_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The API user identifier | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_user**
> update_api_user(body, id)

Update an API user

Update information about a given API user. 

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
api_instance = sigfox_api_client.ApiUsersApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.ApiUserEdition() # ApiUserEdition | The information to update
id = 'id_example' # str | The API user identifier

try:
    # Update an API user
    api_instance.update_api_user(body, id)
except ApiException as e:
    print("Exception when calling ApiUsersApi->update_api_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiUserEdition**](ApiUserEdition.md)| The information to update | 
 **id** | **str**| The API user identifier | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

