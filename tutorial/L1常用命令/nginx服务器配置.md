user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
	# multi_accept on;
}

http {

	##
	# Basic Settings
	##

	sendfile on;
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 65;
	types_hash_max_size 2048;
	# server_tokens off;

	# server_names_hash_bucket_size 64;
	# server_name_in_redirect off;

	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	##
	# SSL Settings
	##

	ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
	ssl_prefer_server_ciphers on;

	##
	# Logging Settings
	##

	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;

	##
	# Gzip Settings
	##

	gzip on;

	# gzip_vary on;
	# gzip_proxied any;
	# gzip_comp_level 6;
	# gzip_buffers 16 8k;
	# gzip_http_version 1.1;
	# gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

	##
	# Virtual Host Configs
	##

	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;


	############# custom
	server {
        listen 80;      # listen 80       注意安全组放通
        server_name 39.96.53.211;   # server_name www.1owo.com      注意www前缀的域名解析
        #root /home/trc/blog;     # 适合静态文件
        #index index.html;
        #access_log /yourproject/logss/nginx.access.log;#项目自己的日志   默认/var/log/nginx/下
        #error_log //yourproject/logss//nginx.error.log;#错误日志

        location / {
          proxy_pass http://127.0.0.1:8000;
         #请求转发给8000端口上的gunicorn      # www.1owo.com:80/article/1/ 转发为 39.96.114.97:8000/article/1/
         #proxy_set_header Host $host;
         #proxy_set_header X-Real-IP $remote_addr;
         #proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

         #location ~ ^/(media|static)/  {
         #root  /EdmureBlog/;  # 静态文件存放路径
         #expires 30d;
        #}
    }

    # vue-todo
    server{
         listen 8010;
         server_name 39.96.53.211;
         location / {
           root  /home/trc/vue-todo;
           index index.html;
         }
    }


}
#mail {
#	# See sample authentication script at:
#	# http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
#
#	# auth_http localhost/auth.php;
#	# pop3_capabilities "TOP" "USER";
#	# imap_capabilities "IMAP4rev1" "UIDPLUS";
#
#	server {
#		listen     localhost:110;
#		protocol   pop3;
#		proxy      on;
#	}
#
#	server {
#		listen     localhost:143;
#		protocol   imap;
#		proxy      on;
#	}
#}
