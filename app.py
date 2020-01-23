from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

dubug = DebugToolbarExtension(app)


@app.route("/")
def index():
    print('jjjjjjjjj', story)
    
    prompts = story.prompts
    print(prompts)
    # return "<h1>Hi</h1>"
    return render_template("form.html", prompts=prompts)

@app.route("/story")
def show_story():

    text = story.generate(request.args)

    return render_template("story_template.html", text=text)

