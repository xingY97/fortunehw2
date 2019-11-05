from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/fortune')
def fortune_form():
                return render_template('fortune_form.html')

@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    users_favorite_animal = request.args.get('animal')
    title = request.args.get('title')
    name = request.args.get('name')

    if users_favorite_animal == 'unicorn':
        fortune = " you will have a sunny day"
    elif users_favorite_animal == 'cat':
        fortune = "you will have a good day"
    elif users_favorite_animal == "dog":
        fortune = "you will have a lucky day"
    else:
        fortune = "you will have a bad day"
    return render_template('fortune_result.html', fortune=fortune, title=title, name=name)
