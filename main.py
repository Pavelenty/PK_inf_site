from flask import Flask, request, render_template
from utils import load_data, define_page

app = Flask(__name__)


@app.route('/')
@app.route('/<string:id>', methods=["GET", "POST"])
def page_id(id="Монитор"):
    data = load_data()
    id = request.form.get('pressed_but')
    if define_page(id) == None:
        article = {
        "name": "Главная",
        "text": [{"child_header": "", "text": [""], "img": "", "class": "not_working_img"}]
    }
    else:
        article = define_page(id)
    return render_template('index.html', data=data, id=id, article=article)


if __name__ == '__main__':
    app.run(debug=True)