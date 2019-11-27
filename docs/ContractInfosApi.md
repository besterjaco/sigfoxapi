# sigfox_api_client.ContractInfosApi

All URIs are relative to *https://api.sigfox.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contract_bulk_restart**](ContractInfosApi.md#contract_bulk_restart) | **POST** /contract-infos/{id}/bulk/restart | Create a job to restart the devices associated to a contract
[**device_list**](ContractInfosApi.md#device_list) | **GET** /contract-infos/{id}/devices | Retrieve the list of devices having a token on the specified contract
[**get_contract_bulk_restart_job**](ContractInfosApi.md#get_contract_bulk_restart_job) | **GET** /contract-infos/bulk/restart/{jobId} | Retrieve a contract async job status for restart action
[**get_contract_info**](ContractInfosApi.md#get_contract_info) | **GET** /contract-infos/{id} | Retrieve information about a contract
[**list_contract_infos**](ContractInfosApi.md#list_contract_infos) | **GET** /contract-infos/ | Retrieve a list of contracts

# **contract_bulk_restart**
> object contract_bulk_restart(id)

Create a job to restart the devices associated to a contract

Create an async job to restart the devices associated to a contract. 

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
api_instance = sigfox_api_client.ContractInfosApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Contract identifier

try:
    # Create a job to restart the devices associated to a contract
    api_response = api_instance.contract_bulk_restart(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractInfosApi->contract_bulk_restart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Contract identifier | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_list**
> object device_list(id, device_type_id=device_type_id, fields=fields, limit=limit, page_id=page_id)

Retrieve the list of devices having a token on the specified contract

Retrieve a list of devices according to visibility permissions and request filters. 

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
api_instance = sigfox_api_client.ContractInfosApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The contract info ID
device_type_id = 'device_type_id_example' # str | Returns only devices of the given device type (optional)
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)
limit = 56 # int | The maximum number of items to return (optional)
page_id = 'page_id_example' # str | Token representing the page to retrieve (optional)

try:
    # Retrieve the list of devices having a token on the specified contract
    api_response = api_instance.device_list(id, device_type_id=device_type_id, fields=fields, limit=limit, page_id=page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractInfosApi->device_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The contract info ID | 
 **device_type_id** | **str**| Returns only devices of the given device type | [optional] 
 **fields** | **str**| Defines the other available fields to be returned in the response.  | [optional] 
 **limit** | **int**| The maximum number of items to return | [optional] 
 **page_id** | **str**| Token representing the page to retrieve | [optional] 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_bulk_restart_job**
> ActionJob get_contract_bulk_restart_job(job_id)

Retrieve a contract async job status for restart action

Retrieve a contract async job status for restart action. 

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
api_instance = sigfox_api_client.ContractInfosApi(sigfox_api_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job identidier (hexademical format)

try:
    # Retrieve a contract async job status for restart action
    api_response = api_instance.get_contract_bulk_restart_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractInfosApi->get_contract_bulk_restart_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job identidier (hexademical format) | 

### Return type

[**ActionJob**](ActionJob.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_info**
> ContractInfo get_contract_info(id, fields=fields)

Retrieve information about a contract

Retrieve information about a given contract. 

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
api_instance = sigfox_api_client.ContractInfosApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Contract identifier
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)

try:
    # Retrieve information about a contract
    api_response = api_instance.get_contract_info(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractInfosApi->get_contract_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Contract identifier | 
 **fields** | **str**| Defines the other available fields to be returned in the response.  | [optional] 

### Return type

[**ContractInfo**](ContractInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contract_infos**
> object list_contract_infos(name=name, group_id=group_id, group_type=group_type, deep=deep, order_ids=order_ids, contract_ids=contract_ids, from_time=from_time, to_time=to_time, token_duration=token_duration, pricing_model=pricing_model, subscription_plan=subscription_plan, geolocation_mode=geolocation_mode, fields=fields, limit=limit, offset=offset, page_id=page_id)

Retrieve a list of contracts

Retrieve a list of contracts according to visibility permissions and request filters. 

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
api_instance = sigfox_api_client.ContractInfosApi(sigfox_api_client.ApiClient(configuration))
name = 'name_example' # str | Searches for contracts containing the given text in their name (optional)
group_id = 'group_id_example' # str | Searches for contracts who are attached to the given group (optional)
group_type = 56 # int | Searches for contracts that are attached to a specific group type. - 2 -> BASIC - 9 -> CHANNEL  (optional)
deep = true # bool | Searches for contracts that are attached to the given group and its descendants (optional)
order_ids = 'order_ids_example' # str | Searches for contracts with the listed orderIds. The elements of the list are separated by comma. (optional)
contract_ids = 'contract_ids_example' # str | Searches for contracts IDs that have the listed external (BSS) contractId. The elements of the list are separated by comma. (optional)
from_time = 789 # int | Searches for contracts starting after the given time (in milliseconds since Unix Epoch). (optional)
to_time = 789 # int | Searches for contracts ending before the given time (in milliseconds since Unix Epoch). (optional)
token_duration = 56 # int | Searches for contracts with the given token duration in months. (optional)
pricing_model = 56 # int | Searches for contracts with a given pricing model  1 -> Pricing model v1 2 -> Pricing model v2 3 -> Pricing model v3  (optional)
subscription_plan = 56 # int | Searches for contracts with the given subscription plan: 0 -> Free order 1 -> Pay As You Grow (PAYG) 2 -> Committed Volume Plan (CVP) 3 -> Flexible Committed Volume Plan (CVP Flex) 4 -> PACK 5 -> DevKit 6 -> Activate  (optional)
geolocation_mode = 56 # int | Searches for contracts with the given geolocation mode (level) 1 (ATLAS) 2 (ATLAS_WIFI) 3 (N/A) 4 (ATLAS_POV) 5 (ATLAS_BUBBLE)  (optional)
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)
limit = 56 # int | The maximum number of items to return (optional)
offset = 56 # int | The number of items to skip (optional)
page_id = 'page_id_example' # str | Token representing the page to retrieve (optional)

try:
    # Retrieve a list of contracts
    api_response = api_instance.list_contract_infos(name=name, group_id=group_id, group_type=group_type, deep=deep, order_ids=order_ids, contract_ids=contract_ids, from_time=from_time, to_time=to_time, token_duration=token_duration, pricing_model=pricing_model, subscription_plan=subscription_plan, geolocation_mode=geolocation_mode, fields=fields, limit=limit, offset=offset, page_id=page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractInfosApi->list_contract_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Searches for contracts containing the given text in their name | [optional] 
 **group_id** | **str**| Searches for contracts who are attached to the given group | [optional] 
 **group_type** | **int**| Searches for contracts that are attached to a specific group type. - 2 -&gt; BASIC - 9 -&gt; CHANNEL  | [optional] 
 **deep** | **bool**| Searches for contracts that are attached to the given group and its descendants | [optional] 
 **order_ids** | **str**| Searches for contracts with the listed orderIds. The elements of the list are separated by comma. | [optional] 
 **contract_ids** | **str**| Searches for contracts IDs that have the listed external (BSS) contractId. The elements of the list are separated by comma. | [optional] 
 **from_time** | **int**| Searches for contracts starting after the given time (in milliseconds since Unix Epoch). | [optional] 
 **to_time** | **int**| Searches for contracts ending before the given time (in milliseconds since Unix Epoch). | [optional] 
 **token_duration** | **int**| Searches for contracts with the given token duration in months. | [optional] 
 **pricing_model** | **int**| Searches for contracts with a given pricing model  1 -&gt; Pricing model v1 2 -&gt; Pricing model v2 3 -&gt; Pricing model v3  | [optional] 
 **subscription_plan** | **int**| Searches for contracts with the given subscription plan: 0 -&gt; Free order 1 -&gt; Pay As You Grow (PAYG) 2 -&gt; Committed Volume Plan (CVP) 3 -&gt; Flexible Committed Volume Plan (CVP Flex) 4 -&gt; PACK 5 -&gt; DevKit 6 -&gt; Activate  | [optional] 
 **geolocation_mode** | **int**| Searches for contracts with the given geolocation mode (level) 1 (ATLAS) 2 (ATLAS_WIFI) 3 (N/A) 4 (ATLAS_POV) 5 (ATLAS_BUBBLE)  | [optional] 
 **fields** | **str**| Defines the other available fields to be returned in the response.  | [optional] 
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

