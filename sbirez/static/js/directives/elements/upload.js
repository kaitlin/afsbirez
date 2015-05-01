'use strict';

angular.module('sbirezApp').directive('upload', function() {
  return {
    restrict: 'A',
    replace: true,
    scope: {
      upload: '=',
      proposal: '@',
      multiplename: '=?',
      multipletoken: '=?'
    },
    templateUrl: 'static/views/partials/elements/upload.html',
    controller: ['$scope', 'DocumentService', 'ProposalService',
      function ($scope, DocumentService, ProposalService) {
        $scope.element = $scope.upload;
        var fileId = null;
        $scope.validationstorage = '';
        $scope.visible = true;

        var validationCallback = function(data) {
          $scope.validationstorage = data;
        };

        var askIfCallback = function(data) {
          $scope.visible = data;
        };

        $scope.storage = ProposalService.register($scope.element,
                                 validationCallback,
                                 $scope.element.ask_if !== null ? askIfCallback : null,
                                 $scope.multipletoken);
        if (typeof $scope.storage === 'object') {
          $scope.storage = undefined; 
        }

        $scope.fieldName = $scope.element.human;
        if ($scope.multiplename !== undefined && $scope.element.human.indexOf('%multiple%') > -1) {
          $scope.fieldName = $scope.element.human.replace('%multiple%', $scope.multiplename);
        }

        $scope.apply = function() {
          ProposalService.apply($scope.element, $scope.storage, $scope.multipletoken);
        };

        if ($scope.storage !== undefined) {
          fileId = parseInt($scope.storage);
          if (fileId) {
            DocumentService.get(fileId).then(function(data) {
              $scope.selectedFiles = [];
              $scope.selectedFiles[0] = data;
              $scope.selectedFiles[0].filename = data.name;
            });
          }
        }

        $scope.onFileSelect = function($files) {
          $scope.selectedFiles = $files;
          $scope.progress = [];

          for (var j = 0; j < $scope.selectedFiles.length; j++) {
            $scope.selectedFiles[j].filename = $scope.selectedFiles[j].name;
            $scope.progress[j] = -1;
          }
        };

        $scope.start = function(index, id) {
          DocumentService.upload($scope.selectedFiles[index],
            $scope.selectedFiles[index].filename,
            $scope.selectedFiles[index].description,
            $scope.proposal,
            function(val) {console.log('progress', val);
          }).then(function(data) {
            $scope.storage = data.id;
            $scope.apply();
          });
        };
      }
    ]
  };
});
