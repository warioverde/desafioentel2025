import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
## PREGUNTA 4 ##
args = getResolvedOptions(sys.argv, ['JOB_NAME','TABLE','S3_BACKUP_PATH','S3_OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
table=args['TABLE']
s3_backup_path=args['S3_BACKUP_PATH']
s3_output_path=args['S3_OUTPUT_PATH']
print(s3_output_path)

backup_df = spark.read.format("avro").load(s3_backup_path)
backup_df.toPandas().to_csv(f"{s3_output_path}{table}.csv", sep="|", index=False, header=False)


job.commit()
