from django.shortcuts import render,redirect

def userprofile(request):
	if request.user.is_authenticated:
		user = request.user
		images = [user.photo1, user.photo2, user.photo3, user.photo4, user.photo5, user.photo6]
		return render(request, 'userprofile.html', {'user': user, 'images': images})
	else:
		return redirect('login')