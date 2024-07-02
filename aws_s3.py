import boto3

# Replace with your AWS credentials
aws_access_key_id = "YOUR_ACCESS_KEY_ID"
aws_secret_access_key = "YOUR_SECRET_ACCESS_KEY"

# Replace with your S3 bucket name and path
bucket_name = "rdec-dev-datalake-ing-us-west-2"
bucket_path = "source/camelcase"

# Initialize S3 client
s3 = boto3.client("s3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# List objects in the specified bucket and path
response = s3.list_objects_v2(Bucket=bucket_name, Prefix=bucket_path)

# Print the list of files
print("Files in S3 bucket:")
for obj in response.get("Contents", []):
    print(obj["Key"])
    
    [hello-dev]
aws_access_key_id        = 78
aws_secret_access_key    = abc

import configparser
import boto3

# Function to read credentials from a file
def read_credentials(credentials_file_path):
    config = configparser.ConfigParser()
    config.read(credentials_file_path)
    
    # Assuming section [hello-dev]
    section = 'hello-dev'
    access_key_id = config.get(section, 'aws_access_key_id')
    secret_access_key = config.get(section, 'aws_secret_access_key')
    
    return access_key_id, secret_access_key

# Function to connect to S3 using key and id
def connect_to_s3(access_key_id, secret_access_key):
    # Initialize the S3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key
    )
    # Example usage: List all buckets
    response = s3.list_buckets()
    print("List of S3 buckets:")
    for bucket in response['Buckets']:
        print(f'- {bucket["Name"]}')

# Example usage
if __name__ == "__main__":
    credentials_file_path = "path/to/credentials.ini"
    aws_access_key_id, aws_secret_access_key = read_credentials(credentials_file_path)
    connect_to_s3(aws_access_key_id, aws_secret_access_key)


List IAM User Permissions:

bash
Copy code
aws iam list-user-permissions --user-name YourUserName
Replace YourUserName with the name of the IAM user you want to list permissions for.

List IAM Group Permissions:

bash
Copy code
aws iam list-group-policies --group-name YourGroupName
aws iam list-group-members --group-name YourGroupName
Replace YourGroupName with the name of the IAM group.

List IAM Role Permissions:

bash
Copy code
aws iam list-attached-role-policies --role-name YourRoleName
aws iam list-role-policies --role-name YourRoleName
Replace YourRoleName with the name of the IAM role.

List IAM Policy Permissions:

bash
Copy code
aws iam list-policy-versions --policy-arn YourPolicyARN
aws iam get-policy --policy-arn YourPolicyARN
Replace YourPolicyARN with the ARN (Amazon Resource Name) of the IAM policy.

Using boto3 in Python
To achieve the same using Python, you'll use the boto3 library to interact with AWS IAM:







