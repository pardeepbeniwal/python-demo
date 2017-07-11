var fs = require('fs');
module.exports = {
    // the function to handle login page and after submit the page 
     index : function(req,res){			
		  res.render('index',{title:'Audio Recorder'});		
     },      
	 uploads: function(req,res){
			 var buf = new Buffer(req.body.blob, 'base64'); // decode
			  fs.writeFile("public/uploads/test.wav", buf, function(err) {
				if(err) {
				  console.log("err", err);
				} else {
				  return res.json({'status': 'success'});
				}
			  }) 
		},
     
};


