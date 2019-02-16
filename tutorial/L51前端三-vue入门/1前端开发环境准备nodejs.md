## nodejs
1. 官网 
2. exe
3. 环境变量
### (选做)包管理工具npm cnpm
由于一些众所周知的原因。类似换pip源。
1. 安装淘宝镜像 
cnpm
2. 常用命令 
`cnpm install xxx`   install 可以简写成i
`cnpm install xxx -g`     -g参数代表global全局,安装完包后可以调用这个包的命令。类似django安装完后path下有一个django-admin.exe脚本。

(练习)安装httpserver包并开启局域网文件共享。

## (选做)IDE webstorm
类似安装pycharm。

## nodejs的包管理
nodejs的包管理跟python相似但不同
### package.json
介绍:package.json是前端工程项目的依赖描述文件，类似pip中requirements.txt。
安装依赖: cd到项目根目录后`npm install`安装。文件格式json。
版本值说明: （比python pip描述的精细）2.3.11 分别为大版本、中版本、小版本号。latest最新版。^ 同一大版本下的最新版。 什么都不加确定某个版本。
### node_modules
执行npm install后项目根目录下生成node_modules，里面各种包，类似python解释器的site_package文件夹。类似python中的venv虚拟环境。  
这样的优点是：各项目开发环境独立确保稳定，跟python venv的优点一样。编译后为纯静态文件，丢到nginx下即可部署。
缺点：不像python有公共内置包和成熟各领域常用包。每个项目都要安装，node_modules文件夹下常常三百多个package，网速不好的情况下安装起来比较痛苦。


## (选做)其它后面用到的工具
由于众所周知的原因，谷歌插件需要科学上网，下面几个工具重要但非必须。
1. vue-dev tools, 方便vue项目调试 
2. postman   接口测试工具。可以寻找在线工具或requests包或curl 代替。
3. json-viewer awesome, 谷歌插件。可以在线工具或复制到ide中格式化 代替。





