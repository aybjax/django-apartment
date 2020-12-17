import boto3


def getQueue():
    sqs = boto3.resource('sqs')

    queue = sqs.get_queue_by_name(QueueName='complaints')

    # queue = sqs.create_queue(
    #         QueueName='complaints',
    #         # Attributes={'DelaySeconds': '5'}
    # )

    print(queue)
    print(queue.url)
    print(queue.attributes)
