import boto3
def lambda_handler(event, context):
  s3 = boto3.resource('s3')
  bucket_list = s3.buckets.all()
  client = boto3.client('s3')
  
  
  non_encrypted_buckets = []
  for bucket in bucket_list:
    try:
      response = client.get_bucket_encryption(Bucket=bucket.name)
      for encryption in response['ServerSideEncryptionConfiguration']['Rules']:
        encryption_algorithm = encryption['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']
    except Exception as e:
      non_encrypted_buckets.append(bucket.name)
  
    try:
      print (bucket.name + ": " + s3.BucketPolicy(bucket.name).policy)
    except Exception as e:
      print (bucket.name + ": No bucket policy")
  
  print ("The following buckets are not encrypted: \n" + str(non_encrypted_buckets))
