from django.views import View
from django.http import JsonResponse

# Function based view
def show_message_success(request):
    data = {
        "message": "successs!!!!!",
        # "age": 20,
        # "hobbies": ["Coding", "Art", "Gaming", "Cricket", "Piano"]
    }
    if request.method == 'GET':
        return JsonResponse(data, status=200)
    else:
        return JsonResponse(message='error', status=400)