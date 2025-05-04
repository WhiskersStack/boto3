import boto3

bucket_name = "jens-bucket-demo-1"
region = "us-west-2"

# Create an S3 bucket in the specified region
def create_bucket():
    # Create S3 client for the specified region
    s3 = boto3.client("s3", region_name=region)

    # Create the bucket in us-west-2
    try:
        s3.create_bucket(
            Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": region}
        )
        print(f"\n✅ Bucket '{bucket_name}' created in region '{region}'\n")
    except Exception as e:
        print(f"\n❌ Failed to create bucket: {e}\n")


# Check if the bucket exists
# If it does not exist, create it
# If it does exist, print a message

def check_bucket_exists():
    s3 = boto3.client("s3", region_name=region)
    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f"\n✅ Bucket '{bucket_name}' already exists in region '{region}'\n")
    except Exception as e:
        print(f"\n❌ Bucket '{bucket_name}' does not exist in region '{region}'\n")
        create_bucket() # Call the function to create the bucket if it doesn't exist


check_bucket_exists() # Call the function to check if the bucket exists

