#!/usr/bin/env python3
import requests
import sys

def get_user_data(username: str):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f"❌ User '{username}' not found.")
    else:
        print(f"⚠️ Error {response.status_code}: {response.text}")
    return None

def main():
    print("👋 GitFind STARTED")

    if len(sys.argv) < 2:
        print("Usage: python gitfind.py <github_username>")
        sys.exit(1)

    username = sys.argv[1]
    print(f"🔍 Looking up GitHub user: {username}\n")

    data = get_user_data(username)
    if not data:
        return

    print(f"Username: {data['login']}")
    print(f"Name: {data.get('name', 'N/A')}")
    print(f"Public repos: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
    print(f"Following: {data['following']}")
    print(f"Profile: {data['html_url']}")
    print(f"Bio: {data.get('bio', 'N/A')}")

if __name__ == "__main__":
    main()
