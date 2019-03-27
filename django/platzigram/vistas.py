
# Django
from django.http import HttpResponse

# utilities
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! current server time  is {now}'.format(now=str(now)))
    # return HttpResponse('<h1>Hello, world</h1>')

def sorted_integers(request):
    # Return a JSON response with sorted integer. 

    numbers = [int (i) for i in request.GET['numbers'].split(',')] # convierte los valores ingresados de tipo str a enteros y los separa despues de la coma
    sorted_ints = sorted(numbers) # regresa la lista ordenada
    
    #onjeto tipo json
    data = {
        'status': 'ok',
        'numbers' : sorted_ints,
        'message' : 'Integers sorted successfully'
    }
    
    # Depurador 
    # import pdb; pdb.set_trace()
    #pasamos los datos para poder procesarlo similar a api
    return HttpResponse(json.dumps(data, indent=4), 
    content_type = 'application/json')

# si el elemento request, recibe mas argumentos, los puede procesar 
def say_hi(request, name = 'Irvyn', age = 11):

    if age < 12 :
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, welcome'.format(name)
    return HttpResponse(message)

