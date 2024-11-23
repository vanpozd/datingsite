from django.shortcuts import render


def userprofile(request):
	user = request.user
	return render(request, 'userprofile.html', {'user': user})