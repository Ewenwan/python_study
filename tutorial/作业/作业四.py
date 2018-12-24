nterms = int(input("你需要几项？"))

# 第一和第二项
n1 = 0
n2 = 1
count = 2

# 判断输入的值是否合法
if nterms <= 0:
    print("请输入一个正整数。")
elif nterms == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1, ",", n2, end=" , ")
    while count < nterms:
        nth = n1 + n2
        print(nth, end=" , ")
        # 更新值
        n1 = n2
        n2 = nth
        count += 1




 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>作业</title><!--写一个注册表单：用户名、密码、电话、提交按钮-->
</head>
<body>
<form action="http://www.baidu.com">
   <label>用户名字</label> <input type="text" placeholder="请输入用户名" ><br>
    <label>用户密码  </label><input type="password" placeholder="请输入密码"><br>
    <label>用户手机</label> <input type="text" placeholder="请输入用户手机号" ><br>
     <input type="submit" value="提交表单">
</form>
</body>
</html>

