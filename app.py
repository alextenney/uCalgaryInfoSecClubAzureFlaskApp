from flask import Flask
app = Flask(__name__)

@app.route('/')
def flag():
  return 'magpie{4cc3553d_941n3d!}'
