from rest_framework import serializers

from todoRest.models import ToDoElements


class ToDoSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = ToDoElements
		fields = ('id', 'todo_text', 'done')

