import os 

class Config:
    '''
    General configuration parent class
    '''




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = { #dictionary to help us access different config option classes
'development':DevConfig,
'production':ProdConfig
}