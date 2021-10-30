# PyGit
# Author : Hari
import os 
from os import name, system
from art import *

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():
    clear()
    tprint('PyGit')
    print('Welcome to pygit, A git push and pull manager for github(Case Sensitive Inputs)')
    branch = input('Enter the branch to upload: ')
    username = input('Enter Username: ')
    repo = input('Enter Repo Name: ')
    token = input('Enter github token: ')
    command = str('git remote set-url origin https://' + token + '@github.com' + '/'+ username + '/' + repo + '.git')
    command2 = 'git remote add origin git@github.com:' + username + '/' + repo + '.git'
    push = str(f'git push origin HEAD:{branch}')
    os.system(command)
    os.system(push)
    os.system(command2)

if __name__ == "__main__":
    main()
