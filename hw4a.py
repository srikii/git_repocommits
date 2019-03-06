"""program to mock the number of repositories in a given username and also the number of commits for each repository
    author: srikanth"""

import urllib
import json
import requests

def git_repocommits(n):
    git_name=n
    git_url= "https://api.github.com/users/{}/repos".format(git_name)
    dataa = requests.get(git_url)   
    
    #uh = urllib.request.urlopen(git_url)
    #data = uh.read().decode()

    data= dataa.text

    try:
        js = json.loads(data)
    except:
        js = None

    l1=list()

    for i in js:
        for key, val in i.items():
            if key == "name":
                l1.append(val)

    l2=list()

    for i in l1:
        repo_url="https://api.github.com/repos/{}/{}/commits".format(git_name, i)
        uh2 = urllib.request.urlopen(repo_url)
        data2 = uh2.read().decode()
        try:
            js2 = json.loads(data2)
        except:
            js2 = None

        commits=len(js2)
        l2.append(commits)

    for i in range(len(l1)):
        print("Repo:", l1[i], "Number of commits: ", l2[i])
    
    return(l1,l2)

def main():

    n=input("enter the GitHub user name: \n")
    g=git_repocommits(n)
    

if __name__ == '__main__':
    main()

