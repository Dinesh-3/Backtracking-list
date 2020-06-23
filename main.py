def print_list_elements(array):
    for element in array:
        if type(element) == list:
            print_list_elements(element)
        else:
            print(element)
array = [34,21,[0,
    [1,2,3],
    [4,5,6,7,8,[1,2,3,4]],
    [9,10,11,[100,101,[12,45,9],95],12,13],
    14,
    [15,16],
    17
    ],76]        
        
print_list_elements(array)    
