import boto3
import csv
import pandas as pd

AWS_FILE='/Users/ashwinshnaker/Desktop/aws_access_keys.csv'
S3_BUCKET='databricks-ashanker'
TRIPS_FILE='uber-raw-data-janjune-15.csv'

aws_file=pd.read_csv(AWS_FILE)
aws_access=aws_file['AWSAccessKey'][0]
aws_secret=aws_file['AWSSecretKey'][0]

client = boto3.client(
    's3',
    aws_access_key_id=aws_access,
    aws_secret_access_key=aws_secret
)

obj = client.get_object(Bucket= S3_BUCKET,
                        Key= TRIPS_FILE) 


initial_df = pd.read_csv(obj['Body']) # 'Body' is a key word
