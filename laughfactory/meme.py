from flask import ( Blueprint, render_template, request, redirect ) 
from . import models 
bp = Blueprint('meme', __name__, url_prefix="/meme")