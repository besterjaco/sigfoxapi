# CellularConnectivityForBs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The group&#x27;s identifier | [optional] 
**group** | [**MinGroup**](MinGroup.md) |  | [optional] 
**base_station** | [**MinBaseStation**](MinBaseStation.md) |  | [optional] 
**state** | **int** | State of a cellular connectivity configuration 0 -&gt; ACTIVE 1 -&gt; PASSIVE 2 -&gt; PENDING (new configuration to synchronize with the base station) 3 -&gt; REJECTED 4 -&gt; DELETING  | [optional] 
**sync_status** | **int** | Synchronisation status of a cellular connectivity configuration 0 -&gt; OK (the conf is synchronized) 1 -&gt; TO_BE_SENT (the conf has to be synchronized) 2 -&gt; SENT (the conf is currently send to the base station)  | [optional] 
**last_switch_error_status** | **int** | Error status returned after a connectivity config switch 0 -&gt; SUCCESS 1 -&gt; BAD_GSM_PIN 2 -&gt; TOO_MANY_PIN_TRIES 3 -&gt; VPN_ESTABLISHMENT_IMPOSSIBLE 4 -&gt; NETWORK_REJECTED 5 -&gt; UNKNOWN  | [optional] 
**last_setconf_error_status** | **int** | Error status returned after a connectivity config creation/edition 0 -&gt; SUCCESS 1 -&gt; BAD_FORMAT 2 -&gt; EXISTING_CONFIG 3 -&gt; TOO_MANY_CONFIG 4 -&gt; CONFIG_ID_CONFLICT 5 -&gt; UNKNOWN  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

