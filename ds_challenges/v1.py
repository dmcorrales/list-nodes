def findElementWithHightestFrequency(list_elements):
    list_repeated = {}
    for element in list_elements:
        actual_element = list_repeated.get(element)
        if actual_element:
            list_repeated[element] = actual_element + 1
        else:
            list_repeated[element] = 1

    sorted_list = dict(sorted(list_repeated.items(), key=lambda x: x[1]))
    return list(sorted_list.keys())[len(sorted_list.keys()) - 1]

if __name__ == '__main__':
    list_elements = [1, 2, 2, 3, 4, 4 ,4 ,4 ,4,5 , 5, 5,5,5,5,5]
    print(findElementWithHightestFrequency(list_elements))