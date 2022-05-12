import datetime
from flask import Flask, Request


class Benchmark:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        request = Request(environ)
        # 打印请求的骑士
        first_at = datetime.datetime.now()
        begin_log = '[35mStarted[0m %s "%s" for %s at %s' % (request.method, request.path, request.remote_addr, first_at)
        Flask.app.logger.debug(begin_log)

        # 打印参数
        params = dict(request.args)
        params.update(request.form)
        params_log = "Parameters: %s" % params
        Flask.app.logger.debug(params_log)
        
        http_status = None
        def my_start_response(status, headers):
            nonlocal http_status
            http_status = status
            return start_response(status, headers);

        res = self.wsgi_app(environ, my_start_response)
        
        # 打印请求结束
        last_at = datetime.datetime.now()
        end_log = '[36mCompleted[0m %s in %sms\n' % (http_status, (last_at - first_at).microseconds/1000)
        Flask.app.logger.debug(end_log)
        return res