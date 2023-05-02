# 1 处理文件 打开文件
# with open('pi_digits.txt') as file_object:
#     name = file_object.read()
# print(name.rstrip())
2 # 逐行读取
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

3 # 创建一个包含文件各行的列表
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

4 # 使用文件中的内容---将所有的内容添加到一个字符串中
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

Pi_String = ''
for line in lines:
    Pi_String += line.strip()

print(Pi_String)
print(len(Pi_String))

# 输入您的生日，判断一下前100万位pi会不会有您的生日
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

Pi_String = ''
for line in lines:
    Pi_String += line.strip()

birthday = input("输入您的生日：")
if birthday in Pi_String:
    print("111")
else:
    print("000")



