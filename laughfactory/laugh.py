from flask import ( Blueprint, render_template )
import json
bp = Blueprint(
    'meme',
    __name__,
    url_prefix="/memes"
)

@bp.route('/')
def index():
    return render_template('index.html',memes=memes)

@bp.route('/login')
def show_pet():
    return render_template('login.html')

@bp.route('/new')
def new_pet():
    return render_template('signup.html')

memes = json.load(open('meme.json'))