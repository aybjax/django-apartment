from django.http import HttpRequest
from django_q.tasks import async_task
from functions.sendEmail import send_welcome_email_async
from functions.sendSqs import sendQueue


def hook_send_welcome_email_async(task):
    if task.result:
        print("message sent")
    else:
        print("FAIL: message NOT sent")


def sendAsyncEmail(request: HttpRequest, messages) -> None:
    try:
        async_task(
                send_welcome_email_async,
                request.user.username,
                request.user.email,
                hook=hook_send_welcome_email_async,
        )
    except:
        messages.error(request, "FAIL: message NOT sent")
    else:
        messages.success(request, "Message sent to your email address. Check spam")


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

def sendQueue_async(msg, name, attr):
    try:
        async_task(
                sendQueue,
                msg,
                name,
                attr,
        )
    except:
        print("FAIL: queue NOT sent")
    else:
        print("Queue sent")
