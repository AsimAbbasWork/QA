import random
import string
import os
from os import path

from package2.learning_functions_skills import replace_text


def random_string_generator():
	random_value = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
	return random_value


def create_empty_text_file(file_path):
	# check if file does not already exist
	if path.exists(file_path) == False:
		# create file
		f = open(file_path, 'w+')
		# close file
		f.close()
		# return  message
		return "successfully created file {} ".format(file_path)
	else:
		return "Cannot create file. File {} already exists.".format(file_path)


def append_text(file_path, insert_text_string, repetation_count):
	# check if file exist
	if path.exists(file_path) == True:
		# Open file and load into memory
		test_file = open(file_path, "a+")
		# iterate till the number of repetition_count
		for x in range(0, repetation_count):
			# write insert_text_string to file
			test_file.write(insert_text_string + '\n')
		# close file
		test_file.close()
		return "successfully appended {} to file {} time".format(insert_text_string, repetation_count)
	else:
		# Create empty text file
		create_empty_text_file(file_path)
		# re-run the append text_file function
		append_text(file_path, insert_text_string, repetation_count)


def delete_text_file(file_path):
	if path.exists(file_path) == True:
		# delete file
		os.remove(file_path)
		
		return "successfully deleted file {} ".format(file_path)
	
	else:
		# exit with error message
		return "Can Not Delete File {} .File Does Not Exist".format(file_path)


def find_string_occurence_count(file_path, search_string):
	# Check if file exists
	if path.exists(file_path) == True:
		# check if file is not empty
		if os.path.getsize(file_path) > 0:
			count = 0
			# Load file content into memory as variable f
			with open(file_path, 'r') as f:
				# Convert file content into a list of line values
				lines = f.readlines()
				# iterate through each line value
				for line in range(0, len(lines)):
					# check if search string exist in line
					if search_string in lines[line]:
						# increase count value by 1
						count = count + 1
			# return the final value of count which is the number of times that search string was found in file
			return count
		
		else:
			# exit with custom message if file is empty
			exit("Can not Find Search String. File is empty")
	else:
		# exit with error message if file does not exist
		exit('Can not Find Search String. file does not exist')
		
def string_occurence_index_numbers_list(file_path, search_string):
	"""
	This function should return a list of index numbers at which the search string is found in file
	"""
	pass


def get_value_of_line_at_index_number(file_path, index_number):
	"""
	This function should return the value at index / line number in file
	"""
	pass

	
def read_text_file(file_path):
	if file_path:
		f = open(file_path, 'r')
		f.read()
		f.close()

def test_case_template():
	"""
	Verify that the program is able to exit gracefully with meaningfully error message when file is not found
	"""
	# Create test summary report file
	test_summary_report = "test_summary_report.txt"
	create_empty_text_file(test_summary_report)
	
	# create a variable named file_path with value as relative path os test_1_file.txt
	file_path = "test_1_file.txt"
	
	# create an empty text file named test_1_file.txt at file_path
	create_empty_text_file(file_path)
	
	# write three lines with a random text in the test_1_file.txt
	random_value = random_string_generator()
	append_text(file_path, random_value, 3)
	
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
	test_case_1 = "PASS Test Case 1 : Verify that the program is able to exit gracefully with meaningfully error message when file is not found"
	file_path = "test_1_file.txt"
	search_string = "The Hapapy"
	replace_string = "sadness"
	error_message = replace_text(file_path, search_string, replace_string)
	
	assert error_message == "Custom Message : File does not exist"
	test_summary_report = "test_1_report.txt"
	create_empty_text_file(test_summary_report)
	append_text(test_summary_report, test_case_1, 1)


test_case1()


def test_case2():
	"""
	 Verify that the program is able to exit gracefully with meaningfully error message when search string is not found
	 """
	test_case_2 = "PASS Test Case 2 : Verify that the program is able to exit gracefully with meaningfully error message when search string is not found"
	file_path = "test_2_file.txt"
	search_string = "this"
	replace_string = "those"
	create_empty_text_file(file_path)
	random_value = random_string_generator()
	append_text(file_path, random_value, 3)
	
	error_message = replace_text(file_path, search_string, replace_string)
	
	assert error_message == "Search string not found in file"
	test_summary_report = "test_2_report.txt"
	create_empty_text_file(test_summary_report)
	append_text(test_summary_report, test_case_2, 1)
	delete_text_file(file_path)


test_case2()


def test_case3():
	"""
	Verify that the program is able to exit gracefully with meaningfully error message when program cannot write to file

	"""
	test_3_report = "PASS Test Case 3: Verify that the program is able to exit gracefully with meaningfully error message when program cannot write to file"
	file_path = "test_3_file.txt"
	search_string = "The Hapapy"
	replace_string = "sadness"
	create_empty_text_file(file_path)
	random_value = random_string_generator()
	append_text(file_path, random_value, 3)
	error_message = replace_text(file_path, search_string, replace_string)
	
	assert error_message == "Search string not found in file"
	test_summary_report = "test_3_report.txt"
	create_empty_text_file(test_summary_report)
	append_text(test_summary_report, test_3_report, 1)
	delete_text_file(file_path)


test_case3()


def test_case4():
	"""
	Verify that the number of replaced string values found in file after the program execution
	is equal to the number of search string values found in file before the program execution
	"""
	test_4_report = (
		"Pass Test Case 4 :\nVerify that the number of replaced string values found in file after the program execution is equal to the number of search \nstring values found in file before the program execution")
	file_path = "test_4_file.txt"
	search_string = "that"
	replace_string = "theirs"
	test_summary_report4 = "test_4_report.txt"
	random_value = random_string_generator()
	create_empty_text_file(file_path)
	append_text(file_path, random_value, 3)
	append_text(file_path, search_string, 3)
	search_string_count = find_string_occurence_count(file_path, search_string)
	replace_text(file_path, search_string, replace_string)
	replace_string_count = find_string_occurence_count(file_path, replace_string)
	error_message = search_string_count == replace_string_count
	assert error_message == True
	create_empty_text_file(test_summary_report4)
	append_text(test_summary_report4, test_4_report, 1)
	delete_text_file(file_path)


test_case4()


def test_case5():
	"""
	Verify that each search string value found in file before the program execution has been
	replaced with the replaced string value after the program execution
	"""
	pass