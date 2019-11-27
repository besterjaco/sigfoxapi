# ProductCertificateWithPacResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | External Id of the certificate | [optional] 
**certificate_code** | **int** | Certificate&#x27;s code | [optional] 
**certificate_index** | **int** | Certificate&#x27;s index | [optional] 
**qualification_time** | **int** | Date of qualification (in milliseconds since the Unix Epoch) | [optional] 
**report_number** | **str** | Report number | [optional] 
**input_sensitivity** | **int** | Input sensitivity | [optional] 
**encryption_payload** | **bool** | true if the payload will be encrypted | [optional] 
**dev_kit** | **bool** | DevKit Flag | [optional] 
**modes** | **list[int]** | List of modes of the certificate [1&#x3D;DOWNLINK, 2&#x3D;MONARCH] | [optional] 
**standards** | [**list[RadioConfiguration]**](RadioConfiguration.md) |  | [optional] 
**standard_cfgs** | [**list[ProductCertificateRadioConfiguration]**](ProductCertificateRadioConfiguration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

