/**
 * Created by nikosgpet on 09/10/15.
 */

var myServices = angular.module('myServices', []);

myServices.factory('nameService', ['$timeout', '$rootScope', '$log', '$http',
    function($timeout, $rootScope, $log, $http) {
    var postDigest = function(callback){
        var unregister = $rootScope.$watch(function () {
            unregister();
            $timeout(function () {
                callback();
                postDigest(callback);
            }, 0, false);
        });
    };

    var setReload = function() {
        postDigest(function(){
            $('.masonry-grid').isotope('reloadItems').isotope();
            $log.log('Items Reloaded');
        });
    };


    return {
        postDigest : postDigest,
        setReload : setReload
    };
}]);



