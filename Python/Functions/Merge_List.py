# Function to merge two lists
def merge_lists(list1, list2):
    merged_list = list1 + list2
    return merged_list

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = merge_lists(list1, list2)
print(f"The merged list is: {merged}")
