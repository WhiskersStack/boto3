import boto3

bucket_name = "jens-bucket-demo-1"
region = "us-west-2"


def create_bucket():
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


def check_bucket_exists():
    s3 = boto3.client("s3", region_name=region)
    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f"✅ Bucket '{bucket_name}' already exists in region '{region}'")
    except Exception as e:
        print(f"❌ Bucket '{bucket_name}' does not exist in region '{region}'")
        create_bucket()


check_bucket_exists()
