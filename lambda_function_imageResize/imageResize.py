import boto3
import os
from PIL import Image


def getBucket():
    s3 = boto3.resource('s3')
    b = s3.Bucket('django-apartment-aybjaxforamazon')

    return b


def download(bucket, filename):
    ext = os.path.splitext(filename)
    tmpName = 'tmp' + ext[1]

    with open(tmpName, 'wb') as tmpFile:
        bucket.download_fileobj(filename, tmpFile)

    return tmpName


def imageResize(filename, size):
    try:
        with Image.open(filename) as img:
            img.thumbnail(size)
            img.save(filename)
    except:
        return False
    else:
        return True


def upload(bucket, tmp_name, filename):
    with open(tmp_name, 'rb') as tmpFile:
        bucket.upload_fileobj(tmpFile, filename)


def clean_up(tmp_name):
    try:
        os.remove(tmp_name)
    except:
        ...


def main(filename):
    try:
        b = getBucket()
        tmpName = download(bucket=b, filename=filename)
    except:
        return

    success = imageResize(filename=tmpName, size=(200, 200))

    if not success:
        return

    upload(bucket=b, tmp_name=tmpName, filename=filename)
    clean_up(tmp_name=tmpName)


if __name__ == '__main__':
    # main('apartment_images/72_amazon_from_mx/apt_amazon_1_1/2_only2iterations.jpg')
    main('1_invitation.jpg')
