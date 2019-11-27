# Group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The group&#x27;s name | [optional] 
**description** | **str** | The group&#x27;s description | [optional] 
**type** | **int** | Group&#x27;s type - 0 -&gt; SO - 2 -&gt; Basic - 5 -&gt; SVNO - 6 -&gt; Partners - 7 -&gt; NIP - 8 -&gt; DIST - 9 -&gt; Channel - 10 -&gt; Starter - 11 -&gt; Partner  | [optional] 
**timezone** | **str** | The timezone (in Java TimeZone ID format, e.g.\&quot;America/Costa_Rica\&quot;). | [optional] 
**id** | **str** | The group&#x27;s identifier | [optional] 
**name_ci** | **str** | The group&#x27;s name to ascii and lowercase | [optional] 
**path** | [**list[MinGroup]**](MinGroup.md) | The group&#x27;s path sorted by descending ancestor {id} (direct parent to farthest parent), restricted to the groups visible by the API user | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

