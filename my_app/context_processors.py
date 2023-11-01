from my_app.models import MAINDETAILS

def contex_view(request):
    detail = MAINDETAILS.objects.last()
    return {'detail':detail}