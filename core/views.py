from django.shortcuts import render
from .models import Message
from django.utils.timezone import now
from core.models import Message
from django.shortcuts import render, get_object_or_404

def inbox(request):
    messages = Message.objects.all().order_by('-created_at')

    return render(request, 'inbox.html', {
        'messages': messages
    })

# def compose(request):
#     if request.method == "POST":

#         Message.objects.create(
#             sender=request.POST['sender'],
#             receiver=request.POST['receiver'],
#             subject=request.POST['subject'],
#             body=request.POST['body'],
#             created_at=now(),
#             is_deleted=False
#         )

#         messages = Message.objects.all()

#         return render(request, 'inbox.html', {'messages': messages})


def inbox(request):

    if request.method == "POST":

        edit_id = request.POST.get('edit_id')
        new_subject = request.POST.get('new_subject')

        if edit_id and new_subject:
            Message.objects.filter(id=edit_id).update(subject=new_subject)
           

    messages = Message.objects.all()

    return render(request, 'inbox.html', {'messages': messages})




def inbox(request):

    if request.method == "POST":
        
        deleted_id = request.POST.get('deleted_id')

        if deleted_id:
            Message.objects.filter(id=deleted_id).delete()

    messages = Message.objects.all()

    return render(request, 'inbox.html', {'messages': messages})
 
 
def sent_emails(request):
    messages = Message.objects.all().order_by('-created_at')

    return render(request, 'sent.html', {
        'messages': messages
    })


def message_detail(request, id):

    message = get_object_or_404(Message, id=id)

    return render(request, 'message_detail.html', {
        'message': message
    })


# OpenAI integration

# from .utils import get_ai_reply

# def send_message(request):
#     # your existing code...

#     reply = get_ai_reply(body)

#     Message.objects.create(
#         sender=receiver,
#         receiver=sender,
#         subject="Re: " + subject,
#         body=reply,
#         created_at=timezone.now(),
#         is_deleted=False
#     )


from django.utils import timezone
from .models import Message
from .utils import get_ai_reply

def compose(request):
    if request.method == "POST":
        sender = request.user
        receiver = request.POST.get("receiver")
        subject = request.POST.get("subject")
        body = request.POST.get("body")

        # 1. Save original message
        Message.objects.create(
            sender=sender,
            receiver=receiver,
            subject=subject,
            body=body,
            created_at=timezone.now(),
            is_deleted=False
        )

        # 2. Get AI reply
        reply = get_ai_reply(body)

        # 3. Save auto-reply message
        Message.objects.create(
            sender=receiver,
            receiver=sender,
            subject="Re: " + subject,
            body=reply,
            created_at=timezone.now(),
            is_deleted=False
        )