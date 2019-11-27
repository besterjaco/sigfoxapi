# BaseIntervention

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** | The author of this intervention | [optional] 
**comment** | **str** | The comment about this intervention | [optional] 
**equipments_to_change** | **list[int]** | List of equipment to change for this intervention - 0 -&gt; ANTENNA - 1 -&gt; BASE STATION - 2 -&gt; LNA - 3 -&gt; FEEDER - 4 -&gt; ADSL MODEM - 5 -&gt; NETWORK CABLE - 6 -&gt; SURGE - 7 -&gt; WATERPROOFNESS - 8 -&gt; SAT DEMOD - 9 -&gt; SAT LNB - 10 -&gt; SAT DISH - 11 -&gt; SAT POWER SUPPLY - 12 -&gt; INVERTER - 13 -&gt; KEY 3G - 14 -&gt; CIRCUIT BREAKER - 15 -&gt; ROUTER 3G  | [optional] 
**planned_time** | **int** | The planned time of this intervention | [optional] 
**intervention_time** | **int** | The time of this intervention | [optional] 
**end_time** | **int** | The end time of this intervention | [optional] 
**bill_code** | **str** | The bill code of this intervention | [optional] 
**rt_id** | **str** | The request tracker identifier of this intervention | [optional] 
**closed** | **bool** | is this intervention closed | [optional] 
**costs** | **float** | The costs of this intervention | [optional] 
**type** | **int** | Convention status. - 0 -&gt; OTHER - 1 -&gt; PRE VISIT - 2 -&gt; ANTENNA INSTALLATION - 3 -&gt; TELECOM LINE INSTALLATION - 4 -&gt; SITE SEARCH - 5 -&gt; SAT INSTALLATION - 6 -&gt; ELECTRICAL - 7 -&gt; DISMANTLING  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

