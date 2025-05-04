import boto3


bucket_name = "jensbucket123-9"
region = "us-west-2"

s3 = boto3.client("s3", region_name=region)

try:
    s3.delete_bucket(Bucket=bucket_name)
    print(f"✅ Bucket '{bucket_name}' deleted")
except Exception as e:
    print(f"❌ Error: {e}")
