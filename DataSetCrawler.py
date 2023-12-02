def input_items(sentence):
    words = sentence.split()
    words_list = []
    for word in words:
        words_list.append(word)
    return words_list

def search_items(list_of_words_lists, query):
    for i in range (0, len(list_of_words_lists)): 
        for j in range (0,len(list_of_words_lists[i])):
            elements = tuple(list_of_words_lists[i])
            if query in list_of_words_lists[i]:
                for element in elements: 
                    print(element, end = " ")
                    break
            else: 
                print("The word you are searching for is not present in the data set")
                break

list_of_words_lists = []

sentence = input("Enter a sentence: ")
while sentence != "END":
    words_list = input_items(sentence)
    list_of_words_lists.append(words_list)

    sentence = input("Enter another sentence (or 'END' to finish): ")

query = input("Enter the query: ")
search_items(list_of_words_lists, query)
