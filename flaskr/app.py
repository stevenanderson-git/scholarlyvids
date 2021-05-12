from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    title = 'ScholarlyVids - The best place to rate educational videos!'
    return render_template('home.html', title = title)

@app.route("/page1")
def page1():
    return render_template('page1.html', title = 'page1')

@app.route("/page2")
def page2():
    return render_template('page2.html')



# EOF
# TODO: Remove debug run
if __name__ == '__main__':
    app.run(debug=True)
# EOF
