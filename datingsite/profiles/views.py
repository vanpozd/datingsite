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
			user.sex = request.POST['sex']
			user.save()
		else:
			return render(request, 'editprofile.html', {'user': user})
	else:
		return redirect('login')