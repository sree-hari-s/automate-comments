import requests
import config
# Your GitHub repository information
repo_owner = "sree-hari-s"
repo_name = "automate-comments"
access_token = config.GITHUB_ACCESS_TOKEN 

# Comment content
comment = "Hello! This is a comment from your GitHub Action."

# Create a comment on a new issue or PR
def create_comment(issue_number):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}/comments"
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {
        "body": comment
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Comment posted successfully.")
    else:
        print(f"Failed to post comment. Status code: {response.status_code}")

if __name__ == "__main__":
    import sys
    issue_number = sys.argv[1]
    create_comment(issue_number)
