import re
ime = []
ave = []
sum = 0
vowels = []
vowels1 = []
with open('word.txt','r') as text_f:
    test = text_f.read().split()
    for x in test:
        x_new = re.sub("[ ,.?! ]"," ",x)
        if x_new[-3:len(x_new)] == 'ime':
           ime.append(x_new)
        if x_new[1:4] == 'ave':
            ave.append(x_new)
        if "r" in x_new or "s" in x_new or "t" in x_new or "l" in x_new or "n" in x_new or "e" in x_new:
            sum += 1
        if "r" in x_new or "s" in x_new or "t" in x_new or "l" in x_new or "n" in x_new:
            percentage = ((sum)/len(test))*100
        if not re.findall('[aeiouyAEIOUY]',x):
            vowels.append(x)
        if 'aeiouy' in x:
            vowels1.append(x)

print("1)",ime)
print("2)",ave)
print("3)",sum)  
print("4)",str(int(percentage))+"%")
print("5)",vowels)
print("6)",vowels1)