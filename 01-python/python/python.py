#!/usr/bin/env python
import boto3
import click
import sys
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Python Deploys websites to AWS"
    pass
@click.command('list-buckets')
def list_buckets():
  "List all s3 buckets"
for bucket in s3.buckets.all():
         print(bucket)


@click.command('list_bucket_objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List all objects in S3 BUCKET"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)
if __name__ ==' __main__':
    cli()
     
