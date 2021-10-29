import os 
print('Welcome to pygit a git push and pull manager (Case Sensitive Inputs)')
token = input('Enter github token: ')
username = input('Enter Username: ')
repo = input('Enter Repo Name: ')
command = str('git remote set-url origin https://' + token + '@github.com'+ username + repo + '.git')
push = str('git push origin HEAD:master')

os.system(command)
os.system(push)