vue项目部署
===
以 vue-todo项目为例 。https://github.com/canaan-yz/vue-todo
1. 确认项目本地正常运行：clone项目、安装依赖、npm run dev。
解释：在chrome开发者工具中看network，整个项目只有index.html和打包所有功能后的xxx.js.
2. 编译打包 npm run build 。
解释：执行后项目生成dist文件夹。双击index.html可独立执行。
3. 将dist文件夹下index.html和 main.js上传的服务器。
小贴士：使用pycharm自带deployment工具的话注意配置路径时本地只需上传dist文件夹下的。
4. nginx代理静态文件。
小贴士：pycharm/tools/deployment/browse remote server ，找到nginx.conf双击打开，工具会帮助自动下载到本地供编辑，省去了上传再命令覆盖原配置文件的操作。
```
server{
     listen 8003;
     server_name 127.0.0.1;
    location / {
        root /home/yangzheng/vue-todo/dist;
        index  index.html;
   }
}
```
注意配置文件;号。每个server间不用加逗号。