from rest_framework.views import APIView
from rest_framework.response import Response

from todoRest.serializers import ToDoSerializer
from todoRest.models import ToDo

class ToDoView(APIView):
	
	def get(self, request):
		todos = ToDo.objects.all()
		serializer = ToDoSerializer(todos, many=True)
		
		return Response(serializer.data)
		
		# def get(self, request):
		# 	return Response({'test':'It worked'})