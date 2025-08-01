from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError


def index(request):
    try:
        send_mail(
            "subject",
            "message",
            "kidus@localhost.com",
            ["test@localhost.com"],
        )
    except BadHeaderError:
        return HttpResponse("Invalid header found.")

    return render(request, "main.html")
