from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
import json
from django.http import JsonResponse, HttpResponse
from django.db import IntegrityError
from datetime import timedelta, date

# from .models import User, Todo, Session
# from .utils import session_is_valid

def index(request):
  return render(request, "handling/index.html")

# @csrf_exempt
# def login_view(request):
#   if request.method == "POST":

#     data = json.loads(request.body)

#     name = data.get("login")
#     password = data.get("password")

#     user = authenticate(request, username=name, password=password)

#     if user is not None:
#       login(request, user)

#       session = Session(user=user)
#       session.save()

#       return JsonResponse({"message": "Authenticated successsfully", "login": request.user.username, "session": session.id, 
#         "result": 0}, status=200)
#     else:
#       return JsonResponse({"message": "Invalid email and/or password", "result": 1}, status=401)
#   else:
#     return JsonResponse({"message": "Method Not Allowed", "result": 1}, status=405)

# @csrf_exempt
# def is_logged_in(request):
#   if request.method == "POST":
#     data = json.loads(request.body)
#     session_id = data.get("session")
#     user = session_is_valid(session_id)

#     if user is not None:
#       return JsonResponse({"message": "Authenticated", "session": session_id, "name": user.username, "result": 0}, status=200)
#     else: 
#       return JsonResponse({"message": "Unauthorized", "result": 1}, status=401)
#   else:
#     return JsonResponse({"message": "Method Not Allowed", "result": 1}, status=405)


# @csrf_exempt
# def logout_view(request):
#   if request.method == "POST":
#     data = json.loads(request.body)
#     session = data.get("session")
#     Session.objects.get(pk=session).delete()
#     logout(request)
#     return JsonResponse({"message": "Logged Out", "result": 0}, status=200)
#   else:
#     return JsonResponse({"message": "Method Not Allowed", "result": 1}, status=405)

# @csrf_exempt
# def register(request):
#   if request.method == "POST":

#     data = json.loads(request.body)

#     login = data.get("login")
#     email = data.get("email")
#     password = data.get("password")
#     confirmation = data.get("confirmation")

#     if password != confirmation:
#       return JsonResponse({"message": "Passwords must match", "result": 1}, status=400)
      

#     try:
#       user = User.objects.create_user(login, email, password)
#       user.save()
#     except IntegrityError:
#       return JsonResponse({"message": "Username've been already taken", "result": 1}, status=400)
#     return JsonResponse({"message": "Registered successfully", "result": 0}, status=200)

#   else:
#     return JsonResponse({"message": "Method Not Allowed", "result": 1}, status=405)

# @csrf_exempt
# def todos(request, session, year, month):
#   user = session_is_valid(session)

#   if user is None:
#     return JsonResponse({"message": "Unauthorized", "result": 1}, status=401)

#   user_todos = Todo.objects.filter(user=user, year=year, month=month)

#   return JsonResponse([todo.serialize() for todo in user_todos], safe=False)

# @csrf_exempt
# def add_delete_todo(request):
#   if request.method == "POST":

#     data = json.loads(request.body)

#     title = data.get("title")
#     date = data.get("date")
#     session_id = data.get("session")

#     user = session_is_valid(session_id)

#     if user is None:
#       return JsonResponse({"message": "Unauthorized", "result": 1}, status=401)

#     date_as_list = date.split("-")

#     todo = Todo(user=user, title=title, year=date_as_list[0], month=date_as_list[1], day=date_as_list[2])
#     todo.save()
#     return JsonResponse({"message": "Todo've been saved successfully", "result": 0}, status=200)

#   elif request.method == "PUT":
#     data = json.loads(request.body)
#     todo_id = data.get("id")
#     Todo.objects.get(pk=todo_id).delete()
#     return JsonResponse({"message": "Todo've been deleted successfully", "result": 0}, status=200)
#   else:
#     return JsonResponse({"message": "Method Not Allowed", "result": 1}, status=405)