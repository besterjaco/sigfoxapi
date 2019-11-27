# sigfox_api_client.CoveragesApi

All URIs are relative to *https://api.sigfox.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**coverages_global_predictions_get**](CoveragesApi.md#coverages_global_predictions_get) | **GET** /coverages/global/predictions | Retrieve coverage predictions for any location.
[**coverages_global_predictions_post**](CoveragesApi.md#coverages_global_predictions_post) | **POST** /coverages/global/predictions | Retrieve coverage predictions for any batch of locations
[**coverages_operators_redundancy_get**](CoveragesApi.md#coverages_operators_redundancy_get) | **GET** /coverages/operators/redundancy | Retrieve coverage redundancy for an operator.

# **coverages_global_predictions_get**
> object coverages_global_predictions_get(lat, lng, radius=radius, group_id=group_id)

Retrieve coverage predictions for any location.

Get coverage margins for a selected latitude and longitude, for each redundancy level. 

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
api_instance = sigfox_api_client.CoveragesApi(sigfox_api_client.ApiClient(configuration))
lat = 1.2 # float | the latitude
lng = 1.2 # float | the longitude
radius = 56 # int | The radius of the area in which the coverage results are averaged and returned for a selected location, in meters. (optional)
group_id = 'group_id_example' # str | the id of a group to include its operator in the global coverage (optional)

try:
    # Retrieve coverage predictions for any location.
    api_response = api_instance.coverages_global_predictions_get(lat, lng, radius=radius, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoveragesApi->coverages_global_predictions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| the latitude | 
 **lng** | **float**| the longitude | 
 **radius** | **int**| The radius of the area in which the coverage results are averaged and returned for a selected location, in meters. | [optional] 
 **group_id** | **str**| the id of a group to include its operator in the global coverage | [optional] 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coverages_global_predictions_post**
> GlobalCoverageResponse coverages_global_predictions_post(body)

Retrieve coverage predictions for any batch of locations

Get the coverage margins for multiple points, for each redundancy level. 

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
api_instance = sigfox_api_client.CoveragesApi(sigfox_api_client.ApiClient(configuration))
body = sigfox_api_client.GlobalCoverageRequest() # GlobalCoverageRequest | 

try:
    # Retrieve coverage predictions for any batch of locations
    api_response = api_instance.coverages_global_predictions_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoveragesApi->coverages_global_predictions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GlobalCoverageRequest**](GlobalCoverageRequest.md)|  | 

### Return type

[**GlobalCoverageResponse**](GlobalCoverageResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coverages_operators_redundancy_get**
> RedundancyResponse coverages_operators_redundancy_get(lat, lng, operator_id=operator_id, device_situation=device_situation, device_class_id=device_class_id)

Retrieve coverage redundancy for an operator.

Get operator coverage redundancy for a selected latitude and longitude, for specific device situation 

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
api_instance = sigfox_api_client.CoveragesApi(sigfox_api_client.ApiClient(configuration))
lat = 1.2 # float | the latitude
lng = 1.2 # float | the longitude
operator_id = 'operator_id_example' # str | The group id related to the operator to get its coverage result. Is required for root sigfox users.  (optional)
device_situation = 'device_situation_example' # str | The coverage mode. - OUTDOOR, max link budget - INDOOR, link budget with 20dB margin - UNDERGROUND, link budget with 30dB margin  (optional)
device_class_id = 56 # int | The product uplink class from 0 to 3 (0U to 3U). (optional)

try:
    # Retrieve coverage redundancy for an operator.
    api_response = api_instance.coverages_operators_redundancy_get(lat, lng, operator_id=operator_id, device_situation=device_situation, device_class_id=device_class_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoveragesApi->coverages_operators_redundancy_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| the latitude | 
 **lng** | **float**| the longitude | 
 **operator_id** | **str**| The group id related to the operator to get its coverage result. Is required for root sigfox users.  | [optional] 
 **device_situation** | **str**| The coverage mode. - OUTDOOR, max link budget - INDOOR, link budget with 20dB margin - UNDERGROUND, link budget with 30dB margin  | [optional] 
 **device_class_id** | **int**| The product uplink class from 0 to 3 (0U to 3U). | [optional] 

### Return type

[**RedundancyResponse**](RedundancyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

