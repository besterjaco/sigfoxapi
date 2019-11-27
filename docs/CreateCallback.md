# CreateCallback

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | The callback&#x27;s channel. - URL - BATCH_URL - EMAIL  | 
**callback_type** | **int** | The callback&#x27;s type. | 
**callback_subtype** | **int** | The callback&#x27;s subtype. The subtype must be valid against its type. - 0 -&gt; STATUS callback sending information about the status of a device (available for SERVICE callbacks) - 1 -&gt; GEOLOC callback sent on a message that can be geolocated (available for SERVICE callbacks) ! Warning - From June 2019, the custom callback SERVICE/GEOLOC will be deprecated  ! - 2 -&gt; UPLINK callback for an uplink message (available for DATA callbacks) - 3 -&gt; BIDIR callback for a bidirectional message (available for DATA callbacks) - 4 -&gt; ACKNOWLEDGE callback sent on a downlink acknowledged message (available for SERVICE callbacks) - 5 -&gt; REPEATER callback triggered when a repeater sends an OOB (available for SERVICE callbacks) - 6 -&gt; DATA_ADVANCED callback sent on a message that can be geolocated (available for SERVICE callbacks)  | 
**payload_config** | **str** | The custom payload configuration. Only for DATA callbacks. This field can be unset when updating. | [optional] 
**enabled** | **bool** | True to enable the callback, otherwise false | 
**send_duplicate** | **bool** | True to duplicates callback, otherwise false | 
**dead** | **bool** | True if last use of the callback fails, otherwise false | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

