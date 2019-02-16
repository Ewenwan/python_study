未完成
## 介绍和作用
作用：高并发大量请求时管理请求队列，依次进入gunicorn的进程中，使web服务的性能进一步提高。同时比较擅长直接处理纯静态页面，纯静态页面不必通过django渲染出来。
### 正向和反向代理
正向场景：翻墙、爬虫时的代理ip
反向场景：nginx ngrok
参考 https://blog.csdn.net/u011456940/article/details/53633991
## nginx
### 安装
apt-get install nginx
### 配置 指向web服务
我的配置近供参考。
```
user www-data;
worker_processes auto;
pid /run/nginx.pid;

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
        gzip_disable "msie6";

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

        #### yangzheng edit
        server {
                listen 8003;
                listen 443 ssl;
                server_name www.1owo.com;
                root /home/yangzheng/myhexo;
                index index.html; 
                ssl_certificate   cert/214515904810241.pem;
                ssl_certificate_key  cert/214515904810241.key;
        }

        server {
                listen 80;
                server_name www.1owo.com;
                root /home/yangzheng/myhexo;
                index index.html;
                return 301 https://$server_name$request_uri;
                # rewrite ^(.*)$ https://www.1owo.com/index.html permanent;
                # error_page 404 https://www.1owo.com/index.html;
        }

        #server{
    #             listen 8003;
    #             server_name 127.0.0.1;
    #             location / {
    #                root /home/yangzheng/vue-todo/dist;
    #           }
    #    }
} # http end    

#mail {
#       # See sample authentication script at:
#       # http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
# 
#       # auth_http localhost/auth.php;
#       # pop3_capabilities "TOP" "USER";
#       # imap_capabilities "IMAP4rev1" "UIDPLUS";
# 
#       server {
#               listen     localhost:110;
#               protocol   pop3;
#               proxy      on;
#       }
# 
#       server {
#               listen     localhost:143;
#               protocol   imap;
#               proxy      on;
#       }
#}

```
### 检查配置和生效

### 最终梳理下思路
客户端浏览器(出xx.xx.xx.xx) → 阿里云服务器(云盾、安全组、防火墙) → (入8080端口)nginx负载均衡(出转发8000端口) → (入8000)gunicorn多进程(代理django wsgi app)→ django代码中。

## (选做)其它
### 静态文件托管
hexo静态博客
### https
#### (选做但建议做)申请https证书
阿里云有免费的
#### 配置
放在nginx的相关配置下



## (选做)supervisor

## 报错
1. ngnix配置后请求不到需要查看日志。nginx请求端口会自己加路由/index 所以你的网站没这个路由的话可能报404.
