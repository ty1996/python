def binary_search(find, list1) :
  low = 0
  high = len(list1)
  while low <= high :
    mid = (low + high) / 2
    if list1[mid] == find :
      return mid
      elif list1[mid] > find :
      high = mid -1
      else :
      low = mid + 1
        return -1

list1 = [1,2,3,7,8,9,10,5]
list1.sort()

print "原有序列表为:",list1
try :
  find = int(raw_input("请输入要查找的数："))
except :
  print "请输入正整数！"
  exit()

result = binary_search(find, list1)
if result != -1 : 
  print "要找的元素%d的序号为：%d" %(find,result)
else :
  print "未找到！"
