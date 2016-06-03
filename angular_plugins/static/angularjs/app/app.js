/**
 * Created by nikosgpet on 09/10/15.
 */
var myApp = angular.module("myApp", [
    'ngRoute',
    'myServices'
]);

myApp.config(['$routeProvider', '$httpProvider', function($routeProvider, $httpProvider){
    $routeProvider
        .when('/', {
            templateUrl: "static/angularjs/partials/main.html",
            controller: 'mainController'
        })
        .when('/second', {
            templateUrl: "static/angularjs/partials/second.html",
            controller: 'secondController'
        })
        .when('/second/:num', {
            templateUrl: "static/angularjs/partials/second.html",
            controller: 'secondController'
        })
        .otherwise({
            redirectTo:'/'
        });

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);