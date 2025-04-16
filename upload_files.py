import pandas as pd
import boto3
from io import StringIO

## PREGUNTA 1 ##

client = boto3.client('s3')
bucket_name="desafiotecnicoentel2025"
print("Iniciando proceso")
s3 = boto3.resource('s3')

def upload_s3(csv_file_name):
    jobs_df = pd.read_csv(csv_file_name, sep=',')
    csv_buf=StringIO()
    jobs_df.to_csv(csv_buf, header=False,  sep='|', index=False)
    client.put_object(Body=csv_buf.getvalue(), Bucket=bucket_name, Key=f'raw/{csv_file_name.split(".")[0]}/{csv_file_name}')

files_list = ["departments.csv", "hired_employees.csv", "jobs.csv"]
for file in files_list:
    upload_s3(file)