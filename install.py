from os import name, system
print('Installing depenedencies')
if name == 'nt':
     _ = system('pip install art ')
else:
     _ = system('pip3 install art')
print('Done! Your good to run')
