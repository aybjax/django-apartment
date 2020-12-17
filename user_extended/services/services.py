from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import HttpRequest
from django.template.loader import get_template


def send_welcome_email_async(username: str, email: str) -> bool:
    subject = "You've registered to apartments website"
    from_email = settings.EMAIL_HOST_USER
    to = [email, ]

    plaintext = get_template('email/registered.txt')
    html = get_template('email/registered.html')
    d = {'username': username}

    text_content = plaintext.render(d)
    html_content = html.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")

    try:
        msg.send()
    except:
        return False

    return True


def hook_send_welcome_email_async(task):
    if task.result:
        print("message sent")
    else:
        print("FAIL: message NOT sent")
