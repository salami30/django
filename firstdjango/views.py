# django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



# def showText (request):
#    return HttpResponse ("Hello World")

#list method
# def showText (request):
#     list = [
# {
#
#   "name" : "Lateef"
#  },
#   {
#     "name" : "Salami"
#   } 
#    ]
#   return JsonResponse (list, safe=false)


# person
# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

def getUser (request):
    if request.method == 'GET':
      person = {
        "Lateef" : "Lateef",
        "Bio" : "I am Cool black guy",
        "Nationality" : "Nigerian"
    
    
    }
    return JsonResponse(person)
@csrf_exempt #must be remove before hosting or deploying your site
def addUser(request):
   if request.method == 'POST':
      # Decode the request to a string
      toString = request.body.decode('utf-8')

      # converts the utf-8 string to python dictionary or object
      user = json.loads(toString)
      print(user)
      return JsonResponse ({"message": "Your post has been succesfully added"}, status=200)
   else:
     return JsonResponse ({"error": "invalid request"}, status=405)



# PUT REQUEST - uPDATING DATA
def updateUser(request):
   if request.method == 'PUT':
      #store
      person = {
         "name" : "Miracle",
         "bio"  : "super cool"
      }
       #decode the request to a string
      toString = request.body.decode('utf-8')
      user = json.loads(toString)
      #convert the utf-8 string to python dictionary or object
      user = json.loads(toString)
      person["name"] = user ["name"]
      person["bio"] = user ["bio"]
      return JsonResponse({"message" : "Put request activatedd"})
   else:
      return JsonResponse({"error": "invalid request"}, status=405)
 


