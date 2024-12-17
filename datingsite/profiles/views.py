from django.shortcuts import render,redirect

def userprofile(request):
	if request.user.is_authenticated:
		user = request.user
		images = [user.photo1, user.photo2, user.photo3, user.photo4, user.photo5, user.photo6]
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
			images = [user.photo1, user.photo2, user.photo3, user.photo4, user.photo5, user.photo6]
			return render(request, 'editprofile.html', {'user': user, 'images': images})
	else:
		return redirect('login')