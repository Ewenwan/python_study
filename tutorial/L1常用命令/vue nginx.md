cnpm install
npm run dev 开启
npm run build
ps -ef  查看wsgi进程 ps -ef | grep gunicorn
nginx -s reload 每次修改完nginx后都要运行这个命令重启一下
