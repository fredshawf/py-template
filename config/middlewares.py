from flask import Flask
import config.routes # 路由的内部实现既Flask中间件的实现，此处归入中间件逻辑

from lib.benchmark import Benchmark

# 获取flask应用中间件
final_wsgi_app = Flask.app.wsgi_app

# 引入相关中间件，并封装Flask应用 new_wsgi_app = SomeMiddleWare(Flask.app.wsgi_app）
if Flask.app.env == 'development':
    final_wsgi_app = Benchmark(final_wsgi_app)


# 设置最终Flask应用的中间件
Flask.app.wsgi_app = final_wsgi_app

