#学习成绩

# 用户输入
passed = ''
rank = ''
score = input('输入学生成绩：')
score = float(score)
if score < 60:
    passed = '不及格'
else:
    passed = '及格'
    if 60 <= score < 70:
        rank = 'D'
    elif 70 <= score < 80:
        rank = 'C'
    elif 80 <= score < 90:
        rank = 'B'
    elif 90 <= score <100:
        rank = 'A'
print(passed)
print(rank)

