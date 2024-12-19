from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import json

def userprofile(request):
	if request.user.is_authenticated:
		user = request.user
		images = [photo for photo in [user.photo1, user.photo2, user.photo3, user.photo4, user.photo5, user.photo6] if photo]
		return render(request, 'userprofile.html', {'user': user, 'images': images})
	else:
		return redirect('login')
	
def editprofile(request):
	if request.user.is_authenticated:
		user = request.user
		if request.method == 'POST':
			user.first_name = request.POST['first_name']
			user.last_name = request.POST['last_name']
			user.description = request.POST['description']
			user.age = request.POST['age']
			user.sex = request.POST['sex']
			user.hobby = request.POST['hobby']
			user.main_goal = request.POST['main_goal']
			user.inst = request.POST['inst']
			user.telegram = request.POST['telegram']
			user.x_network = request.POST['x_network']
			user.save()
			return redirect('profile')
		else:
			images = [photo for photo in [user.photo1, user.photo2, user.photo3, user.photo4, user.photo5, user.photo6] if photo]
			return render(request, 'editprofile.html', {'user': user, 'images': images})
	else:
		return redirect('login')
	

def delete_image(request, image_id):
	if request.user.is_authenticated:
		user = request.user
		if image_id == 1:
			
			user.photo1 = None
		elif image_id == 2:
			user.photo2 = None
		elif image_id == 3:
			user.photo3 = None
		elif image_id == 4:
			user.photo4 = None
		elif image_id == 5:
			user.photo5 = None
		elif image_id == 6:
			user.photo6 = None
		user.save()
		return redirect('editprofile')
	else:
		return redirect('login')
	
def upload_image(request):
	if request.user.is_authenticated:
		user = request.user
		if request.method == 'POST':
			data = json.loads(request.body)
			photo = data.get('image')
			image_id = int(data.get('image_counter'))
			if image_id == 1:
				user.photo1 = photo
			elif image_id == 2:
				user.photo2 = photo
			elif image_id == 3:
				user.photo3 = photo
			elif image_id == 4:
				user.photo4 = photo
			elif image_id == 5:
				user.photo5 = photo
			elif image_id == 6:
				user.photo6 = photo
			user.save()
			return redirect('editprofile')
		else:
			return redirect('editprofile')
	else:
		return redirect('login')