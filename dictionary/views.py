from django.shortcuts import render_to_response


def home(request):
    heading = 'Madyondza Dictionary'
    return render_to_response('home.html', {'heading': heading})
