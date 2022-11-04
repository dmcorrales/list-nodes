def changeValues(list_elements:list) -> list:
    if len(list_elements) < 2:
        return list_elements
    else:
        first_element = list_elements[0]
        last_element = list_elements[len(list_elements) - 1]
        list_elements[0] = last_element
        list_elements[len(list_elements) - 1] = first_element
        return list_elements

def filterValues(input: str) -> str:
    """
    input = hola
    filtering_values = [a,e,i,o,u]
    output = hl
    """
    filtering_values = ["a","e","i", "o", "u"]
    str_output = ""
    str_output = str_output.join(list(filter(lambda x: x not in filtering_values, input)))
    return str_output

if __name__ == '__main__':
    list_elements = [1,2,3,4,5]

    """
    list= 1,2,3,4,5
    
    first_element = list[0]
    last_element = list[len(list) - 1]
    
    list[0] = last_element
    list[len(list) - 1] = first_element
    output = 5,2,3,4,1
    """

    print(filterValues("hola"))