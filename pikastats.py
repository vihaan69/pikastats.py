import requests


username = "your username"

class pikastats:
    @staticmethod
    def friendlist(username:str):
        try:
            response = requests.get(f"https://stats.pika-network.net/api/profile/{username}")
            data = response.json()
            friends = data['friends']
            friend_usernames = [friend['username'] for friend in friends]
            return friend_usernames
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def guild_name(username:str):
        try:
            response = requests.get(f"https://stats.pika-network.net/api/profile/{username}")
            data = response.json()
            if 'clan' in data and isinstance(data['clan'], dict):
                return data['clan'].get('name')
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def guild_owner(username:str):
        try:
            response = requests.get(f"https://stats.pika-network.net/api/profile/{username}")
            data = response.json()
            if 'clan' in data and isinstance(data['clan'], dict):
                return data['clan']['owner']['username']
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def guild_tag(username:str):
        try:
            response = requests.get(f"https://stats.pika-network.net/api/profile/{username}")
            data = response.json()
            if 'clan' in data and isinstance(data['clan'], dict):
                return data['clan'].get('tag')
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def last_seen(username: str):
        try:
            response = requests.get(f"https://stats.pika-network.net/api/profile/{username}")
            data = response.json()
            return data['lastSeen']
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def ranks(username: str):
        try:
            response = requests.get(f"https://stats.pika-network.net/api/profile/{username}")
            data = response.json()
            if 'ranks' in data:
                for rank in data['ranks']:
                    if rank.get('name') == 'games1':
                        return rank.get('displayName')
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

# Example usage:
# print(f"Last seen: {pikastats.last_seen(username)}")
# print(f"Rank: {pikastats.ranks(username)}")
# print(f"Guild name: {pikastats.guild_name(username)}")
# print(f"Guild tag: {pikastats.guild_tag(username)}")
# print(f"Guild owner: {pikastats.guild_owner(username)}")
# print(f"Friend list: {pikastats.friendlist(username)}")
