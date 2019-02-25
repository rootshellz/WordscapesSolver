import os, sys
sys.path.append("..")
import wordscapes_solver
from bottle import run, route, request, static_file, template

word_list_file = "../words_alpha.txt"


@route("/")
def index():
    if request.params.get("solvable") and request.params.get("available_chars"):
        solvable = request.params.get("solvable").lower().replace("-", "_")
        available_chars = sorted(request.params.get("available_chars").lower())
        possible_words = sorted(wordscapes_solver.solve(solvable, available_chars, word_list_file))
        return template("results", {"solvable": solvable.upper(),\
                                    "available_chars": request.params.get("available_chars").upper(),\
                                    "possible_words": possible_words})
    else:
        return static_file("index.html", root="./html")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
