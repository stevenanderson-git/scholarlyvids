from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    title = 'ScholarlyVids - The best place to rate educational videos!'

    musicians = ["Bach", "Beethoven", "Mozart", "Lady Gaga", "Skrillix",
                    "Toby Keith", "FFDP", "Maynard", "Pop-Punk"]


    return render_template('home.html', title = title, musicians=musicians)

@app.route("/page1")
def page1():
    return render_template('page1.html', title = 'page1')

@app.route("/page2")
def page2():
    return render_template('page2.html')

@app.route("/video/<name>")
def video(name):
    return render_template('videoresult.html', name = name)

@app.get("/search_results")
def search_results():
    args = request.args
    page = 'search_results.html'
    title = 'Search Results'
    if args:
        term = args.get('search')
        return render_template(page, term=term)
    

    return render_template(page, title=title)

# EOF
# TODO: Remove debug run
if __name__ == '__main__':
    app.run(debug=True)
# EOF
