import boto3

bucket_name = "jens-bucket-demo-2"
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
        create_bucket()  # Call the function to create the bucket if it doesn't exist


def upload_file():
    file_path = "team_image.png"  # <-- Local file path
    object_key = "TeamImg/team_image.png"  # <-- S3 path in bucket

    # Connect to S3
    s3 = boto3.resource("s3")

    try:
        with open(file_path, "rb") as data:
            s3.Bucket(bucket_name).put_object(Key=object_key, Body=data)

        print(f"✅ File '{file_path}' uploaded to '{bucket_name}/{object_key}'")

    except Exception as e:
        print(f"❌ Upload failed: {e}")


def list_files():
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucket_name)

    print(f"\n📂 Files in bucket '{bucket_name}':\n")

    for obj in bucket.objects.all():
        print(f"• {obj.key}")

    print("\n ~~~ End of Process ~~~\n")

check_bucket_exists()  # Call the function to check if the bucket exists
upload_file()  # Call the function to upload a file if the bucket exists
list_files()  # Call the function to list files in the bucket