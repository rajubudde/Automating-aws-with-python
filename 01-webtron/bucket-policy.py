# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
new_bucket = s3.create_bucket(Bucket='rajupython')
new_bucket.upload_file('index.html', 'index.html', ExtraArgs={'ContentType':'text/html'})
new_bucket.upload_file('index.html', 'index.html', ExtraArgs={'ContentType':'text/html'})
policy = """
{
  "Version":"2012-10-17",
  "Statement":[{
  "Sid":"PublicReadGetObject",
  "Effect":"Allow" 
  "Principal": "*",
  "Action":["s3:GetObject"],
  "Resource":["arn:aws:s3:::rajupython/*"
      ]
    }
  ]
}
""" % new_bucket.name
policy = """
{
  "Version":"2012-10-17",
  "Statement":[{
  "Sid":"PublicReadGetObject",
  "Effect":"Allow" 
  "Principal": "*",
  "Action":["s3:GetObject"],
  "Resource":["arn:aws:s3:::%s/*"
      ]
    }
  ]
}
""" % new_bucket.name
print(policy)
pol = new_bucket.Policy()
policy = policy.strip()
policy
pol.put(Policy=policy)
pol.put(Policy=policy)
policy
pol.put(Policy=policy)
policy
policy = policy.strip()
policy
pol.put(Policy=policy)
ws = new_bucket.Website()
ws.put(WebsiteConfiguration={
         'ErrorDocument': {
             'Key': 'error.html'
             },
             'IndexDocument': {
                 'Suffix': 'index.html'
            }})
url = "https://%s.s3-website.us-east-1.amazonaws.com" % new_bucket.name
url
url = "http://%s.s3-website.us-east-1.amazonaws.com" % new_bucket.name
url
url = "http://%s.s3-website-us-east-1.amazonaws.com" % new_bucket.name
url
get_ipython().run_line_magic('history', '')
