immutable_var = (1 , 2 , 'a' , 'b')
print(immutable_var)
# print(immutable_var[0][2]) котеж предназначен для хранения данных в неизменном виде
mutable_list = ([1, 2], 'a', 'b', 'Modified')
print(mutable_list)
mutable_list[0][0] = 6
print(mutable_list)