import boto3

RESIZE_NAME = 'image_file_upload'
RESIZE_ATTR = {
        'VisibilityTimeout': '30',
        'DelaySeconds': '5',
        'ReceiveMessageWaitTimeSeconds': '1',
        'MessageRetentionPeriod': '60',
}

COMPLAINT_NAME = 'complaints'
COMPLAINT_ATTR = {
        'VisibilityTimeout': '43200',  # 12 hrs
        'DelaySeconds': '5',
        'ReceiveMessageWaitTimeSeconds': '1',
        'MessageRetentionPeriod': '1209600',  # 14 dys
}


def getQueue(queue, attr):
    sqs = boto3.resource('sqs')

    try:
        queue = sqs.get_queue_by_name(QueueName=queue)
    except:
        queue = sqs.create_queue(
                QueueName='image_file_upload',
                Attributes=attr
                # Attributes={
                #         'VisibilityTimeout': '30',
                #         'DelaySeconds': '5',
                #         'ReceiveMessageWaitTimeSeconds': '1',
                #         'MessageRetentionPeriod': '60',
                # }
        )
    return queue


def sendQueue(msg, name, attr):
    queue = getQueue(queue=name, attr=attr)

    response = queue.send_message(MessageBody=msg)
    print(f"queue.send_messages(msg='{msg}', name='{name}')")

    return response
