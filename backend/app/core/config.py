# Configuration settings for the application

import os 
from dotenv import load_dotenv 

load_dotenv()

class _Settings: 
    '''
    This inner class contains the actual configuration settings. 
    It is not meant to be instantiated directly.
    '''
    DATABASE_URL = os.getenv("DATABASE_URL")
    # SECRET_KEY = os.getenv("SECRET_KEY")
    # ALGORITHM = os.getenv("ALGORITHM")
    # ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

class Settings: 
    '''
    This outer class ensures that only one instance of _Settings is created. 
    The __new__ method checks if an instance already exists and, if not, creates one.
    '''
    _instance = None

    def __new__(cls):
        if cls._instance is None: 
            cls._instance = _Settings()
        return cls._instance
    
settings = Settings() # create single instance of the Settings Class - singleton pattern

'''
https://medium.com/10-minutes-qa-story/is-singleton-really-antipattern-in-test-automation-35e3b21b1f0c#:~:text=Singleton%20object%20is%20pretty%20hard,will%20conflict%20with%20each%20other.
싱글톤 패턴을 사용하면 테스트하기가 어렵다고 하는 이야기들이 보인다. 
시간이 되면 읽어보도록 하자! 
역시 완벽한 패턴은 어디에도 없는 것인가..!
'''