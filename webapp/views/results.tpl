<h1><a href="http://wordscapessolver.rootshellz.com">Wordscape Solver</a></h1>
<img src="https://images-na.ssl-images-amazon.com/images/I/81cd6JSC0KL._SY355_.png">
<br>
<a href="https://github.com/rootshellz/WordscapesSolver" target=”_blank”>https://github.com/rootshellz/WordscapesSolver</a>

<br><br>

<h2>Results</h2>
<p><strong>Input Solvable</strong>: <i>{{solvable}}</i></p>
<p><strong>Input Available Characters</strong>: <i>{{available_chars}}</i></p>
<p><strong>Possible Words</strong>:</p>
<ul>
  % for item in possible_words:
    <li>{{item}}</li>
  % end
</ul>
