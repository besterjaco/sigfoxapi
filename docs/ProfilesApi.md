# sigfox_api_client.ProfilesApi

All URIs are relative to *https://api.sigfox.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listprofiles**](ProfilesApi.md#listprofiles) | **GET** /profiles/ | Retrieve a list of profiles

# **listprofiles**
> object listprofiles(group_id, inherit=inherit, fields=fields, limit=limit, offset=offset)

Retrieve a list of profiles

Retrieve a list of a Group's profiles according to visibility permissions and request filters. 

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
api_instance = sigfox_api_client.ProfilesApi(sigfox_api_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group's identifier
inherit = true # bool | also returns profiles inherited from parent's group (optional)
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)
limit = 56 # int | The maximum number of items to return (optional)
offset = 56 # int | The number of items to skip (optional)

try:
    # Retrieve a list of profiles
    api_response = api_instance.listprofiles(group_id, inherit=inherit, fields=fields, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilesApi->listprofiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group&#x27;s identifier | 
 **inherit** | **bool**| also returns profiles inherited from parent&#x27;s group | [optional] 
 **fields** | **str**| Defines the other available fields to be returned in the response.  | [optional] 
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

