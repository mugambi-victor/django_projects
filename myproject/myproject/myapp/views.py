# myapp/views.py
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse
from .forms import FormSubmitForm

@api_view(['POST'])
def submit_form(request):
    if request.method == 'POST':
        form = FormSubmitForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Form submitted successfully!'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'This endpoint only accepts POST requests.'}, status=405)
