'''list1=[12,34,45,52,'Dip']
list2=[True,'Dark_smile','We']
print(list1[1])
print(list1[-3])
print(len(list2))
list3=list1+list2
print(list3)

nest=[
    [12,34,456,3],
    [24,35,67],
    [35,72,13]
]
print(nest)
print(nest[0][1])
for row in nest:
    for i in row:
        print(i, end=" ") 
   
def match_word(words):
    cnt=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            cnt+=1
            lst.append(word)
    return cnt
count=match_word(['aba','oliva','ahon','jannat','alice']) 
print(count)
   
l=[343,345,678,3456,134567,456734,456765432]
sum=0
for i in l:
    sum+=i
avg=sum/len(l)
sor=l.sort()
print("total sum",sum)
print("average",avg)
print("Sorted",sor)
mn=min(l)
mx=max(l)
print("the minimum element ",mn)
print("The largest element",mx)    
  ''' 
nested=[
    ['Virat',[23,57,35,100]],
    ['Rohit',[24.56,3,5]],
    ['Warner',[63,46,83]]
    
]   
for i in nested:
    player=i[0]
    scores=i[1]
    avg=sum(scores)/len(scores)
    print(f" {player}'s average {avg} ")      