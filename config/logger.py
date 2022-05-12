from flask import Flask
import logging
import colorlog


# ============================= 日志处理器配置 =============================    
# 日志格式
file_log_formater = logging.Formatter("[%(asctime)s] %(name)s %(levelname)-7s : %(message)s")
console_log_formatter = colorlog.ColoredFormatter(
            "%(log_color)s[%(asctime)s] %(name)s %(levelname)-7s: %(message)s")

# 文件日志处理器
file_log_handler = logging.FileHandler("log/%s.log" % (Flask.app.env))
file_log_handler.setFormatter(file_log_formater)

# 中端日志处理器
stream_log_handler = logging.StreamHandler()
stream_log_handler.setFormatter(console_log_formatter)

# 设置统一的日志级别
log_level = 'debug' if not Flask.app.config['log_level'] else Flask.app.config['log_level']
log_level_int = logging.DEBUG

if log_level == 'debug':
    log_level_int = logging.DEBUG
if log_level == 'info':
    log_level_int = logging.INFO
if log_level == 'warning':
    log_level_int = logging.WARNING
if log_level == 'error':
    log_level_int = logging.ERROR

file_log_handler.setLevel(log_level_int)
stream_log_handler.setLevel(log_level_int)

# ============================== 各组件日志配置 ===============================
# Flask应用日志
flask_logger = logging.getLogger(Flask.app.name)
flask_logger.setLevel(log_level_int)
flask_logger.addHandler(file_log_handler)
flask_logger.addHandler(stream_log_handler)

# werkzeug日志
werkzeug_logger = logging.getLogger("werkzeug")
# 开发模式下 用benchmark的中间件显示请求相应基本信息
if Flask.app.env == 'development':
    werkzeug_logger.setLevel(logging.WARNING)
else:
    werkzeug_logger.setLevel(log_level_int)
werkzeug_logger.addHandler(file_log_handler)
werkzeug_logger.addHandler(stream_log_handler)

# sqlalchemy日志
sqlalchemy_logger = logging.getLogger('sqlalchemy.engine')
# 生产模式禁止输出SQL日志信息
if Flask.app.env == 'production' and log_level_int < logging.WARNING:
    sqlalchemy_logger.setLevel(logging.WARNING)
else:
    sqlalchemy_logger.setLevel(log_level_int)
sqlalchemy_logger.addHandler(file_log_handler)
# 开发模式把SQL日志输出到控制台
if Flask.app.env == 'development':
    sqlalchemy_logger.addHandler(stream_log_handler)

