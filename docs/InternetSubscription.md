# InternetSubscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of this internet subscription | [optional] 
**type** | **int** | Internet subscription type - 0 -&gt; GSM - 1 -&gt; ADSL - 2 -&gt; SATELLITE - 3 -&gt; LAN - 4 -&gt; WIFI  | [optional] 
**priority** | **int** | Internet subscription priority. - 0 -&gt; PRIMARY - 1 -&gt; SECONDARY - 2 -&gt; TERMINATED  | [optional] 
**comments** | **str** | The comments about this internet subscription. This field can be unset when updating. | [optional] 
**start_time** | **int** | The start time of this internet subscription | [optional] 
**end_time** | **int** | The end time this internet subscription. This field can be unset when updating. | [optional] 
**provider** | [**MinProvider**](MinProvider.md) |  | [optional] 
**contacts** | [**list[MinContact]**](MinContact.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

