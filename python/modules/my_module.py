print("Imported module..")

def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return target


    return -1

test = 'Test string'