from flask import Flask

def create_app():
    app = Flask(__name__)
    @app.route('/')
    def hello():
        return "Hello, it's Meme!"

    from . import meme
    app.register_blueprint(meme.bp)
    return app