import bottle
import json

import users



@bottle.route("/")
def any_name():
    return bottle.static_file("FrontEnd.html", root="")


@bottle.route("/game.js")
def any_name():
    return bottle.static_file("game.js", root="")

@bottle.post('/Login')
def register_user():
    content = bottle.request.body.read().decode()
    content = json.loads(content)
    users.add_user(content['user'])
    return json.dumps(users.view_users())





bottle.run(host="0.0.0.0", port=8080, debug=True)