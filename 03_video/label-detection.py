# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
session.region_name
bucket = s3.create_bucket(Bucket='Rajuvideoanalyse', CreateBucketConfiguration={'LocationConstraint': session.region_name})
bucket = s3.create_bucket(Bucket='rajuvideoanalyse', CreateBucketConfiguration={'LocationConstraint': session.region_name})
bucket = s3.create_bucket(Bucket='rajuvideoanalyse', CreateBucketConfiguration={'LocationConstraint': session.region_name})
bucket = s3.create_bucket(Bucket='rajuvideoanalyse', CreateBucketConfiguration={'LocationConstraint': session.region_name})
bucket = s3.create_bucket(Bucket='rajuvideoanalyse', CreateBucketConfiguration={'LocationConstraint': session.region_name})
bucket = s3.create_bucket(Bucket='rajuvideoanalyse', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
bucket = s3.create_bucket(Bucket='rajuvideoanalyse', 'us-east-1')
bucket = s3.create_bucket(Bucket='rajuvideoanalyse', CreateBucketConfiguration={'LocationConstraint': session.region_name})
s3_client = boto3.client('s3', region_name = 'us-east-1')
s3_client.create_bucket(Bucket='rajuvideor', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
bucket = s3.create_bucket(Bucket='rajuvideoanalyse')
from pathlib import Path
from pathlib import Path
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket,name, 'Name':samplev.mp4}})
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name':samplev.mp4}})
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name':'samplev.mp4'}})
response
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result
result.keys()
result['JobStatus']
result['ResponseMetadata']
result['Labels']
len(result['Labels'])
