
### 查看服务
tasklist /FI "IMAGENAME eq mongod.exe"

### 启动服务
mongod --config "C:\Program Files\Mongodb\Server\4.0.4\mongod.conf"

### 注册到windows服务中
mongod --install --config "C:\Program Files\Mongodb\Server\4.0.4\mongod.conf"

重新开启一个命令行窗口 输入 mongo 连接服务

mongod --dbpath "C:\Program Files\Mongodb\Server\4.0.4\data" 
--logpath "C:\Program Files\Mongodb\Server\4.0.4\log\mongodb.log" --logappend)
### 连接服务

