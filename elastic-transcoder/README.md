# Amazon Elastic Transcoder

Amazon Elastic Transcoder is media transcoding in the cloud. It is designed to be highly scalable, easy to use and cost-effective for developers and businesses to convert (or “transcode”) media files from their source format into versions that will playback on devices such as smartphones, tablets and PCs.

### Streaming
Use Amazon elastic trancoder to convert video (which is stored in S3), setup
prefix for `input` and `output`, create pipeline that manage the jobs to
transcode the input file.

Create jobs to transcode the input file into multiple bit-rates as selected,
create presets. Create presets with multiple output type (to suitable with
multiple network)

In Playlist section, create master playlist (file master.m3u8)
