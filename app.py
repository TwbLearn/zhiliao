from flask import Flask, render_template

# from decorators import login_required

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'questions': [{'id': '1', 'title': '这是第一个标题', 'content': '这里是第一个标题的内容',
                       'create_time': '2018-05-30 14:03:00',
                       'author_id': '1', 'author': '代永强'},
                      {'id': '2', 'title': '这是第二个标题', 'content': '这里是第二个标题的内容',
                       'create_time': '2018-05-30 14:32:14',
                       'author_id': '1', 'author': '代永强'},
                      {'id': '3', 'title': '这是第三个标题', 'content': '这里是第三个标题的内容',
                       'create_time': '2018-05-30 14:33:47',
                       'author_id': '1', 'author': '代永强'},
                      {'id': '4', 'title': '这是第四个标题', 'content': '这里是第四个标题的内容',
                       'create_time': '2018-05-30 14:40:11',
                       'author_id': '1', 'author': '代永强'},
                      {'id': '5', 'title': '这是第五个标题', 'content': '这里是第五个标题的内容',
                       'create_time': '2018-05-30 14:42:19',
                       'author_id': '1', 'author': '代永强'},
                      {'id': '6', 'title': '这是第六个标题', 'content': '这里是第六个标题的内容',
                       'create_time': '2018-05-30 14:51:25',
                       'author_id': '1', 'author': '代永强'}
                      ]
    }
    return render_template('index.html', **context)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/logout/')
def logout():
    pass


@app.route('/question/', methods=['GET', 'POST'])
# @login_required
def question():
    return render_template('question.html')


@app.route('/search/')
def search():
    # q = request.args.get('q')
    questions = {
        'questions': [{'id': '1', 'title': '这是第一个标题', 'content': '这里是第一个标题的内容',
                       'create_time': '20180530 14:03:00',
                       'author_id': '1', 'author': '代永强'},
                      {'id': '2', 'title': '这是第二个标题', 'content': '这里是第二个标题的内容',
                       'create_time': '20180530 14:03:00',
                       'author_id': '1', 'author': '代永强'}
                      ]
    }
    return render_template('index.html', questions=questions)


@app.route('/detail/<question_id>/')
def detail(question_id):
    question_model = {'id': question_id, 'title': '标题', 'content': '内容',
                      'create_time': '20180530 14:03:00',
                      'author_id': '1', 'author': '代永强'}
    return render_template('detail.html', question=question_model)


if __name__ == '__main__':
    app.run()
