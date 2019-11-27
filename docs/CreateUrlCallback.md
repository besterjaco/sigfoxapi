# CreateUrlCallback

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The callback&#x27;s url | [optional] 
**http_method** | **str** | The http method used to send a callback | [optional] 
**downlink_hook** | **bool** | True if this callback is used for downlink, else false. | [optional] 
**headers** | **object** | The headers of the http request to send, as an object with key:value. This field can be unset when updating. | [optional] 
**send_sni** | **bool** | Send SNI (Server Name Indication) for SSL/TLS connections. Used by BATCH_URL and URL callbacks (optional). | [optional] 
**body_template** | **str** | The body template of the request. Only if httpMethpd is set to POST or PUT. It can contain predefined and custom variables. Mandatory for URL callbacks. This field can be unset when updating. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

