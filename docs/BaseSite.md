# BaseSite

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The site&#x27;s name | [optional] 
**lessor_id** | **str** | The lessor identifier of the site. This field can be unset when updating. | [optional] 
**address** | **str** | The address of the site | [optional] 
**comment** | **str** | Comment about the site. This field can be unset when updating. | [optional] 
**status** | **int** | Site status: - 0 -&gt; PROD - 1 -&gt; REFUSED - 2 -&gt; INSTALLED - 3 -&gt; NOT PLANNED - 4 -&gt; PRE PROD - 5 -&gt; CANDIDATE - 6 -&gt; CANCELLED - 7 -&gt; CLIENT - 8 -&gt; RD - 9 -&gt; LABO - 14 -&gt; INSTALLED CONNECTED ONLY SECONDARY - 15 -&gt; INSTALLED CONNECTED ONLY PRIMARY  | [optional] 
**status_comment** | **str** | The comment of the status of the site. This field can be unset when updating. | [optional] 
**station_installation** | **int** | Station installation: - 0 -&gt; INDOOR WITHOUT CABINET - 1 -&gt; INDOOR WITH CABINET - 2 -&gt; OUTDOOR WITHOUT CABINET - 3 -&gt; OUTDOOR WITH CABINET  | [optional] 
**inverter_info** | **int** | Inverter type: - 0 -&gt; NONE - 1 -&gt; AC POWER HOST - 2 -&gt; AC POWER HOST INVERTER - 3 -&gt; AC POWER SIGFOX INVERTER - 4 -&gt; DC POWER HOST 48V - 5 -&gt; DC POWER SOLAR  | [optional] 
**aerial_work_platform_access** | **bool** | is the site access to the aerial work platform | [optional] 
**lat** | **float** | the site&#x27;s latitude | [optional] 
**lng** | **float** | the site&#x27;s longitutde | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

