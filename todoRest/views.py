from rest_framework.views import APIView
from rest_framework.response import Response

from todoRest.serializers import ToDoSerializer


class ToDoView(APIView):
	
	def get(self, request):
		serializer = ToDoSerializer
		
		return Response(serializer.data)