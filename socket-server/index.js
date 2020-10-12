var droid = new Android();

(function () {
  'use strict';
  
  
angular.module('naolMobi',['ngMaterial','ngAria','ngAnimate','ngRoute','btford.socket-io'])
     .config(['$mdIconProvider','$mdAriaProvider','$mdInkRippleProvider', function($mdIconProvider,$mdAriaProvider,$mdInkRippleProvider) {
     	$mdInkRippleProvider.disableInkRipple();
     $mdAriaProvider.disableWarnings();
    $mdIconProvider
      .iconSet('social', 'img/icons/sets/social-icons.svg', 24);
      $mdIconProvider.iconSet('core', 'img/icons/sets/core-icons.svg', 24);
      $mdIconProvider.iconSet('device', 'img/icons/sets/device-icons.svg', 24);
      $mdIconProvider.iconSet('communication', 'img/icons/sets/communication-icons.svg', 24);
 }])
 .factory('socket', function (socketFactory) {
  return socketFactory({
    prefix: 'socket:',
    ioSocket: io.connect('http://127.0.0.1:8009/xx')
  });
})
.controller('AppController',AppController)

.run(function($templateRequest) {

    var urls = [
      'file:///sdcard/sl4a/scripts/Examples/starter/bottom-sheet-list-template.html'
    ];

  //  angular.forEach(urls, function(url) {
    //	alert(url);
      //$templateRequest(url);
    //});

  });

 function AppController(socket,$scope,$mdColors,$timeout,$mdSidenav,$log,$mdDialog,$mdColorPalette,$mdMenu,$mdBottomSheet) {
 	var self=this;
 	self.check="1234";
 self.logs=[];
 
  self.socket=socket;
  
  self.right_open=false;
  $scope.tggle=function(snId){
  	
  $mdSidenav(snId).toggle().then(function () {
  self.right_open=!self.right_open;
 // alert();
  $timeout(function(){$scope.$apply()},500);
  });
  
  }
  
 //md bottom sheet
 self.loaded=false;
 
self.editors={};
self.editor_values={};

 self.droid=droid;
 
 // colors}
 self.toolbar_visible=false;
self.toggleToolbar=function(){
	self.toolbar_visible=!self.toolbar_visible;
	}
 	//sidenav control
 	self.toggleLeft = buildDelayedToggler('left');
	 self.toggleRight= buildDelayedToggler('right');
    self.sock_server={ip:"127.0.0.1",port:8001,name:"poc"};
$scope.sock_servers=[];
self.server_running=false;
function debounce(func, wait, context) {
      var timer;

      return function debounced() {
        var context = $scope,
            args = Array.prototype.slice.call(arguments);
        $timeout.cancel(timer);
        timer = $timeout(function() {
          timer = undefined;
          func.apply(context, args);
        }, wait || 0);
      };
    }
    function buildDelayedToggler(navID) {
      return debounce(function() {
        // Component lookup should always be available since we are not using `ng-if`
        $mdSidenav(navID)
          .toggle()
          .then(function () {
            $log.debug("toggle " + navID + " is done");
          });
      }, 1);
    }
    //fab control
    
	
	self.propt={};
	
		
		
    self.fabopen=false;
    $timeout(function(){
      
      
      
       
      self.loaded=true;
      
      
      
     $scope.$apply();
     jQuery(document).ready(function(){
		//alert(window.outerHeight);
		//angular.element("#log").css({'height':window.outerHeight-200+"px"});
		//angular.element("#main").css({'height':window.height+"px"});
		//angular.element("#tb").css({"height":window.outerHeight+"px"});
		//angular.element("#cc").css({"height":window.outerHeight+"px"});
		//angular.element("#cfnt").css({"height":window.outerHeight+"px"});
		//angular.element("#tb").hide();
		FastClick.attach(document.body);
		})
      },5000);

    // create node using json string
    
 
 
 	//callbacks from the server
	droid.registerCallback('server_status', function(e) {
		//alert(e.data);
		
		if(e.data == "running"){
	               self.server_running=true;
	self.sock_start();
	self.toggleRight();
	$scope.sock_servers.push(self.current);
	//self.sock_start();
	$timeout(function(){
		$scope.$apply()},1000);
	}
	if(e.data == "stopped"){
	                self.server_running=false;
	//alert(self.cur_ind);
	$scope.sock_servers.splice(parseInt(self.cur_ind), 1);
	self.toggleLeft();
	$timeout(function(){
		$scope.$apply()},1000);
	}
	})
	
	
	droid.registerCallback('my_event', function(e) {
		//alert(e.data);
		//alert(e.data);
		//alert();
		self.logs.push(e.data);
		$timeout(function(){
		$scope.$apply()},500);
	
	})
	var socketx=false;
	droid.registerCallback('connected', function(e) {
		//alert(e.data);
		//alert(e.data);
		
		self.logs.push(e.data);
		$timeout(function(){
		$scope.$apply()},500);
		//$('#evemt').click();
	 
	})
	
	
    //send data to server
     self.scrollToBottom=function(id){
var  div_height = $("#"+id).height();
  var div_offset = $("#"+id).offset().top;
var  window_height = $(window).height();
  $('html,body').animate({
    scrollTop: div_offset-window_height+div_height
  },'slow');
}
        self.x=0;
 	//send data to server
	self.send=function(event,data){
		droid.eventPost(event,JSON.stringify(data));
		}
		//var socket=io.connect('http://127.0.0.1:8001/poc')
		self.socks=[];
			var x=1;
			self.sock_start=function(){ 
				var data=self.current;
				var sok=io.connect('http://'+data.ip+':'+data.port+'/poc')
				self.socks.push(sok);
		self.socks[self.socks.length-1].on('connect', function (t) {
    	// alert(t);
    x=x+1;
    self.logs.push("connected " +x);
    //$scope.bar = t;
    $timeout(function(){$scope.$apply()},500);
  });
  
		self.socks[self.socks.length-1].on('bar', function (t) {
    	// alert(t);
    self.x=self.x+1;
    self.logs.push(angular.copy(t));
    self.tt=t;
    //self.scrollToBottom('log');
    //alert($("#log")[0].scrollHeight);
    $("#log").scrollTop($('#log')[0].scrollHeight )
    //$scope.bar = t;
    $timeout(function(){$scope.$apply()},500);
  });
  
  self.socks[self.socks.length-1].on('reconnect', function (t) {
    	// alert(t);
        x=x+1;
    self.logs.push('reconnected '+x);
   // self.socks[self.socks.length-1].emit("task","xft");
    //$scope.bar = t;
    $timeout(function(){$scope.$apply()},500);
  });
  self.socks[self.socks.length-1].on('disconnect', function (t) {
    	// alert(t);
    
    x=x+1;
    self.logs.push('disconnected  '+x);
    //socket.emit("task","hello");
    //$scope.bar = t;
    $timeout(function(){$scope.$apply()},500);
  });
  }
  //self.sock_start();
  //self.sock_start();
		self.start_server=function(event,data){
			
			//socket=io.connect('http://127.0.0.1:8001/poc');
			//socket.emit("task","ttyf");
			
			self.current=angular.copy(self.sock_server);
		droid.eventPost(event,JSON.stringify(data));
		}
		self.stop_serv=function(index,data){
			self.cur_ind=index;

 // self.socks.splice(self.cur_index, 1);
	data.item_index=index;

		droid.eventPost('stop_server',JSON.stringify(data));
		}
		self.select_server=function(index,data){
			self.sock_server=$scope.sock_servers[index];
			self.current=$scope.sock_servers[index];
			$timeout(function(){$scope.$apply()},500);
			self.toggleLeft();
		//droid.eventPost(event,JSON.stringify(data));
		}
		
	//kill app
	self.kill=function(){
		if($scope.sock_servers.length > 0){
		 alert("please close all servers");
		return
		}
		droid.eventPost('kill', '');
		}
		
		
		
		}
    
    })(angular);