'''
Extract timestamps from Amazon Rekognition Video Face Search
Then use Amazon Elastic Transcoder to stitch the clips together
'''

import boto3
import sys

# Connect to Amazon Rekognition
client = boto3.client('rekognition')

# Retrieve the face search results
jobId = sys.argv[1]
person_to_find = sys.argv[2]
timestamps=[]

search = client.get_face_search(JobId=jobId, SortBy='INDEX')

while (True):
  for person in search['Persons']:
    try:
      for face_matches in person['FaceMatches']:
        if face_matches['Face']['ExternalImageId'] == person_to_find:
          timestamps.append(person['Timestamp'])
    except KeyError:
      pass

  # Retrieve the next set of results
  try:
    next_token = search['NextToken']
    search = client.get_face_search(JobId=jobId, SortBy='INDEX', NextToken = search['NextToken'])
  except KeyError:
    break

'''
The timestamps array now looks like:
[99800, 99840, 100000, 100040, ...]
'''

# Break into scenes with start & end times
scenes=[]
start = 0

for timestamp in timestamps:
  if start == 0:
    # First timestamp
    start = end = timestamp
  else:
    # More than 1 second between timestamps? Then scene has ended
    if timestamp - end > 1000:
      # If the scene is at least 1 second long, record it
      if end - start >= 1000:
        scenes.append((start, end))
      # Start a new scene
      start = 0
    else:
      # Extend scene to current timestamp
      end = timestamp

# Append final scene if it is at least 1 second long
if (start != 0) and (end - start >= 1000):
    scenes.append((start, end))

'''
The scenes array now looks like:
[(99800, 101480), (127520, 131760), ...]
'''

# Convert into format required by Amazon Elastic Transcoder
inputs=[]
for scene in scenes:
  start, end = scene
  inputs.append({
    'Key': 'SPLs/202/technical-trainers.mp4',
    'TimeSpan': {
      'StartTime': str(start/1000.),
      'Duration': str((end-start)/1000.)
    }
  })

'''
The inputs array now looks like:
[
  {'Key': 'technical-trainers.mp4', 'TimeSpan': {'StartTime': '99.8', 'Duration': '1.68'}},
  {'Key': 'technical-trainers.mp4', 'TimeSpan': {'StartTime': '127.52', 'Duration': '4.24'}},
  ...
]
'''

# Call Amazon Elastic Transcoder to stitch together a new video
client = boto3.client('elastictranscoder')
generic_720p_preset = '1351620000001-000010'

pipelines = client.list_pipelines()

job = client.create_job(
  PipelineId = pipelines['Pipelines'][0]['Id'],
  Inputs=inputs,
  Output={'Key': person_to_find+'.mp4', 'PresetId': generic_720p_preset}
)

print ('Job submitted for ' + person_to_find)
