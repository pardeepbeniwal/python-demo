/* 
 * To handle group directly with model
 */
var async = require('async');
var _ = require('underscore');
var path = require('path');
var crypto = require('crypto');
var fs = require('fs');
module.exports = {    
     addgroup: function(req,res){
		var groupname = req.body.groupname;
		Schemas.UserGroup.findOne({groupname:groupname}, function(err, group){		
				if(!group)
				{		
					req.body.user_ids.push(req.user._id);
					var members = [];
						 for(var i in req.body.user_ids) {
							user_id = String(req.body.user_ids[i]);
							members.push(user_id);
						}								
					var UserGroup = new Schemas.UserGroup({ groupname:groupname,user_id:req.user._id,members:members});
					 UserGroup.save(function(err,result){
						 var group_id = result._id;
						 arr = {'group_id':group_id,'status':1,'message':'Group has been created successfully'};
						res.jsonp(arr);
					});
				}
				else
				{
					arr = {'status':0,'message':'This group has been created by some one else'};
					res.jsonp(arr);
				}
		})
       
	 }, 
	 getGroupLatestMessages: function(req,res){
			  varQuery = Schemas.GroupMessages.find({group_id:req.body.group_id}).sort({_id:'desc'}).limit(10);
			  varQuery.exec(function (err, clients) {				 
					if (err) {
						res.send({
							error : err
						});
						return false;
					} else if(clients.length > 0){
						async.waterfall([
						function(next){
							var userArr = [];
							var len = clients.length-1;
							var resArr = [];
							async.map(clients, function(client, cb){
								i = 0;
								Schemas.Users.findOne({_id:client.sender}, function(err, info){	
									resArr.push({ 
												"sender" : info.username,
												"message"  : client.message,
												"order"    : client._id 
											});
									if(i == len)
									{	
										res.jsonp(resArr);										
									}
									i++;									
								});
							},function(clients,next){});						
						}],
						function(err,clients){});					
				}
				else
				{
					var resArr  = [];
					res.jsonp(resArr);
				} //end else
			  });
		},
		view_groupInfo: function(req,res){
			 group_id = req.query.group;
			 userId = req.query.user_id;
			async.waterfall([
				function (callback) {
					varQuery = Schemas.UserGroup.findOne({_id:group_id});
					varQuery.exec(function (err, data) {
							callback(null, data);
						})
				},
				function (arg1, callback) {
					data = arg1;
					var userArr = [];
					var len = data.members.length-1;
					var resArr = [];				
					async.map(data.members, function(user, err){
						i = 0;
						Schemas.Users.findOne({_id:user}, function(err, info){	
							var groupname = data.groupname;
							var setadmin = 0;
						    var myGroup	 = 0; 
							if(user == data.user_id)
							{
								setadmin = 1;
							}
							if(data.user_id == userId)
							{
								myGroup = 1;
							}
							
							resArr.push({"Username" : info.username,"admin":setadmin,'myGroup':myGroup});
							if(i == len)
							{	
								var myDate = new Date(data.date_added);
								dt = myDate.getDate() + "/" + myDate.getMonth() + "/" + myDate.getFullYear();							
								resArr.push({ 
												"groupName" : groupname,
												'creation_date':dt
											});
								callback(null, resArr);										
							}
							i++;									
						});
					});
				}				
			], function (err, result) {
				res.jsonp(result);
			});			
		},
		exitfromGroup: function(req,res){
			var group_id = req.body.group_id;
			var user_id  = req.body.user_id;
			
			varQuery = Schemas.UserGroup.findOne({_id:group_id});
					varQuery.exec(function (err, data) {							
							var members = data.members;
							members = _.without(members, user_id);
								Schemas.UserGroup.update({_id: group_id}, {$set: {members: members}}, function(err, updated) {
								  if(!err)
								  {
									  var arr = {'status':1};									  
								  }
								  else
								  {
									  var arr = {'status':0};
								  }
								  res.jsonp(arr);
							});
						})
		},
		deleteGroup: function(req,res){
			var group_id = req.body.group_id;
			varQuery = Schemas.UserGroup.remove({_id:group_id});
			varQuery.exec(function (err, data) {
				 if(!err)
				  {
					  var arr = {'status':1};
				  }
				  else
				  {
					  var arr = {'status':0};
				  }
				  res.jsonp(arr);
			});
		},
		uploads: function(req,res){			
			var fstream;			
			req.pipe(req.busboy);
			req.busboy.on('file', function (fieldname, file, filename, encoding, mimetype) {
				var random_string = fieldname + filename + Date.now() + Math.random();
				newFilename =  crypto.createHash('md5').update(random_string).digest('hex');				
				var ext = path.extname(filename).toLowerCase();
				newFilename = newFilename + ext;
				fstream = fs.createWriteStream(rootPath+'/public/uploads/'+newFilename);
				file.pipe(fstream);
				var Attechment = new Schemas.Attechment({ type:'user',file_name:newFilename});
				Attechment.save(function(err,result){});
				fstream.on('close', function () {
					var picType=new Array('.jpeg', '.jpg', '.png', '.gif','.bmp');					
					if(_.contains(picType,ext)){
						var arr = {'status':1,'path':'<img src="uploads/'+newFilename+'" />'};
					}
					else
					{
						link = '<a href="/download?filename='+newFilename+'" target="_blank"><img src="images/download.png" /></a>';
						var arr = {'status':1,'path':link};
					}	
					res.jsonp(arr);
				});
			});
		},
		download: function(req, res){
			  var filename	= req.query.filename;
			  var file = rootPath+'/public/uploads/'+filename;
			  res.download(file);
		},
};


