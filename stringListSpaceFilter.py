def stringListSpaceFilter(string_list):
    # string_list: List<String> 
    # ret_type: List<String>
    # error_type: AttributeError

    filtered_list = []
    
    for str in string_list:
        try:
            filtered_list.append(str.replace(" ", ""))
        except AttributeError as err:
            raise err
        
    return filtered_list

def test(input):
    try:
        print(stringListSpaceFilter(input))
    except AttributeError as err:
        print(err)
        
def main():
    l1 = ["h o", " tttt", "ga go "]
    l2 = ["h o", 2, " gago"]
    l3 = [["t"], 2]
    l4 = [{}]
    
    test(l1)
    test(l2)
    test(l3)
    test(l4)
    
        
main()