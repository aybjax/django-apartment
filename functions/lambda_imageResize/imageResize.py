import boto3
import os
from PIL import Image


def getBucket():
    s3 = boto3.resource('s3')
    b = s3.Bucket('django-apartment-aybjaxforamazon')

    return b


def download(bucket, filename):
    ext = os.path.splitext(filename)
    # only /tmp/ is writeable
    tmpName = '/tmp/tmp' + ext[1]

    with open(tmpName, 'wb') as tmpFile:
        bucket.download_fileobj(filename, tmpFile)

    return tmpName


def imageResize(filename, size):
    with Image.open(filename) as img:
        img.thumbnail(size)
        img.save(filename)


def upload(bucket, tmp_name, filename):
    with open(tmp_name, 'rb') as tmpFile:
        bucket.upload_fileobj(tmpFile, filename)


def clean_up(tmp_name):
    os.remove(tmp_name)


def main(filename, size):
    b = getBucket()
    tmpName = download(bucket=b, filename=filename)

    imageResize(filename=tmpName, size=size)
    upload(bucket=b, tmp_name=tmpName, filename=filename)
    clean_up(tmp_name=tmpName)


def handler(event, context):
    files = []

    for msg in event['Records']:
        file_json = msg['body']
        file = json.loads(file_json)
        files.append(file)
        # print(f'msg is {file}')

    for file in files:
        # print(f'file is {file}')
        filename = file['filename']
        size = file['size']
        # print(f'filename is: {filename}')
        # print(f'size is {size}, type: {type(size)}')
        size_tuple = (size, size)
        # print(f'size_tuple: {size_tuple}')
        # print("*"*10)
        main(filename=filename, size=size_tuple)

    return "successful"

# zip -r lambda_fnx.zip imageResize.py PIL/ Pillow-8.0.1.dist-info/ Pillow.libs/
