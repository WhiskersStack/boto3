import boto3
import os

bucket_name = "jens-bucket-backup-1"
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
        upload_file()  # Call the function to upload a file if the bucket exists
    except Exception as e:
        print(f"\n❌ Bucket '{bucket_name}' does not exist in region '{region}'\n")
        create_bucket()  # Call the function to create the bucket if it doesn't exist
        upload_file()  # Call the function to upload a file if the bucket exists


def upload_file():
    local_folder = "./dailyDocs"
    s3_prefix = "backup/"

    # Connect to S3
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucket_name)

    # Loop and upload
    for filename in os.listdir(local_folder):
        local_path = os.path.join(
            local_folder, filename
        )  # File path: dailyDocs/filename

        if os.path.isfile(local_path):  # Check if it's a file
            s3_key = s3_prefix + filename  # S3 path to upload to: backup/filename

            with open(local_path, "rb") as data:
                bucket.put_object(Key=s3_key, Body=data)

            print(f"✅ Uploaded '{filename}' to S3 as '{s3_key}'")


def list_files():
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucket_name)

    print(f"\n📂 Files in bucket '{bucket_name}':\n")

    for obj in bucket.objects.all():
        print(f"• {obj.key}")

    print("\n ~~~ End of Process ~~~\n")


check_bucket_exists()  # Call the function to check if the bucket exists
list_files()  # Call the function to list files in the bucket
