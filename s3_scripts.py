import boto3
from botocore.exceptions import ClientError, BotoCoreError



# connecting to s3
# try:
#     s3_client = boto3.client('s3')
#     print('Successfully connected to s3 client')
# except ClientError as e:
#     print('Error connecting to s3 client', e)

# list buckets
# response = s3_client.list_buckets()

# credentials
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials

# passing directly
# with open('/Users/valeria/Documents/aws_access_key') as f:
#     aws_access_key_id = f.read().strip()
# with open('/Users/valeria/Documents/aws_secret_key') as f:
#     aws_secret_access_key = f.read().strip()
# s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
# response = s3_client.list_buckets()

# Output the bucket names
# print('Existing buckets:')
# for bucket in response['Buckets']:
#     print(f'  {bucket["Name"]}')

# environment variables or .aws/credentials
# Output the bucket names
s3_client = boto3.client('s3')
response = s3_client.list_buckets()
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')


# creating resource
s3 = boto3.resource('s3')
print("Listing buckets using resource")
for bucket in s3.buckets.all():
    print(bucket)


# list objects
my_csv_file = None
s3 = boto3.resource('s3')
my_bucket = s3.Bucket('valeria123')
for o in my_bucket.objects.all():
    print(o)
    if o.key.endswith('.csv'):
        my_csv_file = o.key
        print("found csv: ", my_csv_file)
print("done")


# download file
s3_client.download_file('valeria123', my_csv_file, 'temp.csv')
print(f"downloaded {my_csv_file} to temp.csv")

# as stream - user resource
file_obj = s3.Object('valeria123', my_csv_file)
file_content = file_obj.get()['Body'].read()

print(f"file content (as bytestring): {file_content}")
# decode
decoded = file_content.decode()
print(f"file content (as string) - decoded: {decoded}")

# line by line
file_obj = s3.Object('valeria123', my_csv_file)
for i, line in enumerate(file_obj.get()['Body'].iter_lines()):
    print(f"Line {i}: ", line.decode())


# upload file
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html#uploading-files
response = s3_client.upload_file('requirements.txt', 'valeria123', 'code/requirements.txt')
print('Successfully uploaded')

# need to add write permissions


