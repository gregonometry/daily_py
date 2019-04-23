import datetime
import boto3
from dateutil.parser import parse


def days_old(date):
    parsed = parse(date).replace(tzinfo=None)
    diff = datetime.datetime.now() - parsed
    return diff.days


def lambda_handler(event, context):

    # Get list of regions
    ec2 = boto3.client('ec2')

    amis = ec2.describe_images(Owners=['self'])['Images']

    for ami in amis:
        creation_date = ami['CreationDate']
        age_days = days_old(creation_date)
        image_id = ami['ImageId']
        print('ImageId: {}, CreationDate: {} ({} days old)'.format(
            image_id, creation_date, age_days))

        if age_days <= 1:
            print('Deleting ImageId:', image_id)

            # Deregister the AMI
            ec2.deregister_image(ImageId=image_id)r
