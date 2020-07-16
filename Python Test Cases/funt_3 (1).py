import random
import string
import os



from learning_functions_skills import replace_text

def random_string_generator():
    random_value = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    return random_value

def append_text(file_path,insert_text_string,repetation_count):



    test_file = open(file_path, "a+")
    for x in range(0, repetation_count):
        test_file.write(insert_text_string + '\n')
    test_file.close()


def create_empty_text_file(file_path):
    """
    This function should create an empty text file at given path

    """

    f = open(file_path, 'w+')
    f.close()


def delete_text_file(file_path):
    """
    This function should delete the file at given path

    """
    if os.path.getsize(file_path) > 0:

        os.remove(file_path)
    else:
        exit("Can Not Delete File.File Path Does Not Exist")

def find_string_occurence_count(file_path,search_string):
        """
        This function should return the number of times that the given string exits in the file at
        given path

        """
        if os.path.getsize(file_path) > 0:

            count = 0
            with open(file_path, 'r') as f:
                lines = f.readlines()

                for line in range(0, len(lines)):

                    if search_string in lines[line]:
                        count = count+1

            return count
        else:
            exit("Can not Find Search String.File Path Does Not Exist")


# replace_text("test_file3","first_name = ''","first_name = 'This line needs to be changed'")

def test_case_template():
    """
    Verify that the program is able to exit gracefully with meaningfull error message when file is not found
    """

    # create a variable named file_path with value as relative path os test_1_file.txt
    file_path = "test_1_file.txt"

    # delete files if exists
    # delete_text_file(file_path)

    # create an empty text file named test_1_file.txt at file_path
    create_empty_text_file(file_path)



    # write three lines with a random text in the test_1_file.txt
    random_value = random_string_generator()
    append_text(file_path,random_value,3)

    # create a variable named search_string with known value
    search_string = "The is the String"
    # append the value of search string variable

    append_text(file_path,search_string,1)

    # write three lines with a random text in the test_1_file.txt
    test_file1 = open(file_path,'a')
    random_value = random_string_generator()
    append_text(file_path,random_value,3)

    # append the value of search string variable
    append_text(file_path,search_string,1)
    # write three lines with a random text in the testt_1_file.txt
    test_file3 = open(file_path,"a")
    random_value = random_string_generator()

    append_text(file_path, random_value, 3)

    # append the value of search string variable
    append_text(file_path,search_string,1)

    # write three lines with a random text in the testt_1_file.txt
    test_file5 = open(file_path, "a")
    random_value = random_string_generator()

    append_text(file_path,random_value,3)


    #Create a variable named replace string with known value
    replace_string = "This value need to be changed"

    # Get Search String Occurance Count
    search_string_occurence_count = find_string_occurence_count(file_path, search_string)

    # Execute the program_test with test data
    replace_text(file_path, search_string, replace_string)

    # Get Replace String Occurence Count
    replace_string_occurence_count = find_string_occurence_count(file_path, replace_string)



    # Create test execution report
    print(find_string_occurence_count(file_path, replace_string))
    test_summary_report = "test_summary_report.txt"
    create_empty_text_file(test_summary_report)
    append_text(test_summary_report,"Search String Occurence Count : {} ".format(str(search_string_occurence_count)), 1)
    append_text(test_summary_report,"Replace String Occurence Count : {}".format(str(replace_string_occurence_count)), 1)

    # verify that search string occurence count is equal replace string occurence count
    try:
        assert search_string_occurence_count != replace_string_occurence_count
    except Exception as e:
        append_text(test_summary_report,"search_string_occurence_count != replace_string_occurence_count",1)
    # Archives or delete test artifacts
    delete_text_file(file_path)








def test_case1():
    """
    Verify that the program is able to exit gracefully with meaningfull error message when file is not found
    """

    # create a variable named file_path with value as relative path os test_1_file.txt
    file_path = "test_1_file.txt"

    # delete files if exists
    # delete_text_file(file_path)

    # create an empty text file named test_1_file.txt at file_path
    create_empty_text_file(file_path)



    # write three lines with a random text in the test_1_file.txt
    random_value = random_string_generator()
    append_text(file_path,random_value,3)

    # create a variable named search_string with known value
    search_string = "The is the String"
    # append the value of search string variable

    append_text(file_path,search_string,1)

    # write three lines with a random text in the test_1_file.txt
    test_file1 = open(file_path,'a')
    random_value = random_string_generator()
    append_text(file_path,random_value,3)

    # append the value of search string variable
    append_text(file_path,search_string,1)
    # write three lines with a random text in the testt_1_file.txt
    test_file3 = open(file_path,"a")
    random_value = random_string_generator()

    append_text(file_path, random_value, 3)

    # append the value of search string variable
    append_text(file_path,search_string,1)

    # write three lines with a random text in the testt_1_file.txt
    test_file5 = open(file_path, "a")
    random_value = random_string_generator()

    append_text(file_path,random_value,3)


    #Create a variable named replace string with known value
    replace_string = "This value need to be changed"

    # Get Search String Occurance Count
    search_string_occurence_count = find_string_occurence_count(file_path, search_string)

    # Execute the program_test with test data
    replace_text(file_path, search_string, replace_string)

    # Get Replace String Occurence Count
    replace_string_occurence_count = find_string_occurence_count(file_path, replace_string)



    # Create test execution report
    print(find_string_occurence_count(file_path, replace_string))
    test_summary_report = "test_summary_report.txt"
    create_empty_text_file(test_summary_report)
    append_text(test_summary_report,"Search String Occurence Count : {} ".format(str(search_string_occurence_count)), 1)
    append_text(test_summary_report,"Replace String Occurence Count : {}".format(str(replace_string_occurence_count)), 1)

    # verify that search string occurence count is equal replace string occurence count
    try:
        assert search_string_occurence_count != replace_string_occurence_count
    except Exception as e:
        append_text(test_summary_report,"search_string_occurence_count != replace_string_occurence_count",1)
    # Archives or delete test artifacts
    delete_text_file(file_path)




test_case1()




def test_case2():
     """
     Verify that the program is able to exit gracefully with meaningfull error message when search string is not found
     """
     pass





def test_case3():
    """
    Verify that the program is able to exit gracefully with meaningfull error message when program cannot write to file

    """
    pass

def test_case4():
    """
    Verify that the number of replaced string values found in file after the program execution
    is equal to the number of search string values found in file before the program execution
    """
    pass

def test_case5():
    """
    Verify that each search string value found in file before the program execution has been
    replaced with the replaced string value after the program execution
    """
    pass
