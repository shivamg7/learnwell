from django.contrib.auth.models import User
from bsl.models import user

myfile = open("names.csv",'r')

for i in range (1,2000):
  username = myfile.readline()


  try:
      User.objects.get(username=username)
  except User.DoesNotExist:
      User.objects.create_user(username,username+"@gmail.com","password")
      UserVar = User.objects.get(username=username)
      userVar = user(username=username,firstName=username,lastName="Smith",email=username+"@gmail.com",gender="M",profession="Engineer",rating=500)
      userVar.save()
      print(str(i)+"  "+username)

  print(username+" exits")
