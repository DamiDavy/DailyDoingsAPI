from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
import json
from django.http import JsonResponse, HttpResponse
from django.db import IntegrityError

from .models import User, Todo

def hi(request):
  return HttpResponse("Hi!")

@csrf_exempt
def login_view(request):
  if request.method == "POST":

    data = json.loads(request.body)
      # post_data = json.loads(request.body.decode("utf-8"))

    name = data.get("login")
    password = data.get("password")

    # Attempt to sign user in
    # email = request.POST["email"]
    # password = request.POST["password"]
    user = authenticate(request, username=name, password=password)

    # Check if authentication successful
    if user is not None:
      login(request, user)
      return JsonResponse({"message": "Authenticated successsfully", "login": request.user.username, "result": 0}, status=200)
    else:
      return JsonResponse({"message": "Invalid email and/or password", "result": 1}, status=401)
  else:
    return render(request, "handling/login.html")

@csrf_exempt
def is_logged_in(request):
  if request.method == "POST":
    user = request.user

    data = json.loads(request.body)
      # post_data = json.loads(request.body.decode("utf-8"))

    name = data.get("login")
    if user.username == name and name != '': 
      return JsonResponse({"message": "Authenticated", "login": request.user.username, "name": name, "result": 0}, status=200)
    else: 
      return JsonResponse({"message": "Unauthorized", "login": request.user.username, "name": name, "result": 1}, status=401)


def logout_view(request):
    logout(request)
    return JsonResponse({"message": "Logged Out", "result": 0}, status=200)

@csrf_exempt
def register(request):
  if request.method == "POST":

    data = json.loads(request.body)

    login = data.get("login")
    email = data.get("email")
    password = data.get("password")
    confirmation = data.get("confirmation")

    if password != confirmation:
      return JsonResponse({"message": "Passwords must match", "result": 1}, status=400)

    try:
      user = User.objects.create_user(login, email, password)
      user.save()
    except IntegrityError:
      return JsonResponse({"message": "Username've been already taken", "result": 1}, status=400)

    # login(request, user)
    return JsonResponse({"message": "Registered successfully", "result": 0}, status=200)
  else:
    return render(request, "handling/registration.html")

@csrf_exempt
# @login_required
def todos(request):
  if request.method == "POST":
    data = json.loads(request.body)
    login = data.get("login")
    year = data.get("year")
    month = data.get("month")
  # current_user = request.user
    user_todos = Todo.objects.filter(user=login, year=year, month=month)
    # user_todos = Todo.objects.all()
    return JsonResponse([todo.serialize() for todo in user_todos], safe=False)


@csrf_exempt
# @login_required
def add_delete_todo(request):
  if request.method == "POST":

    data = json.loads(request.body)

    user = data.get("user")
    title = data.get("title")
    date = data.get("date")

    date_as_list = date.split("-")

    # current_user = request.user

    todo = Todo(user=user, title=title, year=date_as_list[0], month=date_as_list[1], day=date_as_list[2])
    todo.save()

    return JsonResponse({"message": "Todo've been saved successfully", "user": user, "result": 0}, status=200)

  elif request.method == "PUT":
    data = json.loads(request.body)
    todo_id = data.get("id")
    Todo.objects.get(pk=todo_id).delete()
    return JsonResponse({"message": "Todo've been deleted successfully", "result": 0}, status=200)
  else:
    return render(request, "handling/add_delete_todo.html")