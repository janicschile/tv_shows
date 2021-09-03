from django.shortcuts import render, redirect
from app.models import Show
from django.contrib import messages


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
    print(request.POST['title'])

    errors = Show.objects.basic_validator(request.POST)
        # compruebe si el diccionario de errores tiene algo en élcopy
    if len(errors) > 0:
        # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
        for keyNoShow, value in errors.items():
            messages.error(request, value)
        # redirigir al usuario al formulario para corregir los errores
        context = {
            "data_show_title": request.POST['title'],
            "data_show_network": request.POST['network'],
            "data_show_date": request.POST['date'],
            "data_show_description": request.POST['description']
        }
        return render(request, "new_show.html", context)
    else:
    
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
    messagePopup = f'Exito al Eliminar: TV Show "{showTitle}"'
    print(messagePopup)
    messages.error(request, messagePopup)

    return redirect(f'/shows')


def editShow(request, id):

    context = {
        "data_show": Show.objects.get(id=id)
    }
    return render(request, 'edit_show.html', context)


def saveShow(request, id):

    errors = Show.objects.basic_validator(request.POST)
        # compruebe si el diccionario de errores tiene algo en élcopy
    if len(errors) > 0:
        # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
        for keyNoShow, value in errors.items():
            messages.error(request, value)
        # redirigir al usuario al formulario para corregir los errores
        return redirect(f'/shows/{id}/edit')
    else:
    
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
        messagePopup = f'Exito al Modificar el TV Show:</br> "{title}"'
        print(messagePopup); messages.success(request, messagePopup)
        
        return redirect(f'/shows/{id}')




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