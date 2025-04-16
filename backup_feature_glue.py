import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
## PREGUNTA 3 ##
args = getResolvedOptions(sys.argv, ['JOB_NAME','DATABASE_NAME','TABLES_ENTEL','BUCKUP_S3_URI'])
database_name=args['DATABASE_NAME']
tables_list = args['TABLES_ENTEL'].split(",")
backup_s3_uri=args['BUCKUP_S3_URI']
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
print(database_name)
print(tables_list)
print(backup_s3_uri)

# Load data from Glue Data Catalog
for table in tables_list:
    print(table)
    dynamicFrame = glueContext.create_dynamic_frame.from_catalog(database = database_name, table_name = table)

    glueContext.write_dynamic_frame.from_options(
        frame=dynamicFrame,
        connection_type="s3",
        format="avro",
        connection_options={
            "path": f"{backup_s3_uri}/bkp_{table.strip()}"
        }
    )

# Complete the job
job.commit()