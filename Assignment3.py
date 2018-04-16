def check_double(list1, list2):
    new_list=[]
    multi_list = [i * 2 for i in list2] #this iterates thru list
    
    #iterate thru all elements of both lists for comparison
    for i in range(0, len(list2)):
      for j in range(0, len(list1)):
        if list1[j] == multi_list[i]:
          new_list.append(list1[j])
    return new_list


list1=[11,8,23,7,25,15, 12]
list2=[6,33,50,31,46,78,16,34, 4]
print(check_double(list1, list2))
