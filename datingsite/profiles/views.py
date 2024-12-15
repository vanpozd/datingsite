from django.shortcuts import render,redirect

def userprofile(request):
	if request.user.is_authenticated:
		user = request.user
		return render(request, 'userprofile.html', {'user': user})
	else:
		return redirect('login')