# ContractInfoCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | ID of group associated with the contact | [optional] 
**contract_id** | **str** | The contract external ID. It&#x27;s used to identify the contract in EDRs. | [optional] 
**user_id** | **str** | The ID of the user who created the contract in BSS. | [optional] 
**order_id** | **str** | The order ID (hex), if any. | [optional] 
**order_name** | **str** | The order name, if any | [optional] 
**pricing_model** | **int** | The pricing model used by this contract info. 1 -&gt; Pricing model version 1. 2 -&gt; Pricing model version 2. 3 -&gt; Pricing model version 3.  | [optional] 
**start_time** | **int** | The start time (in milliseconds) of the contract | [optional] 
**timezone** | **str** | The contract timezone name as a Java TimeZone ID (\&quot;full name\&quot; version only, like \&quot;America/Costa_Rica\&quot;). | [optional] 
**subscription_plan** | **int** | The contract info subscription plan. 0 -&gt; Free order 1 -&gt; Pay As You Grow (PAYG) 2 -&gt; Committed Volume Plan (CVP) 3 -&gt; Flexible Committed Volume Plan (CVP Flex) 4 -&gt; PACK 5 -&gt; DevKit 6 -&gt; Activate  | [optional] 
**token_duration** | **int** | The token duration in months. Must be &gt;&#x3D; 0, if 0 unlimited token duration. | [optional] 
**blacklisted_territories** | **list[str]** | The list of \&quot;blacklisted\&quot; territories, as an array of NIP group IDs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

