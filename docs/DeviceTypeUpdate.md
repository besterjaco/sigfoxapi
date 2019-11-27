# DeviceTypeUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload_type** | **int** | The payload type 2 -&gt; Regular (raw payload) 3 -&gt; Custom grammar 4 -&gt; Geolocation 5 -&gt; Display in ASCII 6 -&gt; Radio planning frame 9 -&gt; Sensitv2  | [optional] 
**payload_config** | **str** | The payload configuration. Required if the payload type is Custom, else ignored. | [optional] 
**downlink_mode** | **int** | The downlink mode to use for the devices of this device type. 0 -&gt; DIRECT 1 -&gt; CALLBACK 2 -&gt; NONE 3 -&gt; MANAGED  | [optional] 
**downlink_data_string** | **str** | Downlink data to be sent to the devices of this device type if downlinkMode is equal to 0. It must be an 8 byte length message given in hexadecimal string format.  | [optional] 
**description** | **str** | The device types&#x27;s description | [optional] 
**contract_id** | **str** | The device type&#x27;s contract identifier (must be on the same group than the device type) | [optional] 
**contracts** | [**list[ContractId]**](ContractId.md) | The device type&#x27;s contract identifiers (must be on the same group than the device type) | [optional] 
**geoloc_payload_config_id** | **str** | The geoloc payload configuration identifier. Required if the payload type is Geolocation, else ignored. | [optional] 
**automatic_renewal** | **bool** | Allows the automatic renewal of devices attached to this device type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

