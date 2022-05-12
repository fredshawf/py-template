from flask import Blueprint, Flask, request
from ..models.sys_user import SysUser

# 此处蓝图路由
# 参数1：蓝图路由唯一标识(可以理解成一个bean，名称不能和其他蓝图重复)
# 参数2：当前模块的名称
# 参数3：指定路由的前缀
blueprint = Blueprint('test', __name__, url_prefix='/test')


# 定义改路由后，可通过http://host:port/test/hello 得到访问
@blueprint.route("/hello")
def hello():
    
    user = SysUser.query.first()
    Flask.app.logger.debug(user.id)
    # print(user.id)
    return "hello"