
def swapData ():
    essay_file_path = input("Enter path of the file to edit in ")
    other_file_path = input("Enter path of the file to get data from ")

    # method 1
    # essay_file = open(essay_file_path)
    # other_file = open(other_file_path)

    # essay_file_data = essay_file.read()
    # other_file_data = other_file.read()

    # essay_file_write = open(essay_file_path, "w")
    # other_file_write = open(other_file_path, "w")

    # essay_file_write.write(other_file_data)
    # other_file_write.write(essay_file_data)


    # method 2
    with open(essay_file_path) as essay_file:
        essay_file_data = essay_file.read()

    with open(other_file_path) as other_file:
        other_file_data = other_file.read()
    
    with open(essay_file_path, 'w') as essay_file:
        essay_file.write(other_file_data)
    
    with open(other_file_path, 'w') as other_file:
        other_file.write(essay_file_data)
        

swapData()