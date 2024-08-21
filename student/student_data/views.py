import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse

API_BASE_URL = 'http://127.0.0.1:5000'

# def student_list(request):
#     response = requests.get(f'{API_BASE_URL}/display')
#     students = response.json()
#     return render(request, 'student_data/student_list.html', {'students': students})

def student_list(request):
    # Make a GET request to the Flask API
    response = requests.get('http://127.0.0.1:5000/display')  # Update the port if your Flask app uses a different one

    if response.status_code == 200:
        students = response.json()  # Assuming the response is in JSON format
    else:
        students = []

    return render(request, 'student_data/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        data = {
            'no': request.POST['no'],
            'name': request.POST['name'],
            'email': request.POST['email']
        }
        requests.post(f'{API_BASE_URL}/insert', json=data)
        return redirect('student_list')
    return render(request, 'student_data/student_form.html')

def student_update(request, pk):
    if request.method == 'POST':
        data = {
            'no': pk,
            'name': request.POST['name'],
            'email': request.POST['email']
        }
        requests.put(f'{API_BASE_URL}/update', json=data)
        return redirect('student_list')
    student = requests.get(f'{API_BASE_URL}/display').json()
    student = next((s for s in student if s[0] == pk), None)
    return render(request, 'student_data/student_form.html', {'student': student})

def student_delete(request, pk):
    requests.delete(f'{API_BASE_URL}/delete', json={'no': pk})
    return redirect('student_list')