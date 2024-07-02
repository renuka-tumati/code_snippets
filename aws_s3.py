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
