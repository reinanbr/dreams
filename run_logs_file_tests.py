import glob
import os
import kitano as kt


files_tests = glob.glob('tests/*.py')

for file in files_tests:
    file_name = file.replace('tests/','').replace('.py','')
    file_log = f'tests/logs/{file_name}.log'
    kt.puts(f'running {file} and saving your logs in {file_log}')

    
    os.system(f'python3 {file} > {file_log}')



