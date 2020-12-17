import boto3


def getQueue():
    sqs = boto3.resource('sqs')

    try:
        queue = sqs.get_queue_by_name(QueueName='complaints')
    except:
        queue = sqs.create_queue(
                QueueName='complaints',
                Attributes={
                        'VisibilityTimeout': '43200',  # 12 hrs
                        'DelaySeconds': '5',
                        'ReceiveMessageWaitTimeSeconds': '1',
                        'MessageRetentionPeriod': '1209600',  # 14 dys
                })
    return queue


def sendQueue(msg):
    queue = getQueue()

    response = queue.send_message(MessageBody=msg)

    return response
