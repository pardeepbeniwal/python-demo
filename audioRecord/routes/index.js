exports.apply = function (app) {
    var self = this;
    app.all('*', function (err, req, res, next) {
        if (err) {
            res.render('404.html', {
                title : 'La Belle Assiette| Page Not Found'
            });
            console.log(err);
        } else {
           next(req, res);
        }
    });
}