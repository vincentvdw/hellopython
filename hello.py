def add(x, y):
    return x + y

def tail(list):
    tail = []
    for i in range(1, len(list)):
        tail.append(list[i])
    return tail

def print_dictiorary(dict):
    for i in range(len(dict)):
        print(dict.keys()[i] + ": " + str(dict.values()[i] ))

if __name__ == "__main__":

    print("Hello, World!")

    a_list = [1,2,3,4,5]

    print(tail(a_list))

    another_list = ["Hello", "World"]

    print(tail(another_list))

    a_dictionary = { "World": 2, "Hello": 1 }

    print_dictiorary(a_dictionary)

