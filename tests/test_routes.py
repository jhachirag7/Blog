from blogexample.blueprints.blog.models import Post

def test_home(client):
    response=client.get('/')

    assert b'<title>Flask BLOG</title>' in response.data


def test_add_posts(client,app):
    with app.app_context():
        prev_count=Post.query.count()
    response=client.post("/add",data={'title':"chirag", 'body':"chirag","taglist":"chirag"})
    with app.app_context():
        assert Post.query.count()>prev_count
