# 预定义变量，包括输入消息
input_message = "hello world !!! * # :_) 这是我们的一个加密解密测试作业"
print ("原文输入是：",input_message)
encyption_result = []
decyption_result = []

# 作业思路是，采用ASCII码，将输入消息迭代进一个加密函数，得到加密后的ASCII码，解密时，将加密后的ASCII码迭代进解密函数，得到对应的消息
for char in input_message:
    ascii=ord(char)
    encyption_result.append(ascii+13)
print (encyption_result)
print ("这是原文加密后的ASCII码：")
print ("|".join(str(i) for i in encyption_result))
# for i in encyption_result:
#     print (i, end=",")

for i in encyption_result:
    ascii=chr(i-13)
    decyption_result.append(ascii)
x = "".join(decyption_result)
print("这是ASCII码解密后的原文：")
print (x)

