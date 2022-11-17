import fileinput

tag = "p"
delete_empties = True

body = ""

for line in fileinput.input():
    line = line.strip()
    if delete_empties is True and line == "":
        continue
    body += f"\n    <{tag}>{line}</{tag}>"

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Untitled</title>
    <style>

    </style>
</head>
<body>
<h1>Lexicon of Philippine Weather Report News Titles</h1>
    <p>We read weather reports, but only the Facebook previews.</p>
    <a href="index.html">ALL</a>
    <a href="sym.html">#</a>
    <a href="a.html">A</a>
    <a href="b.html">B</a>
    <a href="c.html">C</a>
    <a href="d.html">D</a>
    <a href="e.html">E</a>
    <a href="f.html">F</a>
    <a href="g.html">G</a>
    <a href="h.html">H</a>
    <a href="i.html">I</a>
    <a href="j.html">J</a>
    <a href="k.html">K</a>
    <a href="l.html">L</a>
    <a href="m.html">M</a>
    <a href="n.html">N</a>
    <a href="o.html">O</a>
    <a href="p.html">P</a>
    <a href="q.html">Q</a>
    <a href="r.html">R</a>
    <a href="s.html">S</a>
    <a href="t.html">T</a>
    <a href="u.html">U</a>
    <a href="v.html">V</a>
    <a href="x.html">X</a>
    <a href="y.html">Y</a>
    <a href="z.html">Z</a>
    {body}
</body>
</html>
"""

print(html)
