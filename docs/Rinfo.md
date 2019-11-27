# Rinfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_station** | [**object**](.md) | Name and Id of the base station which has received the message. | [optional] 
**lat** | **float** | The latitude of the base station that has received the message. | [optional] 
**lng** | **float** | The longitude of the base station that has received the message. | [optional] 
**delay** | **float** | the delay (in second) between sending and receiving the message, may not be present. | [optional] 
**rep** | **int** | number of repetitions sent by the base station | [optional] 
**cb_status** | [**list[CbStatus]**](CbStatus.md) | list of callback status for this reception | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

