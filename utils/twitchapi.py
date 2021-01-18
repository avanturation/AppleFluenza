import datetime
import orjson
from utils.parser import Parser
from config import CLIENT_ID, CLIENT_SECRET
from logger import Logger

class TwitchAPI:
    def __new__(cls):
        cls.logger = Logger.customLogger("TwitchAPI")
        cls.parser = Parser()
        return super().__new__(cls)
 
    @classmethod
    async def getToken (cls, scopes = None):
        if scopes:
            scopes = f"&scope={scopes}"
        else:
            scopes = ""
        data = await cls.parser.post (
            f'https://id.twitch.tv/oauth2/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type=client_credentials{scopes}'
        )
        data = orjson.loads(data)
        token = data['access_token']
        cls.logger.info (f"Token made on {datetime.datetime.now()}. More Information : {data}")
        return token

    @classmethod
    async def users (cls, id):
        token = await cls.getToken()
        headers = {
            'Authorization': f'Bearer {token}',
            'Client-ID': f'{CLIENT_ID}'
        }
        cls.logger.info (f"Helix user requests reported. ID : {id}")
        response = await cls.parser.request (url=f"https://api.twitch.tv/helix/users?login={id}", header=headers)
        return response

    @classmethod
    async def getID (cls, id):
        data = await cls.users (id)
        data = orjson.loads(data)
        id = data["data"][0]["id"]
        return id

    @classmethod
    async def streams (cls, id):
        token = await cls.getToken()
        headers = {
            'Authorization': f'Bearer {token}',
            'Client-ID': f'{CLIENT_ID}'
        }
        cls.logger.info (f"Helix streams request reported. ID : {id}")
        response = await cls.parser.request (url = f"https://api.twitch.tv/helix/streams?user_login={id}", header=headers)
        return response

    @classmethod
    async def checking (cls, id):
        response = await cls.streams(id)
        response = orjson.loads(response)
        if len(response["data"]) > 0:
            return True
        else:
            return False

    @classmethod
    async def getGame (cls, id):
        token = await cls.getToken()
        headers = {
            'Authorization': f'Bearer {token}',
            'Client-ID': 'j25n97ram758w1uovowgj6zavmi3r5'
        }
        cls.logger.info (f"Helix game (find by id) request reported. ID : {id}")
        response = await cls.parser.request (url = f"https://api.twitch.tv/helix/games?id={id}", header=headers)
        return response

    @classmethod
    async def getGamebyName (cls, id):
        token = await cls.getToken()
        headers = {
            'Authorization': f'Bearer {token}',
            'Client-ID': 'j25n97ram758w1uovowgj6zavmi3r5'
        }
        cls.logger.info (f"Helix game (find by name) request reported. NAME : {id}")
        response = await cls.parser.request (url = f"https://api.twitch.tv/helix/games?name={id}", header=headers)
        return response