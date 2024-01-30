# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .forms import FormSubmitForm  # Correct the import statement

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
