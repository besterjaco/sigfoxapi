# EthernetConnectivityForBs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The group&#x27;s identifier | [optional] 
**group** | [**MinGroup**](MinGroup.md) |  | [optional] 
**base_station** | [**MinBaseStation**](MinBaseStation.md) |  | [optional] 
**state** | **int** | State of an ethernet connectivity configuration 0 -&gt; ACTIVE 1 -&gt; PASSIVE 2 -&gt; PENDING (new configuration to synchronize with the base station) 3 -&gt; REJECTED 4 -&gt; DELETING  | [optional] 
**sync_status** | **int** | Synchronisation status of an ethernet connectivity configuration 0 -&gt; OK (the conf is synchronized) 1 -&gt; TO_BE_SENT (the conf has to be synchronized) 2 -&gt; SENT (the conf is currently send to the base station)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

