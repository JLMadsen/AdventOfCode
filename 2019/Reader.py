def readIntcode(filename) -> []:
    
    input_file = open(filename)
    text = input_file.read()
    input_file.close()
    
    delimiter = ','
    array = text.split(delimiter)
    int_array = list( map(int, array))
    
    return int_array