from django.shortcuts import render, redirect
from app.models import Show
from django.contrib import messages
from django.utils import timezone
from datetime import datetime

# Create your views here.
def index(request):
	context = {
	}
	return redirect(f'/shows')
    
    
def newShow(request):
    context = {
    }
    return render(request, "new_show.html", context)




def createShow(request):
    print(request.POST['date'])
    
    # Agregamos formulario a la BD
    Show.objects.create(
        title = request.POST['title'],
        network=request.POST['network'],
        date=request.POST['date'], 
        description=request.POST['description'])
    
    #Obtenemos ID 
    id = Show.objects.last().id
    showTitle = Show.objects.get(id=id).title

    messagePopup = f'El TV Show "{showTitle}", ha sido creado correctamente'
    print(messagePopup)
    messages.success(request, messagePopup)

    # Redireccion a pagina mostrando los datos ingresados
    return redirect(f'/shows/{id}')




def deleteShow(request, id):
    showTitle = Show.objects.get(id=id).title
    elimina = Show.objects.get(id=id)
    elimina.delete()
    messagePopup = f'Exito al Eliminar el TV Show "{showTitle}"'
    print(messagePopup)
    messages.warning(request, messagePopup)

    return redirect(f'/shows')


def editShow(request, id):

    context = {
        "data_show": Show.objects.get(id=id)
    }
    return render(request, 'edit_show.html', context)


def saveShow(request, id):
    
    fecha = request.POST['date']
    title = request.POST['title']
    network = request.POST['network']
    description = request.POST['description']
    print(f"\n\nTitulo: {title}\nCanal: {network}\nFecha: {fecha}\nDescripcion: {description}\n\n")
    actualiza = Show.objects.get(id=id)
    actualiza.title = title
    actualiza.network = network
    actualiza.date = fecha
    actualiza.description = description
    actualiza.save()
    
    # Muestra mensaje Exito
    messagePopup = f'Exito al Modificar el TV Show "{title}"'
    print(messagePopup); messages.success(request, messagePopup)
    
    return redirect(f'/shows')




def viewShow(request, id):
    context = {
        "data_show": Show.objects.get(id=id)
    }
    return render(request, 'view_show.html', context)



def index_shows(request):
    context = {
        "data_show": Show.objects.all()
    }
    return render(request, 'shows.html', context)