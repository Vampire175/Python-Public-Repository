import requests

# Replace these with your own values
GITHUB_USERNAME = 'your-username'
TOKEN = 'your-personal-access-token'

# List of repositories to delete
repos_to_delete = [
    "repo1",
    "repo2",
    "repo3"
]

headers = {
    "Authorization": f"token {TOKEN}"
}

for repo in repos_to_delete:
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Deleted: {repo}")
    else:
        print(f"Failed to delete {repo}: {response.status_code} {response.text}")
