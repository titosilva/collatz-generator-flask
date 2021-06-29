from flask import Flask, render_template, url_for
from jinja2.environment import Template

from collatz_map_generator import CollatzMapGenerator

app = Flask(__name__, static_url_path="", static_folder="static")

ROOT_TEMPLATE = """
<html>
    <head>
        <link rel="stylesheet" href="{{ css }}">
    </head>
    <body>
        {{ content }}
    </body>
</html>
"""

@app.route('/')
def index():
    generator = CollatzMapGenerator(1000)
    template = Template(ROOT_TEMPLATE)
    css = url_for('static', filename= 'styles.css')
    return template.render(content = generator.generate_map(), css = css)

if __name__ == "__main__":
    app.run("localhost", 3000)
