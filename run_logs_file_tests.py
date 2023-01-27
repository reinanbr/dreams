import glob
import os
import kitano as kt


files_test_embed = glob.glob('tests/test_get_video_embed/*.py')

for file in files_test_embed:
    file_name = file.replace('tests/test_get_video_embed/','').replace('.py','')
    file_log = f'tests/test_get_video_embed/logs/{file_name}.log'
    kt.puts(f'[running embed]: {file} and saving your logs in {file_log}')

    os.system(f'python3 {file} > {file_log}')
    


files_test_search = glob.glob('tests/test_search_porn/*.py')

for file in files_test_search:
    file_name = file.replace('tests/test_search_porn/','').replace('.py','')
    file_log = f'tests/test_search_porn/logs/{file_name}.log'
    kt.puts(f'[running search]: {file} and saving your logs in {file_log}')

    
    os.system(f'python3 {file} > {file_log}')



