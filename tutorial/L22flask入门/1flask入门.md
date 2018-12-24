flask 入门
===
封装：tcp、 in http , socket, web开发框架。

## 安装
pip install flask

## (了解）flask 框架组成
在安装flask包时，flask依赖的相关包也会安装。
-flask  核心代码、方法封装
-Jinja2  前端渲染值得语法
-MarkupSafe 前端特殊字符转义，防止后端渲染时出现问题
-itsdangerous  加密和安全工具
-Werkzeug   德语，http协议封装。

## flask 约定俗成架构
.
├──model.py       类，数据库表结构                      模型层
├── app.py         路由、方法、业务逻辑、渲染模板方法   控制层
├── static         .css  .js   .jpg  静态资源文件        
└── templates      .html  网页静态文件                   视图层
