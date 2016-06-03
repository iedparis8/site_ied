/**
 * Created by nikosgpet on 16/10/15.
 */

myApp.directive('rule', function() {
   return {
       templateUrl: "static/angularjs/directives/rule.html",
       replace: true,
       scope : {
           rule: "@ruleName"
       }
   };
});