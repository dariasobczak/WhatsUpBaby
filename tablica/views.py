from django.shortcuts import render, render_to_response

def posty(request):
    return render(request, 'posty.html')