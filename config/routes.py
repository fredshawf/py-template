from flask import Flask
import os
import re


# 1.自动检索和配置src目录下或其子目录下{xxx}_controller.py定义的蓝图路由
controller_path = '%s/src/' % (Flask.app.root)
files = os.walk(controller_path)
for root, dirs, files in files:
    for f in files:
        if re.search(r"_controller.py$", f):
            relative_path = root[len(controller_path):]

            mod_name = ""
            if len(relative_path) > 0:
                mod_name = relative_path.replace("/", ".") + '.' + f[0:-3]
            else:
                mod_name = f[0:-3]

            mod = __import__("src.%s" % (mod_name), globals(), locals(), [f[0:-3]], 0)
            if hasattr(mod, 'blueprint'):
                Flask.app.register_blueprint(mod.blueprint)



# 2.非{xxx}_controller.py命名规则的控制器可在下面自行定义 =======================》
# 例:
# from src.test_ctl.py import TestCtl
# Flask.app.register_blueprint(TestCtl.blueprint)


# 3.还可以定义Flask原生enpisode
# 例：
# @Flask.app.route('/abc', method=['GET'])
# def abc():
#     # 业务逻辑
#
    
    
    
    