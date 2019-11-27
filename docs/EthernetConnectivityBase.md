# EthernetConnectivityBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the name of the configuration | 
**type** | **int** | Token&#x27;s type of an ethernet connectivity configuration 1 -&gt; STATIC 2 -&gt; PARTLY_DYNAMIC  | 
**ip** | **str** | IP address of the ethernet connectivity, required if the type is STATIC | [optional] 
**mask** | **str** | Subnet mask of the ethernet connectivity, required if the type is STATIC | [optional] 
**dns1** | **str** | DNS n°1 of the ethernet connectivity, required if the type is STATIC | [optional] 
**dns2** | **str** | DNS n°2 of the ethernet connectivity, only applicable if the type is STATIC. This field can be unset when updating. | [optional] 
**gateway** | **str** | Gateway of the ethernet connectivity, required if the type is STATIC | [optional] 
**mtu** | **int** | MTU of the ethernet connectivity, required if the type is PARTLY_DYNAMIC. This field can be unset when updating. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

