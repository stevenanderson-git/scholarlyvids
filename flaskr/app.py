from flask import Flask, render_template, request, jsonify, json, url_for
from werkzeug.utils import redirect

app = Flask(__name__)



@app.route("/")
def home():
    title = 'ScholarlyVids - The best place to rate educational videos!'
    video_list = ["Bach", "Beethoven", "Mozart", "Lady Gaga", "Skrillix",
                    "Toby Keith", "FFDP", "Maynard", "Pop-Punk"]
    return render_template('home.html', title = title, video_list = video_list)

@app.route("/page1")
def page1():
    return render_template('page1.html', title = 'page1')

@app.route("/page2")
def page2():
    return render_template('page2.html')

@app.route("/video/<video_title>")
def video(video_title):
    #look up info based on either video_title or video_id
    #video id would be better if pulling from db
    #send video data in a video_object to populate page

    #create json to encapsulate video data
    video_data = {
        'video_title': video_title,
        'thumb_url': 'https://via.placeholder.com/1920x1080',
        'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'runtime': '1:23:45',
        'views': 'at least 1',
        'summary': 'long text description that will go here',
        'transcript_link': 'someurlvalue_clickme_other_place_on_site?'
    }

    return render_template('videopage.html', video_data=video_data)

@app.get("/search")
def search():
    #this route should do something with the search
    args = request.args
    page = 'search_results.html'
    title = 'Search Results'
    if args.get('q') != '':
        term = args.get('q')
        video_list = ["Oranges", "Kiwi", "Interesting", "How to cat?", "Code is Life",
                    "Why, The novel", "Ipsum, a history", "Katchup", "This is a test"]
        return render_template(page, term=term, video_list=video_list)
    

    return render_template(page, title=title)

@app.route("/advanced_search")
def advanced_search():
    page = 'advanced_search.html'
    title = 'Advanced Search'
    args = request.args

    #TODO: meaningful categories from database categorization
    categories = ['Moon', 'Space', 'School', 'Water', 'Programming']


    if args:
        term = args.get('search-term')
        

    return render_template(page, title=title, categories=categories)

# EOF
# TODO: Remove debug run
if __name__ == '__main__':
    app.run(debug=True)
# EOF
