from flask import render_template

from .app import app, pages


@app.route('/')
def home():
    posts = [p for p in pages if p.meta.get('layout') == 'post']

    # sort by date
    sorted_posts = sorted(posts, reverse=True, key=lambda p: p.meta.get('date'))

    return render_template('index.html', pages=sorted_posts)


@app.route('/<path:path>/')
def page(path):
    # path is the filename of a page, without the file extension
    post = pages.get_or_404(path)
    return render_template('page.html', page=post)


@app.route('/about.html')
def me():
    return render_template('about.html', page=pages.get_or_404('about'))
