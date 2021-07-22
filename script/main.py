from zipfile import ZipFile
import os
from os.path import basename, dirname, abspath
import logging
import boto3
from botocore.exceptions import ClientError
import click

@click.group()
def cli():
    pass

def pkg_src_file(pkg_name):
    currdir = abspath(dirname(__file__))
    src_dir = f'{abspath(dirname(currdir))}/src'
    with ZipFile(pkg_name, 'w') as zipObj:
    # Iterate over all the files in directory
        for folderName, subfolders, filenames in os.walk(src_dir):
            for filename in filenames:
                #create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                # Add file to zip
                zipObj.write(filePath, basename(filePath))

def upload_zipfile(file_name, bucket, key_name=None):
    s3_client = boto3.client('s3')
    if key_name is None:
        key_name = file_name
    try:
        response = s3_client.upload_file(file_name, bucket, key_name)
    except ClientError as e:
        print(f'error:{e}')
        return False
    print(f'Pkg is uploaded to {bucket}')


@cli.command(name='pkg-and-upload')
@click.argument('pkg_name')
@click.argument('bucket') 
def pkg_and_upload(pkg_name, bucket):
    # /automatecfg.sh pkg-and-upload version1.zip automatecfg
    pkg_src_file(pkg_name)
    upload_zipfile(pkg_name, bucket)
    

if __name__ == '__main__':
    cli(prog_name='./automatecfg.sh')