# CallbackHTTP

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL called when this message has been processed | [optional] 
**headers** | **object** | The headers sent in the request. If no header is defined, this field is not present. | [optional] 
**body** | **str** | The body of the request, if any. It is only present if the request method is POST. | [optional] 
**content_type** | **str** | The content type of the request. It is only present if the request is a POST. | [optional] 
**method** | **str** | The HTTP method, currently only GET, POST or PUT. | [optional] 
**error** | **str** | If there was an error, for instance if the body is JSON and could not be evaluated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

