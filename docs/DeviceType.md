# DeviceType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The device type&#x27;s identifier | [optional] 
**description** | **str** | The device type&#x27;s description | [optional] 
**downlink_mode** | **int** | The downlink mode to use for the devices of this device type. 0 -&gt; DIRECT 1 -&gt; CALLBACK 2 -&gt; NONE 3 -&gt; MANAGED  | [optional] 
**downlink_data_string** | **str** | Downlink data to be sent to the devices of this device type if downlinkMode is equal to 0. It must be an 8 byte length message given in hexadecimal string format.  | [optional] 
**payload_type** | **int** | The payload type 2 -&gt; Regular (raw payload) 3 -&gt; Custom grammar 4 -&gt; Geolocation 5 -&gt; Display in ASCII 6 -&gt; Radio planning frame 9 -&gt; Sensitv2  | [optional] 
**payload_config** | **str** | The payload configuration. Required if the payload type is Custom, else ignored. | [optional] 
**group** | [**MinGroup**](MinGroup.md) |  | [optional] 
**contract** | [**MinContractInfo**](MinContractInfo.md) |  | [optional] 
**contracts** | [**list[MinContractInfo]**](MinContractInfo.md) | The list of the contracts associated with the device type | [optional] 
**detached_contracts** | [**list[MinContractInfo]**](MinContractInfo.md) | The list of the contracts that were associated with the device type at some point, but are not anymore. | [optional] 
**geoloc_payload_config** | [**GeolocPayloadConfig**](GeolocPayloadConfig.md) |  | [optional] 
**creation_time** | **int** | Date of the creation of this device type (in milliseconds) | [optional] 
**created_by** | **str** | Identifier of the user who created this device type | [optional] 
**last_edition_time** | **int** | Date of the last edition of this device type (in milliseconds) | [optional] 
**last_edited_by** | **str** | Identifier of the user who last edited this device type | [optional] 
**automatic_renewal** | **bool** | Allows the automatic renewal of devices attached to this device type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

