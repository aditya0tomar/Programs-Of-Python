def dict_to_list(input_dict):
# Sort the dictionary by keys in alphabetical order    
    sorted_dict=sorted(input_dict.items())
# Convert the sorted dictionary to a list of tuples
    result=[(key,value)for key,value in sorted_dict]
    return result
