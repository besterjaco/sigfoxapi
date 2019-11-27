# sigfox_api_client.TilesApi

All URIs are relative to *https://api.sigfox.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kmz_create_monarch**](TilesApi.md#kmz_create_monarch) | **POST** /tiles/monarch/kmz | Compute Sigfox Monarch coverage in order to allow export as kmz file
[**kmz_create_public_operator**](TilesApi.md#kmz_create_public_operator) | **POST** /tiles/public-operator/{groupId}/kmz | Compute Sigfox Public operator public coverage in order to allow export as kmz file
[**kmz_file_monarch**](TilesApi.md#kmz_file_monarch) | **GET** /tiles/monarch/kmz/{jobId}/tiles.kmz | Retrieve Sigfox Monarch coverage kmz file
[**kmz_file_public_coverage**](TilesApi.md#kmz_file_public_coverage) | **GET** /tiles/public-coverage/kmz/tiles.kmz | Retrieve Sigfox public coverage kmz file
[**kmz_file_public_operator**](TilesApi.md#kmz_file_public_operator) | **GET** /tiles/public-operator/{groupId}/kmz/{jobId}/tiles.kmz | Retrieve Sigfox public Operator coverage kmz file
[**kmz_status_monarch**](TilesApi.md#kmz_status_monarch) | **GET** /tiles/monarch/kmz/{jobId} | Retrieve Sigfox Monarch coverage kmz computed job results
[**kmz_status_public_operator**](TilesApi.md#kmz_status_public_operator) | **GET** /tiles/public-operator/{groupId}/kmz/{jobId} | Retrieve Sigfox public Operator coverage kmz computed job results
[**tiles_monarch_get**](TilesApi.md#tiles_monarch_get) | **GET** /tiles/monarch | Retrieve the information needed to display Sigfox Monarch service coverage.
[**tiles_public_coverage_get**](TilesApi.md#tiles_public_coverage_get) | **GET** /tiles/public-coverage | Retrieve the information needed to display Sigfox public coverage.

# **kmz_create_monarch**
> object kmz_create_monarch(body)

Compute Sigfox Monarch coverage in order to allow export as kmz file

Starting the computation of Sigfox Monarch coverage view for a specific coverage mode. A new computation starts if no other computation, run in the last 24 hours, is available. Otherwise, the existing jobId is returned. 

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
api_instance = sigfox_api_client.TilesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.KmzCreatePublicRequest() # KmzCreatePublicRequest | The computation will be performed with the specified coverage mode

try:
    # Compute Sigfox Monarch coverage in order to allow export as kmz file
    api_response = api_instance.kmz_create_monarch(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TilesApi->kmz_create_monarch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmzCreatePublicRequest**](KmzCreatePublicRequest.md)| The computation will be performed with the specified coverage mode | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmz_create_public_operator**
> object kmz_create_public_operator(body, group_id)

Compute Sigfox Public operator public coverage in order to allow export as kmz file

Starting the computation of Sigfox public operator coverage view for a specific coverage mode. A new computation starts if no other computation, run in the last 24 hours, is available. Otherwise, the existing jobId is returned. 

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
api_instance = sigfox_api_client.TilesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.KmzCreatePublicRequest() # KmzCreatePublicRequest | The computation will be performed with the specified coverage mode
group_id = 'group_id_example' # str | The operator's group identifier (hexadecimal format)

try:
    # Compute Sigfox Public operator public coverage in order to allow export as kmz file
    api_response = api_instance.kmz_create_public_operator(body, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TilesApi->kmz_create_public_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmzCreatePublicRequest**](KmzCreatePublicRequest.md)| The computation will be performed with the specified coverage mode | 
 **group_id** | **str**| The operator&#x27;s group identifier (hexadecimal format) | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmz_file_monarch**
> kmz_file_monarch(job_id, zoom, north, south, west, east)

Retrieve Sigfox Monarch coverage kmz file

Retrieve Sigfox Monarch coverage kmz from a job 

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
api_instance = sigfox_api_client.TilesApi(sigfox_api_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job's identifier (hexademical format)
zoom = 56 # int | The zoom level used to generate kmz file
north = 1.2 # float | The north boundary to extract coverage
south = 1.2 # float | The south boundary to extract coverage
west = 1.2 # float | The west boundary to extract coverage
east = 1.2 # float | The east boundary to extract coverage

try:
    # Retrieve Sigfox Monarch coverage kmz file
    api_instance.kmz_file_monarch(job_id, zoom, north, south, west, east)
except ApiException as e:
    print("Exception when calling TilesApi->kmz_file_monarch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job&#x27;s identifier (hexademical format) | 
 **zoom** | **int**| The zoom level used to generate kmz file | 
 **north** | **float**| The north boundary to extract coverage | 
 **south** | **float**| The south boundary to extract coverage | 
 **west** | **float**| The west boundary to extract coverage | 
 **east** | **float**| The east boundary to extract coverage | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.google-earth.kmz

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmz_file_public_coverage**
> kmz_file_public_coverage(zoom, north, south, west, east)

Retrieve Sigfox public coverage kmz file

Retrieve Sigfox public coverage kmz file from a job. The public coverage is always available and does not require a previous calculation 

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
api_instance = sigfox_api_client.TilesApi(sigfox_api_client.ApiClient(configuration))
zoom = 56 # int | The zoom level used to generate kmz file
north = 1.2 # float | The north boundary to extract coverage
south = 1.2 # float | The south boundary to extract coverage
west = 1.2 # float | The west boundary to extract coverage
east = 1.2 # float | The east boundary to extract coverage

try:
    # Retrieve Sigfox public coverage kmz file
    api_instance.kmz_file_public_coverage(zoom, north, south, west, east)
except ApiException as e:
    print("Exception when calling TilesApi->kmz_file_public_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zoom** | **int**| The zoom level used to generate kmz file | 
 **north** | **float**| The north boundary to extract coverage | 
 **south** | **float**| The south boundary to extract coverage | 
 **west** | **float**| The west boundary to extract coverage | 
 **east** | **float**| The east boundary to extract coverage | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.google-earth.kmz

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmz_file_public_operator**
> kmz_file_public_operator(group_id, job_id, zoom, north, south, west, east)

Retrieve Sigfox public Operator coverage kmz file

Retrieve Sigfox public Operator coverage kmz from a job 

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
api_instance = sigfox_api_client.TilesApi(sigfox_api_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The operator's group identifier (hexadecimal format)
job_id = 'job_id_example' # str | The job's identifier (hexademical format)
zoom = 56 # int | The zoom level used to generate kmz file
north = 1.2 # float | The north boundary to extract coverage
south = 1.2 # float | The south boundary to extract coverage
west = 1.2 # float | The west boundary to extract coverage
east = 1.2 # float | The east boundary to extract coverage

try:
    # Retrieve Sigfox public Operator coverage kmz file
    api_instance.kmz_file_public_operator(group_id, job_id, zoom, north, south, west, east)
except ApiException as e:
    print("Exception when calling TilesApi->kmz_file_public_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The operator&#x27;s group identifier (hexadecimal format) | 
 **job_id** | **str**| The job&#x27;s identifier (hexademical format) | 
 **zoom** | **int**| The zoom level used to generate kmz file | 
 **north** | **float**| The north boundary to extract coverage | 
 **south** | **float**| The south boundary to extract coverage | 
 **west** | **float**| The west boundary to extract coverage | 
 **east** | **float**| The east boundary to extract coverage | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.google-earth.kmz

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmz_status_monarch**
> KmzStatusResponse kmz_status_monarch(job_id)

Retrieve Sigfox Monarch coverage kmz computed job results

Retrieve Sigfox Monarch coverage kmz computation from asynchronous job status 

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
api_instance = sigfox_api_client.TilesApi(sigfox_api_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job's identifier (hexademical format)

try:
    # Retrieve Sigfox Monarch coverage kmz computed job results
    api_response = api_instance.kmz_status_monarch(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TilesApi->kmz_status_monarch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job&#x27;s identifier (hexademical format) | 

### Return type

[**KmzStatusResponse**](KmzStatusResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmz_status_public_operator**
> KmzStatusResponse kmz_status_public_operator(group_id, job_id)

Retrieve Sigfox public Operator coverage kmz computed job results

Retrieve Sigfox Sigfox public Operator coverage kmz computation from asynchronous job status 

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
api_instance = sigfox_api_client.TilesApi(sigfox_api_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The operator's group identifier (hexadecimal format)
job_id = 'job_id_example' # str | The job's identifier (hexademical format)

try:
    # Retrieve Sigfox public Operator coverage kmz computed job results
    api_response = api_instance.kmz_status_public_operator(group_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TilesApi->kmz_status_public_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The operator&#x27;s group identifier (hexadecimal format) | 
 **job_id** | **str**| The job&#x27;s identifier (hexademical format) | 

### Return type

[**KmzStatusResponse**](KmzStatusResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tiles_monarch_get**
> TilesResponse tiles_monarch_get()

Retrieve the information needed to display Sigfox Monarch service coverage.

Retrieve the information needed to display Sigfox Monarch service coverage. 

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
api_instance = sigfox_api_client.TilesApi(sigfox_api_client.ApiClient(configuration))

try:
    # Retrieve the information needed to display Sigfox Monarch service coverage.
    api_response = api_instance.tiles_monarch_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TilesApi->tiles_monarch_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TilesResponse**](TilesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tiles_public_coverage_get**
> TilesResponse tiles_public_coverage_get()

Retrieve the information needed to display Sigfox public coverage.

Retrieve the information needed to display Sigfox public coverage. 

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
api_instance = sigfox_api_client.TilesApi(sigfox_api_client.ApiClient(configuration))

try:
    # Retrieve the information needed to display Sigfox public coverage.
    api_response = api_instance.tiles_public_coverage_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TilesApi->tiles_public_coverage_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TilesResponse**](TilesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

