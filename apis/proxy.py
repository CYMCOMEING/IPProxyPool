from flask.views import MethodView
from flask import request, jsonify
from logics.proxy import ProxyLogic
from apis import app


class ProxyAPI(MethodView):

    def get(self):
        proxy_logic = ProxyLogic()
        proxy = proxy_logic.random()
        data = {
            'code': 0,
            'proxy': proxy
        }
        return jsonify(data)

    def delete(self):
        proxy = request.args.get('proxy')
        proxy_logic = ProxyLogic()
        proxy_logic.descrease(proxy)
        data = {
            'code': 0,
            'msg': '减分成功'
        }
        return jsonify(data)


app.add_url_rule(
    '/proxy', view_func=ProxyAPI.as_view('proxy'), endpoint="proxy")
