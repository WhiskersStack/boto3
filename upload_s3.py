import boto3

# Connect to S3
s3 = boto3.resource('s3')

# List all buckets
print("Your buckets:")
for bucket in s3.buckets.all():
    print("-", bucket.name)


# Upload a file
bucket_name = 'jensbucket123'         # <-- replace this
file_path = 'text.txt'               # <-- replace this
object_key = 'uploads/text.txt'      # <-- S3 path inside the bucket

with open(file_path, 'rb') as data:
    s3.Bucket(bucket_name).put_object(Key=object_key, Body=data)

print(f"✅ File '{file_path}' uploaded to '{bucket_name}/{object_key}'")