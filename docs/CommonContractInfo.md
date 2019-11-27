# CommonContractInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The contract name | [optional] 
**activation_end_time** | **int** | The activation end time (in milliseconds) of the contract. 0 means no activation time limit. | [optional] 
**communication_end_time** | **int** | The end time (in milliseconds) of the communication. 0 means no communication time limit. | [optional] 
**bidir** | **bool** | True if the contract info is bidirectional. | [optional] 
**high_priority_downlink** | **bool** | True if all downlinks are high priority. | [optional] 
**max_uplink_frames** | **int** | The maximum number of uplink frames. | [optional] 
**max_downlink_frames** | **int** | The maximum number of downlink frames. | [optional] 
**max_tokens** | **int** | The maximum number of tokens for this contract. Either 0 (unlimited) or a positive number. | [optional] 
**automatic_renewal** | **bool** | True if automatic renewal is allowed. | [optional] 
**renewal_duration** | **int** | The renewal duration in months. | [optional] 
**options** | **list[object]** | The activated premium options. Given options will be merged with existing options in contract. In order to delete a single option use \&quot;/{id}/options\&quot; API. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

