# Site

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The site&#x27;s identifier | [optional] 
**host_id** | [**MinHost**](MinHost.md) |  | [optional] 
**maintenance_id** | [**MinMaintenance**](MinMaintenance.md) |  | [optional] 
**group_id** | [**MinGroup**](MinGroup.md) |  | [optional] 
**basestation_count** | **int** | the number of base station installed on this site | [optional] 
**primary_internet_subscription** | [**InternetSubscription**](InternetSubscription.md) |  | [optional] 
**candidate_external_id** | **int** | the external identifier of the site as a candidate | [optional] 
**location** | **list[object]** | ISO 3166-1 UN M.49 country code of the site location. The first code is the country (region and department available for some countries). | [optional] 
**creation_time** | **int** | Date of the creation of this site (in milliseconds) | [optional] 
**created_by** | **str** | Identifier of the user who created this site | [optional] 
**last_edited_time** | **int** | Date of the last edition of this site (in milliseconds) | [optional] 
**last_edited_by** | **str** | Identifier of the user who last edited this site | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

