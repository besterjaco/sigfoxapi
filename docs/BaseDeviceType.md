# BaseDeviceType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The device type&#x27;s name | [optional] 
**description** | **str** | The device type&#x27;s description | [optional] 
**downlink_mode** | **int** | The downlink mode to use for the devices of this device type - 0 -&gt; DIRECT - 1 -&gt; CALLBACK - 2 -&gt; NONE - 3 -&gt; MANAGED  | [optional] 
**downlink_data_string** | **str** | Downlink data to be sent to the devices of this device type if the downlinkMode is equal to 0. It must be an 8 byte length message given in hexadecimal string format.  | [optional] 
**payload_type** | **int** | The payload type - 2 -&gt; Regular (raw payload) - 3 -&gt; Custom grammar - 4 -&gt; Geolocation - 5 -&gt; Display in ASCII - 6 -&gt; Radio planning frame - 9 -&gt; Sensitv2  | [optional] 
**payload_config** | **str** | The payload configuration. Required if the payload type is Custom, else ignored. | [optional] 
**keep_alive** | **int** | Keep alive period in seconds (0 to not keep alive else 1800 second minimum) | [optional] 
**alert_email** | **str** | Email address to contact in case of problems occurring while executing a callback. This field can be unset when updating. | [optional] 
**automatic_renewal** | **bool** | Allows the automatic renewal of devices attached to this device type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

