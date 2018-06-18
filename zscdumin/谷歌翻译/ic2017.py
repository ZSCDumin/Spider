linklist=[]
str='https://aaai.org/ocs/index.php/ICAPS/ICAPS17/paper/view/'
f = open('C:\Users\Administrator\Desktop\ICAPS.txt', 'r') #此处保存上述网页的源代码，用于下一步的字符串检索
line = f.readline()             # 调用文件的 readline()方法
endpos=67
while line:
    i = line.find(str)
    if i > -1:
        #print line[i:i+endpos]
        if line[i:i+endpos].find('>') == -1:
            print line[i:i+endpos]
            linklist.append(line[i:i+endpos])
    line = f.readline()
print linklist
f.close()

#2017
#https://aaai.org/ocs/index.php/ICAPS/ICAPS17/paper/view/
#https://aaai.org/ocs/index.php/ICAPS/ICAPS17/paper/view/15724
#https://aaai.org/ocs/index.php/ICAPS/ICAPS17/paper/view/15724/15148

#2016
#http://www.aaai.org/ocs/index.php/ICAPS/ICAPS16/paper/view/
#http://www.aaai.org/ocs/index.php/ICAPS/ICAPS16/paper/view/13146
#http://www.aaai.org/ocs/index.php/ICAPS/ICAPS16/paper/view/13146/12718
