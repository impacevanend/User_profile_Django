from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class HelloApiVie(APIView):
    
    '''API View de prueba '''
    
    def get(self, request, format=None):
        """Retornar lista de caracteristicas del APIview"""
        an_apiview = [
            'Usamos métodos HTTP como funciones (get, post, patch, put, delete)',
            'ES similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la lógica de nuestra aplicación',
            'Está mapeado manualmente a los urls',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

