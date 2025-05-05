import toml

with open('data.toml', 'r') as f:
    data = toml.load(f)

for word in data.values():
    with open('template.html', 'r') as html:
        doc = html.read()

    doc = doc.replace('{{name}}', word['name'])
    doc = doc.replace('{{body}}', word['body'])
    doc = doc.replace('{{note}}', word['note'])
    doc = doc.replace('{{etymology}}', word['etymology'])

    with open('vectors/' + word['name'] + '.svg', 'r') as svg:
        doc = doc.replace('{{sitelen}}', svg.read())

    br = '<br>'.join(word['examples']) + '<br>'
    doc = doc.replace('{{examples}}', br)

    table = ''
    for trans in word['translations']:
        table += '<tr><td>' + trans[0] + '</td><td>' + trans[1] + '</td></tr>'
    doc = doc.replace('{{translations}}', table)

    with open('docs/' + word['name'] + '.html', 'w') as prod:
        prod.write(doc)
