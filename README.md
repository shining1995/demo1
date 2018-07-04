# Archive
archive samples from AWS S3

## Run the program
- boto3 need Authentication of aws S3
- set the crontab on server
  crontab -e
  0 */1 * * * /Archive/run_do_archive.sh
- the bash should be run each hour

## Introduction
  create a json.gz which contents the dict of stored samples including
  'file_name', 'prefix', 'bucket_name', 'market'
  
  you can get the sample storage path by 's3://bucket_name/prifix/file_name'
  
  the gz would be stored on 's3://bucket_name/meta_data_path/Year/Month/Date/Year-Month-Date-hour.gz'
  
  
  
### config.py
- sample_path: the sample path located on s3://bucket_name/..
- meta_data_path: the archive gz file path stored on s3://bucket_name/..
- server_archive_path：temp json path stored on server
- archive_delay: archive samples which stored archive_delay(hours) before

### boto_helper.py
- provide the method to get information from aws S3

### archive_sql_helper.py
- do the sql operation to get information from datebase
- have not been used


