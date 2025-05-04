# 📦 AWS S3 Bucket Automation Project

This project automates the creation and management of AWS S3 buckets using Python and the `boto3` library. It includes logic for:

- Creating S3 buckets
- Checking if buckets already exist
- Uploading files (including images and randomly generated text files)
- Listing contents of buckets
- Avoiding duplicate uploads

---

## 📁 Project Structure

```
.
├── Ex1.py                  # Uploads team_image.png to S3 bucket 'jens-bucket-demo-1'
├── Ex2.py                  # Uploads all files from ./dailyDocs to 'jens-bucket-backup-1'
├── Ex3.py                  # Like Ex2, but skips re-uploading files already in S3
├── randomFileGenerator.py  # Generates 20 random text files in ./dailyDocs
├── team_image.png          # Image uploaded by Ex1.py
```

---

## ✅ How to Use

1. **Install dependencies:**

```bash
pip install boto3
```

2. **Generate test files:**

```bash
python randomFileGenerator.py
```

3. **Run the desired script:**

- `Ex1.py`: Uploads `team_image.png` to `jens-bucket-demo-1`
- `Ex2.py`: Uploads files in `./dailyDocs` to `jens-bucket-backup-1`
- `Ex3.py`: Same as `Ex2.py`, but skips files already present in S3

---

## 📝 Notes

- Make sure your AWS credentials are configured (via `~/.aws/credentials` or environment variables).
- Buckets must be globally unique. If "jens-bucket-demo-1" or "jens-bucket-backup-1" already exist in another AWS account, consider changing the names.
- The region used is `us-west-2` by default.
