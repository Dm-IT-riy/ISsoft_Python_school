file_names = input('Enter file names separated by a space: ').split()
#Example: task.1.py Task.2.doc quest3.txt Ask4.py


def sort(names):
    names.sort()
    names.sort(key = lambda x: x[x.rfind('.'):])
    return names

def print_names(sort_names):
    for name in sort_names:
        print(name)

print_names(sort(file_names))