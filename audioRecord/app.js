var express = require('express')
    ,app = express()    
    ,http = require('http').Server(app)
    ,path = require('path')
    ,bodyParser = require('body-parser');


app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({limit: '50mb', extended: true}));

// Enable CORS
var allowCrossDomain = function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE");
    res.header("Access-Control-Allow-Headers", "Content-Type, Authorization, Content-Length, X-Requested-With");
    res.header("Access-Control-Allow-Credentials", true);
    next();
};

app.use(allowCrossDomain);

// define the configuration
app.set('port', process.env.PORT || 5000);
app.set('views', path.join(__dirname, 'public/views'));
app.engine('.html', require('ejs').__express);
app.set('view engine', 'html');
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

require('./routes/index.js').apply(app);
require('./api/config/route.js').apply(app);

http.listen(5000, function () {
    console.log('Express server listening on port *:'+app.get('port'));
});



