from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
	def get(self,request,format=None):
		an_apiview=[
			'Uses HTTP methods as function (get, post, patch, put)',
 			'It is similar to a traditional Djnago view',
 			'Gives you the most control over the logic',
 			'Is mapped manually to URLs',
 		]
		return Response({'message': 'hello!', 'an_apiview': an_apiview})

