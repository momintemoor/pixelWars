import bottle
import json
import users

@bottle.route("/")
def any_name():
    return bottle.static_file("FrontEnd.html", root="FrontEnd.html")


@bottle.route("/game.js")
def any_name():
    return bottle.static_file("game.js", root="game.js")


@bottle.post('/Login')
def register_user():
    content = bottle.request.body.read().decode()
    content = json.loads(content)
    users.update_users(content["username"])
    return json.dumps(users.view_users())


if __name__ == '__main__':
    bottle.run(host="0.0.0.0", port=8080, debug=True)