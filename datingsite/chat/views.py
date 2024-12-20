from django.shortcuts import render, redirect


def allchats(request):
    return render(request, 'allchats.html')