'use strict';

angular.module('sbirezApp')
  .controller('DocumentListCtrl', function ($scope, $http, $upload, $window) {
    $scope.jwt = $window.sessionStorage.token;
    $scope.progress = [];
    $scope.docList = [];
    $http.get('/api/documents').success(function(list) {
      console.log(list);
      $scope.docList = list.files;
    });

    $scope.uploadSuccess = function(data, status) {
      console.log('data: ' + data);
      console.log('status: ' + status);
      //console.log('headers: ' + headers);
      //console.log('config: ' + config);
      $http.get('/api/documents').success(function(list) {
        $scope.docList = list.files;
      });
    };

    $scope.onFileSelect = function($files) {
      $scope.selectedFiles = $files;
      $scope.progress = [];

      if ($scope.upload && $scope.upload.length > 0) {
        for (var i = 0; i < $scope.upload.length; i++) {
          if ($scope.upload[i] !== null) {
            $scope.upload[i].abort();
          }
        }
      }

      $scope.upload = [];
      $scope.uploadResult = [];

      for (var j = 0; j < $files.length; j++) {
        var file = $scope.selectedFiles[j];
        $scope.progress[j] = -1;
        $scope.upload = $upload.upload({
          url: '/api/documents',
          //data: {myObj: $scope.docModelObj},
          file: file,
        })
          .progress(function(evt) {
            console.log('loaded:' + Math.min(100, parseInt(100.0 * evt.loaded / evt.total)));
            $scope.progress[j] = Math.min(100,  parseInt(100.0 * evt.loaded /evt.total));
          })
          .success(function(data/*, status, headers, config*/) {
            console.log(data);
            $http.get('/api/documents').success(function(list) {
              $scope.docList = list.files;
            });
          });
      }
    };
  });