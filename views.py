from flask import Blueprint
from marshmallow import ValidationError

app_bp = Blueprint('main', __name__)

@app_bp.route("/perform_query", methods=['POST'])
def perform_query():
    try:
        params = BatchRequestParams().load(request.json)

    except ValidationError as e:
        return e.message, 404

    result = None
    for query in params['queries']:
        result = build_query(cmd=query['cmd'], param=query['param'], data=result)

    return jsonify(result)


    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    return app.response_class('', content_type="text/plain")