import random
# 这是第一版v1.0的‘智能’算数出题工具的源码
# 请遵循MIT开源协议，可以用于商业目的
# 预定义函数
def plus():
    first = random.randint(1,10)
    last = random.randint(1,10)
    print(first , '+' , last)
def sub():
    first = random.randint(1,10)
    last = random.randint(1,10)
    print(first , '-' , last)
def multi():
    first = random.randint(1,10)
    last = random.randint(1,10)
    print(first , '*' , last)
def div():
    first = random.randint(1,10)
    last = random.randint(1,10)
    print(first , '/' , last)
print("""
1. 10以内加算数生成模式
2. 10以内减算数生成模式
3. 10以内乘算数生成模式
4. 10以内除算数生成模式
exit 停止生成
""")
#获得用户模式
mode = int(input('请输入模式数字'))
# 开始操作
while mode == 1:
    plus()
    mode = int(input('按任意键回车停止生成'))
else:
    while mode == 2:
        sub()
        mode = int(input('按任意键回车停止生成'))
    else:
        while mode == 3:
            multi()
            mode = int(input('按任意键回车停止生成'))
        else:
            while mode == 4:
                div()
                mode = int(input('按任意键回车停止生成'))
            else:
                mode == False