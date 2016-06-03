/**
 * Created by nikosgpet on 09/10/15.
 */

myApp.controller('mainController', ['$rootScope', '$scope', '$http', '$log', '$timeout', 'nameService',
    function($rootScope, $scope, $http, $log, $timeout, nameService) {

    $scope.name = 'Rules';


    $scope.getRules = function() {
        $http.get('/api/rules/')
        .success(function (result){
            $scope.rules = result.slice(-5);
        })
        .error(function (data, status){
            $log.log(data);
        });
    };
    $scope.getRules();

    $scope.newRule = '';
    $scope.addRule = function () {
        $http.post('/api/rules/', { rule: $scope.newRule })
            .success(function (result){
                $scope.newRule = "";
                $scope.getRules();
            })
            .error(function(data, status){
                $log.log(data);
            });
    };
    nameService.setReload();

}]);

myApp.controller('secondController', ['$scope', '$log', '$routeParams', 'nameService', '$http',
    function($scope, $log, $routeParams, nameService, $http){
    $scope.name = 'Second';
    //$scope.rule = 'Always be on time';


    $scope.getRules = function() {
        $http.get('/api/rules/')
        .success(function (result){
            $scope.rules = result.slice(-5);
        })
        .error(function (data, status){
            $log.log(data);
        });
    };
    $scope.getRules();

    nameService.setReload();
}]);