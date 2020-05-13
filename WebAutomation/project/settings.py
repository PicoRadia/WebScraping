import os

file = os.path.abspath(".")
'''
please pay attention to the following things :
    The path  mot be in quotes "" 
    The path must end in \\
'''

'''Here you will write the absolute path to the automation file .This file needs to have 
the chromedriver .
'''
absolute_path_to_automation_file= file

''' 
specify the absolute_path_to_data_entries . 
By default this file is contained in the automation file hence : 
absolute_path_to_data_entries + 'data entries/'
You can change it by specifying the absolute path to the folder .
 '''
absolute_path_to_data_entries = absolute_path_to_automation_file+ '\\data entries\\'

''' 
specify the absolute_path_to_data_results . 
By default this file is contained in the automation file hence : 
absolute_path_to_data_entries + 'data results/'
You can change it by specifying the absolute path to the folder .
 '''

absolute_path_to_data_results= absolute_path_to_automation_file + '\\data results\\'
