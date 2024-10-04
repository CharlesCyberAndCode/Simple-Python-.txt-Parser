### Simple file parsing tool

## Function for parsing
def filerParser(path):
    txt = {}
    ## Opening file at the given path
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            ## Key Value
            a , b = line.split('=', 1)
            ## Setting up for dictionary use
            txt[a.strip()] = b.strip()
    return txt


if __name__ == "__main__":
    ## r to allow Windows paths, \ is not to escape python, it is a literal
    #path = r'your file path here'
    text = filerParser(path)
    print(text)
    ## Output should be in a format of 'key' : 'value'.
    ## This parserwill be for my own personal use for parsing config files, therefore ->
    ## this uses = to seperate