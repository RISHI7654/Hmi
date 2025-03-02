import requests

# Access Token (Facebook Graph API token)
access_token = 'YOUR_ACCESS_TOKEN'

# Post ID (The post ID where you want to comment, react, etc.)
post_id = 'YOUR_POST_ID'

# Function to post a comment
def post_comment(post_id, comment):
    url = f'https://graph.facebook.com/{post_id}/comments'
    data = {'message': comment, 'access_token': access_token}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Comment posted successfully!")
    else:
        print(f"Failed to post comment: {response.text}")

# Function to add a reaction (LIKE, LOVE, WOW, HAHA, SAD, ANGRY)
def add_reaction(post_id, reaction_type):
    url = f'https://graph.facebook.com/{post_id}/reactions'
    data = {'type': reaction_type, 'access_token': access_token}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print(f"Reacted with {reaction_type}!")
    else:
        print(f"Failed to react: {response.text}")

# Function to vote on a poll (replace the poll ID)
def vote_poll(poll_id, option_id):
    url = f'https://graph.facebook.com/{poll_id}/votes'
    data = {'option': option_id, 'access_token': access_token}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print(f"Voted successfully on the poll!")
    else:
        print(f"Failed to vote: {response.text}")

# Function to share a post
def share_post(post_id):
    url = f'https://graph.facebook.com/{post_id}/sharedposts'
    data = {'access_token': access_token}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Post shared successfully!")
    else:
        print(f"Failed to share post: {response.text}")

# Example usage
# Commenting on the post
post_comment(post_id, "This is an automated comment!")

# Reacting with "LOVE"
add_reaction(post_id, "LOVE")

# Voting on a poll (Example: poll_id and option_id should be actual IDs)
vote_poll('POLL_ID', 'OPTION_ID')

# Sharing the post
share_post(post_id)
