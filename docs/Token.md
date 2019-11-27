# Token

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **int** | - 0 -&gt; OK - 1 -&gt; OFF_CONTRACT - 2 -&gt; NA_FOR_API - 3 -&gt; INVALID_TOKEN  | [optional] 
**detail_message** | **str** | Token state description - Valid - Off Contract - Not applicable for API - Invalid  | [optional] 
**end** | **int** | The device&#x27;s communication end time (in milliseconds since the Unix Epoch) | [optional] 
**free_messages** | **int** | The number of free messages left for this token | [optional] 
**free_messages_sent** | **int** | The number of free messages already sent for this token | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

