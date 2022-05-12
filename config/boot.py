import os
import re
from telnetlib import STATUS
from flask import Flask
from configparser import ConfigParser



class Boot:

    
    
    @classmethod
    def start(cls):
        cls.__load_configuration()
        cls.__initialize_script()
        cls.__initialize_app_key()
        cls.__initialize_logger()
        cls.__initialize_middleware_stack()


    @classmethod
    def __load_configuration(cls):
        # 加载环境配置
        configParser = ConfigParser()
        configParser.read("%s/config/environments/global.ini" % Flask.app.root)
        configParser.read("%s/config/environments/%s.ini" % (Flask.app.root, Flask.app.env))
        config = dict(configParser.items("app", 0, os.environ))

        # 设置debug模式
        if config['debug'] == 'True':
            Flask.app.config['DEBUG'] = True
            os.environ['FLASK_DEBUG'] = 'True'
        else:
            Flask.app.config['DEBUG'] = False
            os.environ['FLASK_DEBUG'] = 'False'
        
        Flask.app.config.from_object(config)
        Flask.app.config.update(config)
        
        
    @classmethod
    def __initialize_script(cls):
        files = os.listdir('%s/config/initializers' % (Flask.app.root))
        for f in files:
            if re.search(r"[^_].py$", f):
                __import__("config.initializers.%s" % (f[0:-3]), globals(), locals(), [], 0)


    @classmethod
    def __initialize_app_key(cls):
        Flask.app.secret_key = Flask.app.config['secret_key']
    

    @classmethod
    def __initialize_logger(cls):
        __import__("config.logger", globals(), locals(), [], 0)
    
    
    @classmethod
    def __initialize_middleware_stack(cls):
        __import__("config.middlewares")
    
    
    
    
    
    