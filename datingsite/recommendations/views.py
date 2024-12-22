from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from authentication.models import CustomUser
from chat.models import Chat
import json

def get_liked_profile_id(request):
    liked_profiles = request.user.get_liked_profiles()

    if liked_profiles is not None:
        liked_user = liked_profiles.pop(0)
        if len(liked_profiles) == 0:
            request.user.set_liked_profiles(None)    
        else:
            request.user.set_liked_profiles(liked_profiles)
        return liked_user
    return None

def recom(request):
    if request.user.is_authenticated:
        like_flg = False
        liked_user = get_liked_profile_id(request)
        if liked_user is None:
            liked_user = CustomUser.objects.exclude(id=request.user.id).filter(age__gte=request.user.age-2, age__lte=request.user.age+2).first()
        else:
            liked_user = CustomUser.objects.get(id=liked_user)
            like_flg = True 
        images = [photo.url for photo in [liked_user.photo1, liked_user.photo2, liked_user.photo3, liked_user.photo4, liked_user.photo5, liked_user.photo6] if photo]
        return render(request, 'recommendations.html', {'rec_user': liked_user, 'images': images, 'like_flg': like_flg})
    else:
        return redirect('login')

@csrf_exempt
def handle_action(request):
    if request.method == 'POST':
        like_flg = False
        data = json.loads(request.body)
        action = data.get('type')
        user_id = data.get('user_id')
        already_liked_flg = data.get('like_flg')

        request.user.get_liked_profiles()
        if action == 'like':
            if already_liked_flg:
                try:
                    newchat = Chat.objects.create(user1=request.user, user2=CustomUser.objects.get(id=user_id))
                    newchat.save()
                except:
                    pass
            else:
                request.user.add_number_to_liked_profiles(user_id)
        elif action == 'dislike':
            pass
        elif action == 'report':
            CustomUser.objects.get(id=user_id).report()
        else:
            return JsonResponse({'error': 'Invalid action'}, status=400) 
        
        user = request.user
        liked_user_id = get_liked_profile_id(request)
        if liked_user_id is not None:
            print("liked_user_id is not None")
            like_flg = True 
            next_user = CustomUser.objects.get(id=liked_user_id)
        else:
            next_user = CustomUser.objects.exclude(id=request.user.id).filter(age__gte=user.age-2, age__lte=user.age+2, id__gt=user_id).first()    
        if not next_user:
            next_user = CustomUser.objects.exclude(id=request.user.id).filter(age__gte=user.age-2, age__lte=user.age+2).first()
  
        images = [photo.url for photo in [next_user.photo1, next_user.photo2, next_user.photo3, next_user.photo4, next_user.photo5, next_user.photo6] if photo]
        
        response_data = {
            'user_first_name': next_user.first_name,
            'user_last_name': next_user.last_name,
            'user_age': next_user.age,
            'user_desc': next_user.description,
            'user_sex': next_user.sex,
            'user_hobby': next_user.hobby,
            'user_main_goal': next_user.main_goal,
            'user_tg': next_user.telegram,
            'user_inst': next_user.inst,
            'user_x': next_user.x_network,
            'user_id': next_user.id,
            'like_flg': like_flg,
            'images': images
        }
        return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request'}, status=400)