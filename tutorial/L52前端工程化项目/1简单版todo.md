简单版todo项目
===
## 步骤
1. nodejs npm cnpm
2. 安装vue-cli。 `npm install vue-cli -g`
3. 新建Vue工程项目。 `vue init webpack [project_name]`
4. 向导选项。 1> 会花费一点时间下载webpack模板 2>项目名、项目描述、作者保持默认 3>编译，选默认选项runtime+compiler 4>vue-router路由插件，小项目选no 5>ESLint前端代码风格审查工具，类似python中的PEP8，
选no 。6> unit tests、e2e tests单元测试，选no。7> run npm install创建工程后是否安装依赖，选noI will myself手动安装。
5. 安装依赖。 cd到项目根目录， npm install
6. 运行开发服务器。 根目录 npm run dev

## 项目组织大概解释
src放源代码  
.vue单页组件  
依赖babel js一直更新新语法，但浏览器可能还未支持，把新语法es6 es7转换为es2015老语法。
css-loader  
webpack 编译打包
项目入口 src/main.js

## 报错
1. 安装vue-cli ,报错 没有权限。解决使用管理员权限终端。
2. 前端包过多导致死机。解决 任务管理器终止项目，使用sublime。
3. (常见)npm run dev ,多样报错“提示集中在第三方包、跟npm无关”。确定代码没错。原因：由于cnpm组织包方式跟npm有所不同，或由于网络原因，总之依赖安装不正确。解决，删除node_modules文件夹，cnpm重装。建议npm安装。













## 参考
代码见同级目录 simple_vue_todo项目
参考图文 https://www.jianshu.com/p/a60f125fe10a
详细过程和前端概念了解见讲师录屏。


#