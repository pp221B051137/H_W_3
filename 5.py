import re
e = []
with open('5_text.txt','r') as text:
    srt = text.read().split("\n")
    for x in srt:
        srt_l = x.split()
        pochty = srt_l[1]
        pochty_1 = pochty[1:len(pochty)-1]
        qwe = pochty_1.split("@")
        
        if not re.findall("[,!:?/\-+=#]",qwe[1]) and re.findall("^[a-z]",qwe[0]):
                qwe.remove(qwe[0])
                print(x)
                e.append(x)
with open('5_new.txt','w') as wqe:
    for ew in e:
        wqe.write(ew)
                # q = wqe.write(x)
                # w = open('5_new.txt','w')
                # w.write(x)
            
    # print(type(srt_l))