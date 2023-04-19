import boto3

from botocore.handlers import disable_signing
resource = boto3.resource('s3')
resource.meta.client.meta.events.register('__cb__.*', disable_signing)
print(resource)