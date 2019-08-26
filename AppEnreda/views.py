from django.shortcuts import render
from .models import Creador

# Create your views here.
from django.views.generic import ListView
from .models import CrudUser
from AppEnreda import views
from .models import Creador
from django.views.generic import View
from django.http import JsonResponse

class CrudView(ListView):
    model = CrudUser
    template_name = 'crud.html'
    context_object_name = 'users'


def post_list(request):
    creador_list=Creador.objects.all
    crud_user=CrudUser.objects.all
    return render(request, 'crud.html', {'creador_list':creador_list, 'users':crud_user })   
    
    
class CreateCrudUser(View):

    def  get(self, request):
        note1 = request.GET.get('note', None)
        creador_list = request.GET.getlist('creador[]', None)
        creador=""
        for i in range(len(creador_list)):
            if creador!="":
                creador= creador +"|"
            creador= creador +creador_list[i]
        end_date1=request.GET.get('end_date', None)
        task1 = request.GET.get('task', None)
        tag1 = request.GET.get('tag', None)
        type1 = request.GET.get('type', None)
        
        obj = CrudUser.objects.create(
            note = note1,
            creador2= creador,
            end_date=end_date1,
            task=task1,
            tag=tag1,
            type=type1,
        )

        user = {'id':obj.id,'note':obj.note,'creador2': obj.creador2,'date':obj.date,'end_date':obj.end_date,'task':obj.task,'tag':obj.tag,'type':obj.type}

        data = {
            'user': user
        }
        return JsonResponse(data)   


class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        note1= request.GET.get('note',None) 
        creador_list= request.GET.get('creador2',None)
        end_date1=request.GET.get('end_date', None)
        task1 = request.GET.get('task', None)
        tag1 = request.GET.get('tag', None)
        type1 = request.GET.get('type', None)
        obj = CrudUser.objects.get(id=id1)
        obj.note= note1
        obj.creador2=creador_list
        obj.end_date=end_date1
        obj.task=task1
        obj.tag=tag1
        obj.type=type1
        obj.save()
        user = {'id':obj.id,'note':obj.note,'creador2':obj.creador2,'end_date':obj.end_date,'task':obj.task,'tag':obj.tag,'type':obj.type}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)