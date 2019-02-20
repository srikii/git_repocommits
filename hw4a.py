import urllib.request
import urllib.parse
import urllib.error
import json
import requests
import ssl


def git_repocommits(n):
    git_name=n
    git_url= f"https://api.github.com/users/{git_name}/repos"
    uh = urllib.request.urlopen(git_url)
    data = uh.read().decode()

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
        repo_url=f"https://api.github.com/repos/{git_name}/{i}/commits"
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
    #print(g)


if __name__ == '__main__':
    #unittest.main(exit=False, verbosity=2)
    main()

