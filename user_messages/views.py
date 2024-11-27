from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message


@csrf_exempt
def receive_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        content = request.POST.get('content')

        if name and email and phone and date and content:
            Message.objects.create(name=name, email=email, phone=phone, date=date, content=content)
            return JsonResponse({"message": "Appointment booked successfully!"})
        else:
            return JsonResponse({"error": "Invalid request", 'message': 'Missing data'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


