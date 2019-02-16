npm install hexo -g #安装

npm update hexo -g #升级

hexo init #初始化

hexo new "postName" #新建文章

hexo new page "pageName" #新建页面

hexo generate #生成静态页面至public目录

hexo server #开启预览访问端口（默认端口4000，'ctrl + c'关闭server）

hexo deploy #将.deploy目录部署到GitHub

hexo n #写文章

hexo g #生成

hexo d #部署 #可与hexo g合并为hexo d -g 



一般操作，在博客下调出cmd命令窗口：

hexo new "xx"

在E:\MyBlog\source\_posts下，找到xx.md

用markdown抒写，完成后，先开启本地测试hexo s

没有问题后，hexo d -g
