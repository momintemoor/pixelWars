import bottle
import json
import users


@bottle.route("/")
def index():
    return bottle.static_file("FrontEnd.html", root="Frontend.html")


@bottle.route("/stylesheet.css")
def static():
    return bottle.static_file("stylesheet.css", root="")


@bottle.route("/game.js")
def any_name():
    return bottle.static_file("game.js", root="")


@bottle.route('/users')
def get_users():
    return json.dumps(users.view_users())


@bottle.post('/Login')
def register_user():
    content = bottle.request.body.read().decode()
    content = json.loads(content)
    users.update_users(content['username'])
    return json.dumps(users.view_users())


bottle.run(host="0.0.0.0", port=8080, debug=True)