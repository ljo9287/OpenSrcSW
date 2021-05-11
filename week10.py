#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = input().split(' ')
num = list(map(int, a))
print(max(num))


# In[ ]:


str = input().split()
str.reverse()

str_chr = ""
str_c = ""
str_ord = ""
str_o = ""
char = ''
space = " "
code = 0

for i in range(len(str)):
    for j in range(len(list(str[i]))):    
        char = str[i][j]
        code = ord(char)+1
        char = chr(code)
        str_ord += char

str_o = str_ord[0:len(list(str[0]))] + space + str_ord[len(list(str[0])):] 
print(str_o)

for i in range(len(str_ord)):
    for j in range(len(list(str_ord[i]))):    
        char = str_ord[i][j]
        code = ord(char)-1
        char = chr(code)
        str_chr += char


str_c = str_chr[0:len(list(str[0]))] + space + str_chr[len(list(str[0])):] 
print(str_c)


# In[ ]:



members = {}
num = 0

while num < 10:
    menu = input('회원정보 추가(a), 검색(b)')
    if menu=='a':
        name = input('이름: ')
        phone = int(input('전화번호: '))
        members[name] = phone
        print('----------')
        print('{0:s} 입력 완료'.format(name))
        print('{0:s}: {1:d}'.format(name, phone))
        #print(f'{name}:', phone)
        print('----------')
        num = num + 1

    elif menu=='b':
        name = input('이름: ')
        phone = members.get(name)
        
        if name not in members:
            print('전화번호부 목록에 존재하지 않습니다.') 
        
        else:
            print('----------')
            print('{0:s}: {1:d}'.format(name, phone))
            print('----------')


# In[ ]:




