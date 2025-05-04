import boto3

for i in range(1, 5):
    print(f"Creating bucket {i+5}...")
    # Create a unique bucket name

    bucket_name = f"jensbucket123-{i+5}"  # <-- replace this with a unique name
    region = 'us-west-2'

    # Create S3 client for the specified region
    s3 = boto3.client('s3', region_name=region)

    # Create the bucket in us-west-2
    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
        print(f"✅ Bucket '{bucket_name}' created in region '{region}'")
    except Exception as e:
        print(f"❌ Failed to create bucket: {e}")
