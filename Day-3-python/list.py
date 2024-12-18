# using list data type you represent stack and queue
# index start with zero and from backward -1
mylist = ["prashant", 'Ashish', 'komal', 'ankush', 'Ashish', 77, 'sandip', 60.52, 'prashant']

print(mylist)
print(type(mylist))
######### print(mylist[index_no.]) ##########################################
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])

####### print(mylist[staring index : end index : gap between]) #######################
print(mylist[1:])
print(mylist[1:8:2])

########### updating index or chaning index #########################################
mylist[0]='Ayush'
print(mylist)

########### appending at the end of document ############################
mylist.append('harsh')
mylist.append(82)
print(mylist)

########## inserting object in list    mylist.insert(index no, 'object') ####################################3
mylist.insert(2,'sanket') 
print(mylist)


########################## remove object from list ############################
##### if duplicate of object present in list mylist.remove func remove first dublicate ###############
mylist.remove('sandip')
print(mylist)

############ clone/coping list ############################
newlist = mylist.copy()
print(mylist)


############ Multidimensional List #############

#[       [0]       [1]]
#[0]   prashant    jha
#[1]   85.56
#[2]  440022       yyy

mylist= [['prashant', 'jha'], ['85.56'], [440022, 'yyy'] ]

print('example of mulidimensional list')
print(mylist)
############ print(mylist[row][col])
print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[2][0])
print(mylist[2][1])



################# some basic of list #################
# Multiplying list
list1=['prashant', 'jha']  #output : ['prashant', 'jha', 'prashant', 'jha']
print(list1*2)
# Adding list
list2 =[50,25.50]
print(list1+list2)         #output : ['prashant', 'jha', 50, 25.5]
# deleting object from list
list2 = [50,25.50,'prashant']
del list2[2]
# deleting entire list
# del list2[2] #deleting index 2 
del list2    #deleting entire list
#print(list2) 

# clear the oject inside list 
list2 =[50, 25.50, 'prashant']
list.clear(list2)  # gonna clear list 
print(list2)

name ='prashant' #['p','r', 'a']
print(name)


# reverse list
mylist = [40,30,20,10]
mylist.reverse()
print(mylist)

############### sorting list ##################################
# default sorting order for number is ascending order
# default sorting order for string is alphabetical order
# we should know that list should contain homogenious data otherwise we will get typeerror
# python2 first short number then string follow

#example
mylist = [44,22,77,0,9,88]
mylist.sort()
print(mylist)
# mylist.sort().reverse()
# print(mylist)


############# (lista mutability concept) Alising
#alising means assigining one variable reference to another variable
mylist=[44,22,77,0,9,88]
newlist= mylist
print(id(mylist))
print(id(newlist))


################ for loop in list ################
mylist=[44,22,77,0,9,88]
for i in mylist:
    print(i)




########### conditional in list ################
container =[2,1,4,5,5,4,4,1,1]
count =0
even =0
odd =0
for i in container:
    if i==4:
        count += 1
    elif i==2:
        even += 1
    elif i == 5:
        odd +=1
print(count-even)
print(count-odd)
print(count-count)


#question : find the majority element:
#question : find the majority element(element that appers n/2 times ) in an array
#logic : use moore's voting algorithm
#sample input : [3,3,4,2,4,4,2,4,4]

# maj_list = [3,3,4,2,4,4,2,4,4]
# four =0
# three =0
# two =0
# for i in maj_list:
#     if i == 4:
#         four +=1
#     elif i == 3:
#         three +=1
#     elif i == 2:
#         two +=1
# print(count-four)
# print(count-three)
# print(count-four)


########### max & min ########################################
data = [2,1,4,5,5,4,4,1,1]  #data_len = 9
max = min = data[0]   
for i in range(len(data)): #i=1<9
    if data[i]> max:
        max = data[i]
    if data[i] < min:
        min = data[i]
    
print('max value in this list is ', max) #output : 5
print('min value in this list is ', min) #output : 1



#question

mylist =[0,1,0,3,12]
N = len(mylist)
print(N)
for i in range(N):
    if mylist[4] == 0:
        mylist.remove(0)
        mylist.append(0)

print(mylist)


#question
# find the Kth largest element
mylist = [3,2,1,5,6,4]
k = data[0]




#question
# find the Kth largest element whitout sort funcion
...

# question : for loop with conditional 

mycart=[10,20,200,300,800,60,700]
for i in mycart:
    if i>400:
        print("this item not in budget")
        continue
    print(i)
else:
    print('you is on budget')


#question : 
rollno =[3,5,7,1,11,4,5,2]
for x in rollno:
    if x == 2 or x == 4 or x ==6 or x ==8 or x == 10:
        print("which even no is found ", x)
        break

#question find the common element in two list
list1 = [1,2,3,4]
list2 = [3,4,5,6]
common = []
for i in list1:
    if i in list2:
        common.append(i)
        print(common)
     
    

#question find the first no repeating element
list = [1,2,3,2,1,4,99]
for i in list:
    if list.count(i) == 1:
        print(i)
        break

#question photo from mobile # ooutput : 3 (key sum)
data = [5,7,8,3,7,8,9,2,3]
reapeting_value = 0
for i in list:
    if list.count(i) > 1:
        reapeting_value += 1
print('key is ',reapeting_value)

#question count positive and negative in list
list = [3, -2, 7, -1,0 ,5, -4]
post = 0
neg =0
for i in list:
    if i>=0:
        post+=1
    else:
        neg+=1
print('postive is ',post)
print('negative is ',neg)




#find the maximum number of consecutive(continues) 1's in a binary array
# mylist = [1,1,0,1,1,1,0,1,1,1,1]
# consec_count=[]
# count = 0
# for i in mylist:
#     if i== 1:
#          count+= 1
#     else :
#         consec_count.append(count)
#         count =0
# else:
#     consec_count.append(count)
# print(consec_count)