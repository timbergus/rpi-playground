const Koa = require('koa');
const koa = new Koa();
var bodyParser = require('koa-bodyparser');
var cors = require('kcors');
const convert = require('koa-convert')

koa.use(convert(cors()));
koa.use(bodyParser());

koa.use((ctx) => {
    console.log(ctx.request.body);
    
    ctx.statusCode = 200;
    ctx.body = 'We have a body!';
});

koa.listen(5000);
