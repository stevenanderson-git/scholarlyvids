from flask import Flask, render_template, request, jsonify, json, url_for
from werkzeug.utils import redirect
from video import *

app = Flask(__name__)



@app.route("/")
def home():
    title = 'ScholarlyVids - The best place to rate educational videos!'
    video_names = ["Bach", "Beethoven", "Mozart", "Lady Gaga", "Skrillix",
                    "Toby Keith", "FFDP", "Maynard", "Pop-Punk"]
    video_list = []
    for name in video_names:
        video_list.append(Video(name).data())

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

    # Create a video object to generalize the information being passed to page
    v = Video(video_title)

    return render_template('videopage.html', video_data=v.data())

@app.get("/search")
def search():
    #this route should do something with the search
    args = request.args
    page = 'search_results.html'
    title = 'Search Results'
    if args.get('q') != '':
        term = args.get('q')
        video_list = [Video("Oranges").data(), Video("Kiwi").data(), Video("Interesting").data(), Video("How to cat?").data(), Video("Code is Life").data(),
                    Video("Why, The novel").data(), Video("Ipsum, a history").data(), Video("Katchup").data(), Video("This is a test").data()]
        print(video_list)
        return render_template(page, term=term, video_list=video_list)
    

    return render_template(page, title=title)

@app.route("/advanced_search")
def advanced_search():
    page = 'advanced_search.html'
    title = 'Advanced Search'
    #TODO: meaningful categories from database categorization
    categories = ['Moon', 'Space', 'School', 'Water', 'Programming']
      

    return render_template(page, title=title, categories=categories)

# EOF
# TODO: Remove debug run
if __name__ == '__main__':
    app.run(debug=True)
# EOF
