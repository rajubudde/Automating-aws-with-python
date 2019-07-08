# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName = key_name)
key.key_material
withopen(key_path, 'w') as key_file:
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().magic(u'ls -l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().magic(u'ls -l python_automation_key.pem')
ec2.image.filter(Owners=['amazon'])
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.Image('ami-02f706d959cedf892')
img.name
ec2-apse2 = session.resource('ec2', region.name = 'ap-southeast-2')
ec2_apse2 = session.resource('ec2', region_name = 'ap-southeast-2')
img_apse2 = ec2_apse2.Image('ami-02f706d959cedf892')
img_apse2.name
img.name
ami_name = 'amzn-ami-hvm-2018.03.0.20190611-x86_64-gp2'
filters = [{'Name:', 'name', 'Values':[ami_name]}]
filters = [{'Name': 'name', 'Values':[ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
list(ec2_apse2.images.filter(Owners=['amazon'], Filters=filters))
img
key
instances = ec2.create_instance(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key_name)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key_name)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
ec2.Instance(id='i-03eac632156571da3')
inst = instances[0]
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups
sg = ec2.SecurityGroup(inst.security_group[0]['GroupID'])
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupID'])
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupID'])
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0][u'GroupID'])
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupID'])
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp':'172.31.87.196/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp':'0.0.0.0/0'}]}])
inst.dns_name
inst.public_dns_name
get_ipython().magic(u'history')
