import markdown
import jinja2
import pathlib

# convert article to HTML
source = open('article.md', 'r').read()
md = markdown.Markdown(extensions=['meta'])
html = md.convert(source)
meta = md.Meta
if 'title' in meta:
    meta['title'] = meta['title'][0]
if 'date' in meta:
    meta['date'] = meta['date'][0]
if 'authors' in meta:
    meta['authors'] = ', '.join(meta['authors'])
article = dict(source=source, html=html, meta=meta)

# run through template
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("templates"),
    )
template = env.get_template('content.html')
output_html = template.render(**article)

# output to file
pathlib.Path('output/').mkdir(parents=True, exist_ok=True)
with open('output/article.html', 'w') as f:
    f.write(output_html)
