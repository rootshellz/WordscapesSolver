import os
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

import bottle
import wordscrapes_solver_web
# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()
