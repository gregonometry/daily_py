import boto3
ec2 = boto3.resource('ec2')
def lambda_handler(event, context):
    # Connect with ec2 service
    filter = [
        {
            "Name" : 'tag:Type',
            "Value":['Dev']
        }
        ]
    #find running instances with a certain filter, eventually it would be nice to filter by tag
    instances = ec2.instances.filter()
    for instance in instances:
        instance.start()
    return 'Success'
    
