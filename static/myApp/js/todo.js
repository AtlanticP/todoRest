var app = angular.module('toDo', []);
app.controller('toDoController', function($scope) {
	$scope.todoList = [{todoText: 'finish this app'}];
	$scope.todoAdd = function () {
		$scope.todoList.push({todoText: $scope.todoInput});
		$scope.todoInput = '';
	}
});