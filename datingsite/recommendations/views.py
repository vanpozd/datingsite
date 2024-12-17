from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from authentication.models import CustomUser
import json

def recom(request):
    user = request.user
    users = CustomUser.objects.exclude(id=request.user.id).filter(age__gte=user.age-2, age__lte=user.age+2)
    if request.user.is_authenticated:
        return render(request, 'recommendations.html', {'rec_user': users[0]})
    else:
        return redirect('login')

@csrf_exempt
def handle_action(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        action = data.get('type')
        user_id = data.get('user_id')
        
        if action == 'like':
            pass
        elif action == 'dislike':
            pass
        elif action == 'report':
            pass
        else:
            return JsonResponse({'error': 'Invalid action'}, status=400) 
        
        user = request.user
        users = CustomUser.objects.exclude(id=request.user.id).filter(age__gte=user.age-2, age__lte=user.age+2)
        next_user = users.filter(id__gt=user_id).first()
        
        if next_user:
            response_data = {
                'user_first_name': next_user.first_name,
                'user_last_name': next_user.last_name,
                'user_age': next_user.age,
                'user_desc': next_user.description,
                'user_id': next_user.id
            }
        else:
            response_data = {
                'message': 'No more users'
            }
        
        return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request'}, status=400)