# ContractInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The contract ID. | [optional] 
**contract_id** | **str** | The contract external ID. It&#x27;s used to identify the contract info in EDRs.  | [optional] 
**user_id** | **str** | The ID of the user who created the contract in BSS. | [optional] 
**group** | [**MinGroup**](MinGroup.md) |  | [optional] 
**order** | [**MinContractInfo**](MinContractInfo.md) |  | [optional] 
**pricing_model** | **int** | The pricing model used by this contract info. - 1 -&gt; Pricing model version 1. - 2 -&gt; Pricing model version 2. - 3 -&gt; Pricing model version 3.  | [optional] 
**created_by** | **str** | The user id of contract&#x27;s creator | [optional] 
**last_edition_time** | **int** | Creation date of this contract (timestamp in milliseconds since Unix Epoch) | [optional] 
**last_edited_by** | **str** | The user id of the contract last editor | [optional] 
**start_time** | **int** | The start time (in milliseconds) of the contract | [optional] 
**timezone** | **str** | The contract timezone name as a Java TimeZone ID (\&quot;full name\&quot; version only, like \&quot;America/Costa_Rica\&quot;). | [optional] 
**subscription_plan** | **int** | The contract info subscription plan. - 0 -&gt; Free order - 1 -&gt; Pay As You Grow (PAYG) - 2 -&gt; Committed Volume Plan (CVP) - 3 -&gt; Flexible Committed Volume Plan (CVP Flex)  | [optional] 
**token_duration** | **int** | The token duration in months. Must be &gt;&#x3D; 0. 0 means unlimited time. | [optional] 
**blacklisted_territories** | [**list[MinGroup]**](MinGroup.md) | The list of \&quot;blacklisted\&quot; territories, as an array of NIP groups. | [optional] 
**tokens_in_use** | **int** | The number of tokens in use. | [optional] 
**tokens_used** | **int** | The number of tokens used (expired or revoked). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

