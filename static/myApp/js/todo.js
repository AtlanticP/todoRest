var app = angular.module('toDo', []);
app.controller('toDoController', function($scope) {
	$http.get('/todo/api/').then(function(response) {
		$scope.todoList = response.data;
	$scope.todoAdd = function () {
		$scope.todoList.push({todoText: $scope.todoInput, done: false});
		$scope.todoInput = '';
	};
	$scope.remove = function () {
		var oldList = $scope.todoList;
		$scope.todoList = [];
		angular.forEach(oldList, function(x) {
			if (!x.done) $scope.todoList.push(x);
		});
	};
});

