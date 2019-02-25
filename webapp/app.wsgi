import os,sys
sys.path.append(os.path.dirname(__file__))
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

import bottle
import wordscapes_solver_web
# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()
