from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from .models import Chat, Message
from django.contrib import messages

def chat_list(request):
    if request.user.is_authenticated:
        chats = Chat.objects.filter(models.Q(user1=request.user) | models.Q(user2=request.user))
        if not chats:
            messages.success(request, 'You have no chats yet')
            return redirect('recommendations')
        return render(request, 'chat_list.html', {'chats': chats})
    else:
        return redirect('login')


def chat_detail(request, chat_id):
    if request.user.is_authenticated:
        chat = get_object_or_404(Chat, id=chat_id)
        if request.user not in [chat.user1, chat.user2]:
            return JsonResponse({'error': 'Access denied'}, status=403)

        messages = chat.messages.order_by('timestamp')
        return render(request, 'chat_detail.html', {'chat': chat, 'messages': messages})
    else:
        return redirect('login')

@csrf_exempt
def send_message(request, chat_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            chat = get_object_or_404(Chat, id=chat_id)
            if request.user not in [chat.user1, chat.user2]:
                return JsonResponse({'error': 'Access denied'}, status=403)

            content = request.POST.get('content')
            if not content:
                return JsonResponse({'error': 'Content cannot be empty'}, status=400)

            message = Message.objects.create(chat=chat, sender=request.user, content=content)
            return redirect('chat_detail', chat_id=chat_id)

        return JsonResponse({'error': 'Invalid method'}, status=405)
    else:
        return redirect('login')
    