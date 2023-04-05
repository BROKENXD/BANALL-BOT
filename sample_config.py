import os

class Config:

    BOT_TOKEN=os.environ['6139871154:AAFnYgWu80lHB_JhwU8I_-frvNL5nH0fQWM']

    API_HASH=os.environ['d0c75e0e8ae1f79ddad10a033411f9ed']

    API_ID=int(os.environ['21124451'])

    

    if not BOT_TOKEN:

        raise ValueError('BOT TOKEN not set')

    

    if not API_HASH:

        raise ValueError("API_HASH not set")

    if not API_ID:

        raise ValueError("API_ID not set")
