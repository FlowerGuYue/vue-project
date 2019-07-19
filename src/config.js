let server='';

if(process.env.NODE_ENV=='development'){
  server='http://172.18.48.152:80/';
}else{
  server='http://172.18.48.152:80/';
}

export const SERVER=server;
