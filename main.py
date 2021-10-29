import os 
print('Welcome to pygit a git push and pull manager (Case Sensitive Inputs)')
token = input('Enter github token: ')
username = input('Enter Username: ')
repo = input('Enter Repo Name: ')
command = str('git remote set-url origin https://' + token + '@github.com'+ username + repo + '.git')
push = str('git push origin HEAD:master')

os.system(command)
os.system(push)
 # TODO
command2 = 'git remote add origin git@github.com:' + username + '/' + repo + '.git'
os.system(command2)

git remote add origin git@github.com:pynvimdev/pygit.git
os.system('git branch -M main')
os.system('git push -u origin main')
