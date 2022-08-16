from logging.config import IDENTIFIER
import requests
import json
from django.shortcuts import render
#from Proyecto_API.api.models import Contact
from .models import Contact



from hubspot import HubSpot
from hubspot.crm.contacts import ApiException
from hubspot.crm.contacts import SimplePublicObjectInput


def crear(nombre, apellido, email, celular):
  api_client = HubSpot(access_token= 'pat-na1-a677ee48-431f-488d-bfa4-f3abc2cb5b5c')

  all_contacts = api_client.crm.contacts.get_all()

  for i in all_contacts:
    if i.properties['email'] == email:
      id = i.properties['hs_object_id']

    try:
      simple_public_object_input = SimplePublicObjectInput(
          properties={"firstname": nombre,
                    "lastname": apellido,
                    "phone": celular}
      )
      api_response = api_client.crm.contacts.basic_api.update(id,
          simple_public_object_input=simple_public_object_input
      )

  
    except ApiException as e:
      print("Exception when creating contact: %s\n" % e)

    
    

def form(request):
  if request.method=='POST':
    nombre = request.POST['nombre']
    apellido = request.POST['lastname']
    email = request.POST['email']
    celular = request.POST['phone']
    contacto = Contact(name=nombre, lastname=apellido, email=email, phone=celular)
    contacto.save() 
    crear(nombre, apellido, email, celular)
    cont = []
    for contactos in Contact.objects.all():
      cont.append(contactos)
    return render(request, 'Registro.html',{'contact': cont})  
    
  return render(request,'contactos.html') 

def TerminosYCondiciones(request):
    return render(request, 'TerminosYCondiciones.html')

def eliminar(request):
    return render(request, 'eliminar.html')


    



