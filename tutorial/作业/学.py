#用户输入
score = input('请输入学生成绩')
score = int (score)
#print(score,type(score))

# 判断成绩
if score< 0 or score > 100:
    print('用户输入不合法')

if 0 <= score < 60:
    print('不及格')
else:
    print('及格')
    if 60 <= score < 70:
        print('D')
    if 70 <= score < 80:
        print('C')
    if 80 <= score < 90:
        print('B')
    if 90 <= score < 100:
        print('A')
