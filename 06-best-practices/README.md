$env:INPUT_FILE_PATTERN = "s3://nyc-duration/in/{year:04d}-{month:02d}.parquet"
$env:OUTPUT_FILE_PATTERN = "s3://nyc-duration/out/{year:04d}-{month:02d}.parquet"
$env:AWS_ACCESS_KEY_ID = "test"
$env:AWS_SECRET_ACCESS_KEY = "test"

ws --endpoint-url='http://localhost.localstack.cloud:4566' s3 ls s3://nyc-duration/in/