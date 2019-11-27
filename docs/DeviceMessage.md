# DeviceMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | [**object**](.md) | Defines a device message | [optional] 
**time** | **int** | Timestamp of the message (in milliseconds since the Unix Epoch) | [optional] 
**data** | **str** | message content, hex encoded | [optional] 
**ack_required** | **bool** | true if an acknowledge is required | [optional] 
**lqi** | **int** | link quality indicator 0 -&gt; LIMIT 1 -&gt; AVERAGE 2 -&gt; GOOD 3 -&gt; EXCELLENT 4 -&gt; NA  | [optional] 
**lqi_repeaters** | **int** | link quality indicator for repeated message 0 -&gt; LIMIT 1 -&gt; AVERAGE 2 -&gt; GOOD 3 -&gt; EXCELLENT 4 -&gt; NA  | [optional] 
**seq_number** | **int** | the sequence number for this message, may not be present when device uses VO protocol | [optional] 
**nb_frames** | **int** | nbFrames can be 1 or 3. This value represents an expected number of frames sent by the device. | [optional] 
**computed_location** | [**list[ComputedLocation]**](ComputedLocation.md) |  | [optional] 
**rinfos** | [**list[Rinfo]**](Rinfo.md) |  | [optional] 
**downlink_answer_status** | [**object**](.md) | the last callback status for this reception | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

