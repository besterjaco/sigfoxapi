# sigfox_api_client.DevicesApi

All URIs are relative to *https://api.sigfox.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bulk_device**](DevicesApi.md#create_bulk_device) | **POST** /devices/bulk | Create multiple devices
[**create_device**](DevicesApi.md#create_device) | **POST** /devices/ | Create a device
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /devices/{id} | Delete a device
[**device_bulk_edit_async**](DevicesApi.md#device_bulk_edit_async) | **PUT** /devices/bulk | Update multiple devices
[**device_bulk_transfer**](DevicesApi.md#device_bulk_transfer) | **POST** /devices/bulk/transfer | Transfer multiple devices to another device type
[**device_bulk_unsubscribe**](DevicesApi.md#device_bulk_unsubscribe) | **POST** /devices/bulk/unsubscribe | Unsubscribe multiple devices
[**device_seq_number_disengage**](DevicesApi.md#device_seq_number_disengage) | **POST** /devices/{id}/disengage | Disengage sequence number check for the next message
[**devices_bulk_replace**](DevicesApi.md#devices_bulk_replace) | **POST** /devices/bulk/replace | Replace multiple devices
[**devices_bulk_restart**](DevicesApi.md#devices_bulk_restart) | **POST** /devices/bulk/restart | Restart multiple devices
[**devices_bulk_resume**](DevicesApi.md#devices_bulk_resume) | **POST** /devices/bulk/resume | Resume multiple devices
[**devices_bulk_suspend**](DevicesApi.md#devices_bulk_suspend) | **POST** /devices/bulk/suspend | Suspend multiple devices
[**devices_id_consumption_year_get**](DevicesApi.md#devices_id_consumption_year_get) | **GET** /devices/{id}/consumption/{year} | Retrieve a device&#x27;s consumption for a year
[**devices_id_consumption_year_month_get**](DevicesApi.md#devices_id_consumption_year_month_get) | **GET** /devices/{id}/consumption/{year}/{month} | Get a Device&#x27;s consumption for a given month
[**devices_id_messages_metric_get**](DevicesApi.md#devices_id_messages_metric_get) | **GET** /devices/{id}/messages/metric | Retreive the number of messages
[**get_bulk_job_for_device**](DevicesApi.md#get_bulk_job_for_device) | **GET** /devices/bulk/{jobId} | Retrieve the status of a job
[**get_bulk_restart_job**](DevicesApi.md#get_bulk_restart_job) | **GET** /devices/bulk/restart/{jobId} | Retrieve the async job status for a restart action.
[**get_bulk_resume_job**](DevicesApi.md#get_bulk_resume_job) | **GET** /devices/bulk/resume/{jobId} | Retrieve the status of a resume job
[**get_bulk_suspend_job**](DevicesApi.md#get_bulk_suspend_job) | **GET** /devices/bulk/suspend/{jobId} | Retrieve the status of a suspend job
[**get_callback_messages_error_list_for_device**](DevicesApi.md#get_callback_messages_error_list_for_device) | **GET** /devices/{id}/callbacks-not-delivered | Retrieve a list of undelivered callbacks
[**get_device**](DevicesApi.md#get_device) | **GET** /devices/{id} | Retrieve information about a device
[**get_device_locations_list**](DevicesApi.md#get_device_locations_list) | **GET** /devices/{id}/locations | Retrieve the locations of a device
[**get_device_messages_list_for_device**](DevicesApi.md#get_device_messages_list_for_device) | **GET** /devices/{id}/messages | Retrieve a list of messages
[**get_device_unsubscribe_job**](DevicesApi.md#get_device_unsubscribe_job) | **GET** /devices/bulk/unsubscribe/{jobId} | Retrieve the async job status for an unsubscribe action.
[**get_modem_certificate_info**](DevicesApi.md#get_modem_certificate_info) | **GET** /devices/{id}/certificate/modem | Retrieve the modem certificate associated with a device
[**get_product_certificate_info**](DevicesApi.md#get_product_certificate_info) | **GET** /devices/{id}/certificate/product | Retrieve the product certificate associated with a device
[**get_product_certificate_info_with_pac**](DevicesApi.md#get_product_certificate_info_with_pac) | **GET** /devices/{id}/product-certificate | Retrieve the product certificate associated with a device ID and PAC
[**list_devices**](DevicesApi.md#list_devices) | **GET** /devices/ | Retrieve a list of devices
[**unsubscribe**](DevicesApi.md#unsubscribe) | **PUT** /devices/{id}/unsubscribe | Unsubscribe a device
[**update_device**](DevicesApi.md#update_device) | **PUT** /devices/{id} | Update a device

# **create_bulk_device**
> object create_bulk_device(body)

Create multiple devices

Create multiple new devices with asynchronous job 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.AsynchronousDeviceCreationJob() # AsynchronousDeviceCreationJob | The devices to create

try:
    # Create multiple devices
    api_response = api_instance.create_bulk_device(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_bulk_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AsynchronousDeviceCreationJob**](AsynchronousDeviceCreationJob.md)| The devices to create | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device**
> object create_device(body)

Create a device

Create a new device. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.DeviceCreationJob() # DeviceCreationJob | The device to create

try:
    # Create a device
    api_response = api_instance.create_device(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceCreationJob**](DeviceCreationJob.md)| The device to create | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> delete_device(id)

Delete a device

Delete a given device. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device identifier (hexadecimal format)

try:
    # Delete a device
    api_instance.delete_device(id)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device identifier (hexadecimal format) | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_bulk_edit_async**
> object device_bulk_edit_async(body)

Update multiple devices

Update or edit multiple devices with asynchronous job. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.AsynchronousDeviceEditionJob() # AsynchronousDeviceEditionJob | The devices to edit

try:
    # Update multiple devices
    api_response = api_instance.device_bulk_edit_async(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_bulk_edit_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AsynchronousDeviceEditionJob**](AsynchronousDeviceEditionJob.md)| The devices to edit | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_bulk_transfer**
> object device_bulk_transfer(body)

Transfer multiple devices to another device type

Transfer multiple devices to another device type with asynchronous job 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.AsynchronousDeviceTransferJob() # AsynchronousDeviceTransferJob | The devices to move

try:
    # Transfer multiple devices to another device type
    api_response = api_instance.device_bulk_transfer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_bulk_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AsynchronousDeviceTransferJob**](AsynchronousDeviceTransferJob.md)| The devices to move | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_bulk_unsubscribe**
> object device_bulk_unsubscribe(body)

Unsubscribe multiple devices

Unsubscribe multiple devices with asynchronous job. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.BulkUnsubscribe() # BulkUnsubscribe | array of device's identifier (hexadecimal format) with unsubscribtion time

try:
    # Unsubscribe multiple devices
    api_response = api_instance.device_bulk_unsubscribe(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_bulk_unsubscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkUnsubscribe**](BulkUnsubscribe.md)| array of device&#x27;s identifier (hexadecimal format) with unsubscribtion time | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_seq_number_disengage**
> device_seq_number_disengage(id)

Disengage sequence number check for the next message

Disable sequence number check for the next message. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device identifier (hexadecimal format)

try:
    # Disengage sequence number check for the next message
    api_instance.device_seq_number_disengage(id)
except ApiException as e:
    print("Exception when calling DevicesApi->device_seq_number_disengage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device identifier (hexadecimal format) | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_bulk_replace**
> ReplaceResponse devices_bulk_replace(body=body)

Replace multiple devices

Replace multiple devices (moving tokens from one device to another) with synchronous job 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.AsynchronousDeviceReplacementJob() # AsynchronousDeviceReplacementJob | Pairs of source and target devices (optional)

try:
    # Replace multiple devices
    api_response = api_instance.devices_bulk_replace(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_bulk_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AsynchronousDeviceReplacementJob**](AsynchronousDeviceReplacementJob.md)| Pairs of source and target devices | [optional] 

### Return type

[**ReplaceResponse**](ReplaceResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_bulk_restart**
> object devices_bulk_restart(body)

Restart multiple devices

Restart multiple devices with asynchronous job. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.DeviceActionJob() # DeviceActionJob | list of device's identifier (hexadecimal format)

try:
    # Restart multiple devices
    api_response = api_instance.devices_bulk_restart(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_bulk_restart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceActionJob**](DeviceActionJob.md)| list of device&#x27;s identifier (hexadecimal format) | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_bulk_resume**
> object devices_bulk_resume(body)

Resume multiple devices

Resume multiple devices with asynchronous job. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.DeviceActionJob() # DeviceActionJob | list of device's identifier (hexadecimal format)

try:
    # Resume multiple devices
    api_response = api_instance.devices_bulk_resume(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_bulk_resume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceActionJob**](DeviceActionJob.md)| list of device&#x27;s identifier (hexadecimal format) | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_bulk_suspend**
> object devices_bulk_suspend(body)

Suspend multiple devices

Suspend multiple devices with asynchronous job 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.DeviceActionJob() # DeviceActionJob | list of device's identifier (hexadecimal format)

try:
    # Suspend multiple devices
    api_response = api_instance.devices_bulk_suspend(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_bulk_suspend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceActionJob**](DeviceActionJob.md)| list of device&#x27;s identifier (hexadecimal format) | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_consumption_year_get**
> DeviceConsumption devices_id_consumption_year_get(id, year)

Retrieve a device's consumption for a year

Retrieve a device's consumption for a given year. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device identifier (hexadecimal format)
year = 56 # int | The year of consumption

try:
    # Retrieve a device's consumption for a year
    api_response = api_instance.devices_id_consumption_year_get(id, year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_id_consumption_year_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device identifier (hexadecimal format) | 
 **year** | **int**| The year of consumption | 

### Return type

[**DeviceConsumption**](DeviceConsumption.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_consumption_year_month_get**
> DeviceConsumption devices_id_consumption_year_month_get(id, year, month)

Get a Device's consumption for a given month

Retrieve a device's consumption for a given month during a given year. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device identifier (hexadecimal format)
year = 56 # int | The year of consumption
month = 56 # int | The month of consumption

try:
    # Get a Device's consumption for a given month
    api_response = api_instance.devices_id_consumption_year_month_get(id, year, month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_id_consumption_year_month_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device identifier (hexadecimal format) | 
 **year** | **int**| The year of consumption | 
 **month** | **int**| The month of consumption | 

### Return type

[**DeviceConsumption**](DeviceConsumption.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_messages_metric_get**
> object devices_id_messages_metric_get(id)

Retreive the number of messages

Return the number of messages for a given device, for the last day, last week and last month. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device identifier (hexadecimal format)

try:
    # Retreive the number of messages
    api_response = api_instance.devices_id_messages_metric_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_id_messages_metric_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device identifier (hexadecimal format) | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_job_for_device**
> RegistrationJobStatus get_bulk_job_for_device(job_id)

Retrieve the status of a job

Retrieve the status of an asynchronous job for devices. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job identidier (hexademical format)

try:
    # Retrieve the status of a job
    api_response = api_instance.get_bulk_job_for_device(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_bulk_job_for_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job identidier (hexademical format) | 

### Return type

[**RegistrationJobStatus**](RegistrationJobStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_restart_job**
> ActionJob get_bulk_restart_job(job_id)

Retrieve the async job status for a restart action.

Retrieve the async job status for a restart devices action. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job identidier (hexademical format)

try:
    # Retrieve the async job status for a restart action.
    api_response = api_instance.get_bulk_restart_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_bulk_restart_job: %s\n" % e)
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

# **get_bulk_resume_job**
> ActionJob get_bulk_resume_job(job_id)

Retrieve the status of a resume job

Retrieve the async job status for a resume devices action. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job identidier (hexademical format)

try:
    # Retrieve the status of a resume job
    api_response = api_instance.get_bulk_resume_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_bulk_resume_job: %s\n" % e)
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

# **get_bulk_suspend_job**
> ActionJob get_bulk_suspend_job(job_id)

Retrieve the status of a suspend job

Retrieve the async job status for a suspend devices action. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job identidier (hexademical format)

try:
    # Retrieve the status of a suspend job
    api_response = api_instance.get_bulk_suspend_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_bulk_suspend_job: %s\n" % e)
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

# **get_callback_messages_error_list_for_device**
> object get_callback_messages_error_list_for_device(id, since=since, before=before, limit=limit, offset=offset)

Retrieve a list of undelivered callbacks

Retrieve a list of undelivered callbacks and errors for a given device, in reverse chronological order (most recent message first). 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device identifier (hexadecimal format)
since = 789 # int | Starting timestamp (in milliseconds since the Unix Epoch) (optional)
before = 789 # int | Ending timestamp (in milliseconds since the Unix Epoch) (optional)
limit = 56 # int | The maximum number of items to return (optional)
offset = 56 # int | The number of items to skip (optional)

try:
    # Retrieve a list of undelivered callbacks
    api_response = api_instance.get_callback_messages_error_list_for_device(id, since=since, before=before, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_callback_messages_error_list_for_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device identifier (hexadecimal format) | 
 **since** | **int**| Starting timestamp (in milliseconds since the Unix Epoch) | [optional] 
 **before** | **int**| Ending timestamp (in milliseconds since the Unix Epoch) | [optional] 
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

# **get_device**
> Device get_device(id, fields=fields)

Retrieve information about a device

Retrieve information about a given device. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device identifier (hexadecimal format)
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)

try:
    # Retrieve information about a device
    api_response = api_instance.get_device(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device identifier (hexadecimal format) | 
 **fields** | **str**| Defines the other available fields to be returned in the response.  | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_locations_list**
> object get_device_locations_list(id, oob=oob, since=since, before=before, limit=limit, offset=offset)

Retrieve the locations of a device

Retrieve a list of location data of a device according to request filters. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device identifier (hexadecimal format)
oob = true # bool | if true, the method return also the location from out of band Messages (optional)
since = 789 # int | Starting timestamp (in milliseconds since the Unix Epoch) (optional)
before = 789 # int | Ending timestamp (in milliseconds since the Unix Epoch) (optional)
limit = 56 # int | The maximum number of items to return (optional)
offset = 56 # int | The number of items to skip (optional)

try:
    # Retrieve the locations of a device
    api_response = api_instance.get_device_locations_list(id, oob=oob, since=since, before=before, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_locations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device identifier (hexadecimal format) | 
 **oob** | **bool**| if true, the method return also the location from out of band Messages | [optional] 
 **since** | **int**| Starting timestamp (in milliseconds since the Unix Epoch) | [optional] 
 **before** | **int**| Ending timestamp (in milliseconds since the Unix Epoch) | [optional] 
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

# **get_device_messages_list_for_device**
> object get_device_messages_list_for_device(id, fields=fields, since=since, before=before, limit=limit, offset=offset)

Retrieve a list of messages

Retrieve a list of messages for a given device according to request filters, with a 3-day history. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device identifier (hexadecimal format)
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)
since = 789 # int | Starting timestamp (in milliseconds since the Unix Epoch) (optional)
before = 789 # int | Ending timestamp (in milliseconds since the Unix Epoch) (optional)
limit = 56 # int | The maximum number of items to return (optional)
offset = 56 # int | The number of items to skip (optional)

try:
    # Retrieve a list of messages
    api_response = api_instance.get_device_messages_list_for_device(id, fields=fields, since=since, before=before, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_messages_list_for_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device identifier (hexadecimal format) | 
 **fields** | **str**| Defines the other available fields to be returned in the response.  | [optional] 
 **since** | **int**| Starting timestamp (in milliseconds since the Unix Epoch) | [optional] 
 **before** | **int**| Ending timestamp (in milliseconds since the Unix Epoch) | [optional] 
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

# **get_device_unsubscribe_job**
> ActionJob get_device_unsubscribe_job(job_id)

Retrieve the async job status for an unsubscribe action.

Retrieve the async job status for an unsubscribe devices action. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job identidier (hexademical format)

try:
    # Retrieve the async job status for an unsubscribe action.
    api_response = api_instance.get_device_unsubscribe_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_unsubscribe_job: %s\n" % e)
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

# **get_modem_certificate_info**
> ModemCertificate get_modem_certificate_info(id, fields=fields)

Retrieve the modem certificate associated with a device

Retrieve the modem certificate associated with a device. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device identifier (hexadecimal format)
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)

try:
    # Retrieve the modem certificate associated with a device
    api_response = api_instance.get_modem_certificate_info(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_modem_certificate_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device identifier (hexadecimal format) | 
 **fields** | **str**| Defines the other available fields to be returned in the response.  | [optional] 

### Return type

[**ModemCertificate**](ModemCertificate.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_certificate_info**
> ProductCertificate get_product_certificate_info(id, fields=fields)

Retrieve the product certificate associated with a device

Retrieve the product certificate associated with a device already registered. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device identifier (hexadecimal format)
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)

try:
    # Retrieve the product certificate associated with a device
    api_response = api_instance.get_product_certificate_info(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_product_certificate_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device identifier (hexadecimal format) | 
 **fields** | **str**| Defines the other available fields to be returned in the response.  | [optional] 

### Return type

[**ProductCertificate**](ProductCertificate.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_certificate_info_with_pac**
> ProductCertificateWithPacResponse get_product_certificate_info_with_pac(id, pac)

Retrieve the product certificate associated with a device ID and PAC

Retrieve the product certificate associated with a given device ID and PAC, when the device has not already been created on the portal, only in CRA 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The Device identifier (hexadecimal format)
pac = 'pac_example' # str | The device's PAC (hexadecimal format)

try:
    # Retrieve the product certificate associated with a device ID and PAC
    api_response = api_instance.get_product_certificate_info_with_pac(id, pac)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_product_certificate_info_with_pac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Device identifier (hexadecimal format) | 
 **pac** | **str**| The device&#x27;s PAC (hexadecimal format) | 

### Return type

[**ProductCertificateWithPacResponse**](ProductCertificateWithPacResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_devices**
> object list_devices(id=id, group_ids=group_ids, deep=deep, device_type_id=device_type_id, operator_id=operator_id, sort=sort, min_id=min_id, max_id=max_id, fields=fields, limit=limit, offset=offset, page_id=page_id)

Retrieve a list of devices

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
id = 'id_example' # str | The device's identifier (hexadecimal format) (optional)
group_ids = ['group_ids_example'] # list[str] | Returns all devices under the given groups (included sub-groups if the parameter deep is equals to true) (optional)
deep = true # bool | if true, we search by groups and subgroups through the parameter 'groupIds' (optional)
device_type_id = 'device_type_id_example' # str | Returns all devices of the given device type (optional)
operator_id = 'operator_id_example' # str | Returns all devices under the given operator (optional)
sort = 'sort_example' # str | The field on which the list will be sorted. (field to sort ascending or -field to sort descending) (optional)
min_id = 'min_id_example' # str | The minimal id of the filtered range, only availble when sort parameter is set to \"id\" or \"-id\" (optional)
max_id = 'max_id_example' # str | The maximal id of the filtered range, only availble when sort parameter is set to \"id\" or \"-id\" (optional)
fields = 'fields_example' # str | Defines the other available fields to be returned in the response.  (optional)
limit = 56 # int | The maximum number of items to return (optional)
offset = 56 # int | The number of items to skip (optional)
page_id = 'page_id_example' # str | Token representing the page to retrieve (optional)

try:
    # Retrieve a list of devices
    api_response = api_instance.list_devices(id=id, group_ids=group_ids, deep=deep, device_type_id=device_type_id, operator_id=operator_id, sort=sort, min_id=min_id, max_id=max_id, fields=fields, limit=limit, offset=offset, page_id=page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->list_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The device&#x27;s identifier (hexadecimal format) | [optional] 
 **group_ids** | [**list[str]**](str.md)| Returns all devices under the given groups (included sub-groups if the parameter deep is equals to true) | [optional] 
 **deep** | **bool**| if true, we search by groups and subgroups through the parameter &#x27;groupIds&#x27; | [optional] 
 **device_type_id** | **str**| Returns all devices of the given device type | [optional] 
 **operator_id** | **str**| Returns all devices under the given operator | [optional] 
 **sort** | **str**| The field on which the list will be sorted. (field to sort ascending or -field to sort descending) | [optional] 
 **min_id** | **str**| The minimal id of the filtered range, only availble when sort parameter is set to \&quot;id\&quot; or \&quot;-id\&quot; | [optional] 
 **max_id** | **str**| The maximal id of the filtered range, only availble when sort parameter is set to \&quot;id\&quot; or \&quot;-id\&quot; | [optional] 
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

# **unsubscribe**
> unsubscribe(body, id)

Unsubscribe a device

Set an unsubscription date for the device's token. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.TokenUnsubscribe() # TokenUnsubscribe | the unsubscription time (in milliseconds since the Unix Epoch)
id = 'id_example' # str | The Device identifier (hexadecimal format)

try:
    # Unsubscribe a device
    api_instance.unsubscribe(body, id)
except ApiException as e:
    print("Exception when calling DevicesApi->unsubscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenUnsubscribe**](TokenUnsubscribe.md)| the unsubscription time (in milliseconds since the Unix Epoch) | 
 **id** | **str**| The Device identifier (hexadecimal format) | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> update_device(body, id)

Update a device

Update a given device. 

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
api_instance = sigfox_api_client.DevicesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.DeviceUpdateJob() # DeviceUpdateJob | The device to update
id = 'id_example' # str | The Device identifier (hexadecimal format)

try:
    # Update a device
    api_instance.update_device(body, id)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceUpdateJob**](DeviceUpdateJob.md)| The device to update | 
 **id** | **str**| The Device identifier (hexadecimal format) | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

