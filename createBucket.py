import boto3


bucket_name = "jens-bucket-demo-1"
region = "us-west-2"

# Create S3 client for the specified region
s3 = boto3.client("s3", region_name=region)

# Create the bucket in us-west-2
try:
    s3.create_bucket(
        Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": region}
    )
    print(f"✅ Bucket '{bucket_name}' created in region '{region}'")
except Exception as e:
    print(f"❌ Failed to create bucket: {e}")
