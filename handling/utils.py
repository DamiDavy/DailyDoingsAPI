# from datetime import timedelta, date

# from .models import Session

# def session_is_valid(pk):
#   session = Session.objects.get(pk=pk)

#   today = date.today()
#   if (session.creation_date + timedelta(days=7) < today):
#     session.delete()

#   if session is not None:
#     return session.user
#   else: 
#     return None