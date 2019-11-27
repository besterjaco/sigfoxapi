# ComputedLocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | The device&#x27;s estimated latitude | [optional] 
**lng** | **float** | The device&#x27;s estimated longitude | [optional] 
**radius** | **int** | The radius of the circle (meters) | [optional] 
**source** | **int** | Define how the location has been computed: - 0 -&gt; computed using RSSI and position of the station (legacy) - 1 -&gt; computed using the GPS data inside the payload - 2 -&gt; computed using Network location - 3 -&gt; computed using PoI location - 4 -&gt; computed using HD network location - 5 -&gt; computed using private database location - 6 -&gt; computed using WiFi location  | [optional] 
**place_ids** | **list[str]** | The place ids computed by the Sigfox Geolocation service | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

