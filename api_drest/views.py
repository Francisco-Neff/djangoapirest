import json
from django.views import View
from django.http import JsonResponse, QueryDict
from django.shortcuts import render
from .models import User_Rest
from .forms import User_Rest_Form
# Create your views here.

class User_View(View):
    """
    Vista para mostrar template inicial y todos los registros
    """
    template_name = 'user_drest_crud.html'
    context = {}

    def get(self, request,*args, **kwargs):
        self.context['form'] = User_Rest_Form()
        self.context['users'] = User_Rest.objects.all()
        return render(request,self.template_name,self.context) 


class UserCRUD_View(View):
    """
    Vista para manejar el modelo User_Rest con metodología CRUD
    """
    
    def get(self, request,id,*args, **kwargs):
        try: 
            user = User_Rest.serialize_user(id)
            return JsonResponse({'status':200,'message':'Se ha eliminado el registro correctamente','user':user})
        except Exception as e:
            return JsonResponse({'status':404,'message':'No se ha encontrado el registro','error':str(e)})

    def post(self, request,id,*args, **kwargs): 
        try:
            user = User_Rest(
                id=id,
                name_drest=request.POST['name'],
                email_drest=request.POST['email']
            )
            user.save()
            return JsonResponse({'status':200,'message':'Se ha creado el registro correctamente','user':user})
        except Exception as e:
            return JsonResponse({'status':404,'message':'No se ha creado el registro','error':str(e)})
    
    def put(self, request,id,*args, **kwargs):
        try:
            data = QueryDict(request.body)
            user_drest = User_Rest.objects.get(id=id)
            user_drest.name_drest = data['name']
            user_drest.email_drest = data['email']
            user_drest.save()
            user_drest = User_Rest.serialize_user(id)
            return JsonResponse({'status':200,'message':'Se ha modificado el registro correctamente','user':user_drest})
        except Exception as e:
            print('error',e)
            return JsonResponse({'status':404,'message':'No se ha modificado el registro','error':str(e)})

    def delete(self, request,id,*args, **kwargs): 
        try:
            User_Rest.objects.get(id=id).delete()
            return JsonResponse({'status':200,'message':'Se ha eliminado el registro correctamente','id':id})
        except Exception as e:
            return JsonResponse({'status':404,'message':'No se ha eliminado el registro','error':str(e) })
