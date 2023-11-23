from django.shortcuts import render
from .models import person_collection
from .models import user_collection
from .models import main_Activities, main_plot, main_ProjectMaster, main_Treatment, main_Users
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>App is running</h1>")

def add_person(request):
    records={
        "first_name":"This is first",
        "last_name":"Note"
    }
    person_collection.insert_one(records)
    return HttpResponse("person added")

def get_all(request):
    persons = list(person_collection.find())
    serialized_persons = []

    for person in persons:
        serialized_persons.append({
            'first_name': person['first_name'],
            'last_name': person['last_name'],
        })

    return JsonResponse({'person': serialized_persons}, safe=False)

def get_users(request):
    persons = list(user_collection.find())
    context = {"persons": persons}
    return render(request, "notesApp/htmlTemplate.html", context)

def get_Main_Activities(request):
    persons = list(main_Activities.find())
    context = {"persons": persons}
    return render(request, "notesApp/htmlTemplate.html", context)

def get_Main_Plot(request):
    persons = list(main_plot.find())
    context = {"persons": persons}
    return render(request, "notesApp/htmlTemplate.html", context)

def get_Main_ProjectMaster(request):
    persons = list(main_ProjectMaster.find())
    context = {"persons": persons}
    return render(request, "notesApp/htmlTemplate.html", context)

def get_Main_Treatments(request):
    persons = list(main_Treatment.find())
    context = {"persons": persons}
    return render(request, "notesApp/htmlTemplate.html", context)

def get_Main_Users(request):
    persons = list(main_Users.find())
    context = {"persons": persons}
    return render(request, "notesApp/htmlTemplate.html", context)


def get_users_api(request):
    persons = list(user_collection.find())
    for person in persons:
        person['_id'] =str(person['_id'])
    context = {"persons": persons}
    return JsonResponse(context)
