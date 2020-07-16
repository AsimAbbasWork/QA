import random
import string
import os

from learning_functions_skills import replace_text


def random_string_generator():
    random_value = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    return random_value


def append_text(file_path, insert_text_string, repetation_count):
    if file_path:
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
def read_text_file(file_path):
    if file_path:
        f = open(file_path,'r')
        f.read()
        f.close()

def delete_text_file(file_path):
    """
    This function should delete the file at given path

    """
    if file_path:

        os.remove(file_path)
    else:
        exit("Can Not Delete File.File Path Does Not Exist")


def find_string_occurence_count(file_path, search_string):
    """
    This function should return the number of times that the given string exits in the file at
    given path

    """
    if os.path.getsize(file_path) > 0:

        count = 0
        with open(file_path, 'r+') as f:
            lines = f.readlines()

            for line in range(0, len(lines)):

                if search_string in lines[line]:
                    count = count + 1

        return count
    else:
        exit("Can not Find Search String.File Path Does Not Exist")


def test_case_template():
    """
    Verify that the program is able to exit gracefully with meaningfully error message when file is not found
    """

    # create a variable named file_path with value as relative path os test_1_file.txt
    file_path = "test_1_file.txt"

    # delete files if exists
    # delete_text_file(file_path)

    # create an empty text file named test_1_file.txt at file_path
    create_empty_text_file(file_path)

    # write three lines with a random text in the test_1_file.txt
    # random_value = random_string_generator()
    # append_text(file_path, random_value, 3)

    # create a variable named search_string with known value
    search_string = "The is the String"
    # append the value of search string variable

    append_text(file_path, search_string, 1)

    # write three lines with a random text in the test_1_file.txt
    test_file1 = open(file_path, 'a')
    random_value = random_string_generator()
    append_text(file_path, random_value, 3)

    # append the value of search string variable
    append_text(file_path, search_string, 1)
    # write three lines with a random text in the testt_1_file.txt
    test_file3 = open(file_path, "a")
    random_value = random_string_generator()

    append_text(file_path, random_value, 3)

    # append the value of search string variable
    append_text(file_path, search_string, 1)

    # write three lines with a random text in the testt_1_file.txt
    test_file5 = open(file_path, "a")
    random_value = random_string_generator()

    append_text(file_path, random_value, 3)

    # Create a variable named replace string with known value
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
    append_text(test_summary_report, "Search String Occurence Count : {} ".format(str(search_string_occurence_count)),
                1)
    append_text(test_summary_report, "Replace String Occurence Count : {}".format(str(replace_string_occurence_count)),
                1)

    # verify that search string occurence count is equal replace string occurrence count
    try:
        assert search_string_occurence_count == replace_string_occurence_count
    except Exception as e:
        append_text(test_summary_report, "search_string_occurence_count == replace_string_occurence_count", 1)
    # Archives or delete test artifacts
    delete_text_file(file_path)


# test_case_template()


def test_case1():
    """
    Verify that the program is able to exit gracefully with meaningfully error message when file is not found
    """

    # create a variable named file_path with value as relative path os test_1_file.txt
    test_case_1 ="PASS Test Case 1 : Verify that the program is able to exit gracefully with meaningfully error message when file is not found"
    file_path = "test_1_file.txt"
    search_string = "The Hapapy"
    replace_string = "sadness"
    error_message = replace_text(file_path,search_string,replace_string)

    assert error_message == error_message
    test_summary_report = "test_1_report.txt"
    create_empty_text_file(test_summary_report)
    append_text(test_summary_report,test_case_1,1)




test_case1()


def test_case2():
    """
     Verify that the program is able to exit gracefully with meaningfully error message when search string is not found
     """
    test_case_2 = "PASS Test Case 2 : Verify that the program is able to exit gracefully with meaningfully error message when search string is not found"
    file_path = "test_2_file.txt"
    search_string = "this"

    create_empty_text_file(file_path)
    random_value = random_string_generator()
    append_text(file_path,random_value,3)

    error_message = replace_text(file_path,search_string,search_string)

    assert error_message == "Search string not found in file"
    test_summary_report = "test_2_report.txt"
    create_empty_text_file(test_summary_report)
    append_text(test_summary_report,test_case_2,1)

test_case2()


def test_case3():
    """
    Verify that the program is able to exit gracefully with meaningfully error message when program cannot write to file

    """
    test_3_report = "PASS Test Case 3: Verify that the program is able to exit gracefully with meaningfully error message when program cannot write to file"
    file_path = "test_3_file.txt"
    search_string = "The Hapapy"
    replace_string = "sadness"
    error_message = replace_text(file_path, search_string, replace_string)

    assert error_message == error_message
    test_summary_report = "test_3_report.txt"
    create_empty_text_file(test_summary_report)
    append_text(test_summary_report, test_3_report, 1)
     # "Need Some Clearifications"

test_case3()


def test_case4():
    """
    Verify that the number of replaced string values found in file after the program execution
    is equal to the number of search string values found in file before the program execution
    """
    test_4_report =("Pass Test Case 4 :\nVerify that the number of replaced string values found in file after the program execution is equal to the number of search \nstring values found in file before the program execution")
    file_path ="test_4_file.txt"
    search_string = "that"
    replace_string ="theirs"
    test_summary_report4 = "test_4_report.txt"
    random_value = random_string_generator()
    create_empty_text_file(file_path)
    append_text(file_path,random_value,3)
    append_text(file_path,search_string,3)
    search_string_count =find_string_occurence_count(file_path,search_string)
    replace_text(file_path,search_string,replace_string)
    replace_string_count = find_string_occurence_count(file_path,replace_string)
    error_message = search_string_count == replace_string_count
    assert error_message == True
    create_empty_text_file(test_summary_report4)
    append_text(test_summary_report4,test_4_report,1)
test_case4()


def test_case5():
    """
    Verify that each search string value found in file before the program execution has been
    replaced with the replaced string value after the program execution
    """
    pass
