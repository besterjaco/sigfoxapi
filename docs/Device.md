# Device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_type** | [**MinDeviceType**](MinDeviceType.md) |  | [optional] 
**contract** | [**MinContractInfo**](MinContractInfo.md) |  | [optional] 
**group** | [**MinGroup**](MinGroup.md) |  | [optional] 
**modem_certificate** | [**Certificate**](Certificate.md) |  | [optional] 
**prototype** | **bool** | The device is a prototype | [optional] 
**product_certificate** | [**Certificate**](Certificate.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**last_computed_location** | [**ComputedLocation**](ComputedLocation.md) |  | [optional] 
**pac** | **str** | The device&#x27;s PAC (Porting Access Code) | 
**sequence_number** | **int** | The last device&#x27;s sequence number. Absent if the device has never communicated or if the SIGFOX message protocol is V0  | [optional] 
**trash_sequence_number** | **int** | The last trashed device&#x27;s sequence number. Absent if there is no message trashed or if the SIGFOX message protocol is V0  | [optional] 
**last_com** | **int** | The last time (in milliseconds since the Unix Epoch) the device has communicated | [optional] 
**lqi** | **int** | Link Quality Indicator 0 -&gt; LIMIT 1 -&gt; AVERAGE 2 -&gt; GOOD 3 -&gt; EXCELLENT 4 -&gt; NA  | [optional] 
**activation_time** | **int** | The device&#x27;s activation time (in milliseconds since the Unix Epoch) | [optional] 
**creation_time** | **int** | The device&#x27;s provisionning time (in milliseconds since the Unix Epoch) | 
**state** | **int** | State of this device. 0 -&gt; OK 1 -&gt; DEAD 2 -&gt; OFF_CONTRACT 3 -&gt; DISABLED 4 -&gt; WARN 5 -&gt; DELETED 6 -&gt; SUSPENDED 7 -&gt; NOT_ACTIVABLE  | 
**com_state** | **int** | Communication state of this device. 0 -&gt; NO 1 -&gt; OK 2 -&gt; WARN 3 -&gt; KO 4 -&gt; (na) 5 -&gt; NOT_SEEN  | 
**token** | [**Token**](Token.md) |  | [optional] 
**unsubscription_time** | **int** | The device&#x27;s unsubscription time (in milliseconds since the Unix Epoch) | [optional] 
**created_by** | **str** | The id of device&#x27;s creator user | [optional] 
**last_edition_time** | **int** | Date of the last edition of this device (in milliseconds since the Unix Epoch) | [optional] 
**last_edited_by** | **str** | The id of device&#x27;s last editor user | [optional] 
**automatic_renewal** | **bool** | Allow token renewal ? | 
**automatic_renewal_status** | **int** | Computed automatic renewal status. 0 -&gt; ALLOWED 1 -&gt; NOT_ALLOWED 2 -&gt; RENEWED 3 -&gt; ENDED  | [optional] 
**activable** | **bool** | true if the device is activable and can take a token | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

