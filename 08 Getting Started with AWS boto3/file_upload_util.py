import boto3

def upload_file(src_file, bucket, tgt_file):
    s3_client = boto3.client('s3')
    s3_client. \
        upload_file(
            src_file,
            bucket,
            tgt_file
        )
    return