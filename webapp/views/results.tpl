<h1>Wordscape Solver</h1>
<h2>by <a href="https://github.com/rootshellz" target=”_blank”>rootshellz</a></h2>
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
