from django.shortcuts import render
from .models import Usuario
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Usuario, Entrenador


# Create your views here.

def index(request):
    #Generar contadores de algunos objetos
    num_usuario = Usuario.objects.all().count()
    num_entrenador = Entrenador.objects.all().count()


    #Renderiza o envia a la plantilla HTML index.html con los datos en las variables contexto
    return render(
        request,
        'index.html',
        context={'num_usuario':num_usuario, 'num_entrenador':num_entrenador},
    )

class UsuarioCreate(CreateView):
    model = Usuario
    fields ='__all__'
    
class UsuarioUpdate(UpdateView):
    model = Usuario
    fields= ['primer_nombre','apellido','fecha_nac','genero']

class UsuarioDelete(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario')

class EntrenadorCreate(CreateView):
    model = Entrenador
    fields ='__all__'
    
class EntrenadorUpdate(UpdateView):
    model = Entrenador
    fields= ['primer_nombre','apellido','fecha_nac','genero']

class EntrenadorDelete(DeleteView):
    model = Entrenador
    success_url = reverse_lazy('entrenador')
    

class UsuarioListView(generic.ListView):
    model = Usuario

    paginate_by=10

class EntrenadorListView(generic.ListView):
    model = Entrenador

    paginate_by=10
    
class UsuarioDetailView(generic.DetailView):
    model = Usuario

class EntrenadorDetailView(generic.DetailView):
    model = Entrenador

