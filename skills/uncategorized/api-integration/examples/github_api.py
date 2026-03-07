# Example: GitHub API integration (reference only)
import requests


def get_user_repos(username: str, token: str) -> list[dict]:
    """Fetch public repositories for a GitHub user."""
    response = requests.get(
        f"https://api.github.com/users/{username}/repos",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
        },
        params={"per_page": 100, "sort": "updated"},
    )
    response.raise_for_status()
    return response.json()


def create_issue(owner: str, repo: str, title: str, body: str, token: str) -> dict:
    """Create an issue in a GitHub repository."""
    response = requests.post(
        f"https://api.github.com/repos/{owner}/{repo}/issues",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
        },
        json={"title": title, "body": body},
    )
    response.raise_for_status()
    return response.json()
