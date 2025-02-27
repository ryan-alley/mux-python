# CreateLiveStreamRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playback_policy** | [**list[PlaybackPolicy]**](PlaybackPolicy.md) |  | [optional] 
**new_asset_settings** | [**CreateAssetRequest**](CreateAssetRequest.md) |  | [optional] 
**reconnect_window** | **float** | When live streaming software disconnects from Mux, either intentionally or due to a drop in the network, the Reconnect Window is the time in seconds that Mux should wait for the streaming software to reconnect before considering the live stream finished and completing the recorded asset. Defaults to 60 seconds on the API if not specified. | [optional] 
**passthrough** | **str** |  | [optional] 
**audio_only** | **bool** | Force the live stream to only process the audio track when the value is set to true. Mux drops the video track if broadcasted. | [optional] 
**embedded_subtitles** | [**list[LiveStreamEmbeddedSubtitleSettings]**](LiveStreamEmbeddedSubtitleSettings.md) | Describe the embedded closed caption contents of the incoming live stream. | [optional] 
**reduced_latency** | **bool** | This field is deprecated. Please use latency_mode instead. Latency is the time from when the streamer transmits a frame of video to when you see it in the player. Set this if you want lower latency for your live stream. Note: Reconnect windows are incompatible with Reduced Latency and will always be set to zero (0) seconds. Read more here: https://mux.com/blog/reduced-latency-for-mux-live-streaming-now-available/ | [optional] 
**low_latency** | **bool** | This field is deprecated. Please use latency_mode instead. Latency is the time from when the streamer transmits a frame of video to when you see it in the player. Setting this option will enable compatibility with the LL-HLS specification for low-latency streaming. This typically has lower latency than Reduced Latency streams, and cannot be combined with Reduced Latency. Note: Reconnect windows are incompatible with Low Latency and will always be set to zero (0) seconds. | [optional] 
**latency_mode** | **str** | Latency is the time from when the streamer transmits a frame of video to when you see it in the player. Set this as an alternative to setting low latency or reduced latency flags. The Low Latency value is a beta feature. Note: Reconnect windows are incompatible with Reduced Latency and Low Latency and will always be set to zero (0) seconds. Read more here: https://mux.com/blog/introducing-low-latency-live-streaming/ | [optional] 
**test** | **bool** | Marks the live stream as a test live stream when the value is set to true. A test live stream can help evaluate the Mux Video APIs without incurring any cost. There is no limit on number of test live streams created. Test live streams are watermarked with the Mux logo and limited to 5 minutes. The test live stream is disabled after the stream is active for 5 mins and the recorded asset also deleted after 24 hours. | [optional] 
**simulcast_targets** | [**list[CreateSimulcastTargetRequest]**](CreateSimulcastTargetRequest.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


