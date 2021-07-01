from flask import Flask, render_template, request, jsonify, json, url_for
from werkzeug.utils import redirect
from video import Video

app = Flask(__name__)

video_1 = Video('The Insane Biology of: The Platypus', 'insane_biology_of_platypus.jpg', 'https://www.youtube.com/watch?v=Wh2du5SOjmY', 'Science', 1)
video_2 = Video('The Secret Language of Trees', 'secret_language_of_trees.jpg', 'https://www.youtube.com/watch?v=9HiADisBfQ0', 'Nature', 2)
video_3 = Video('How language shapes the way we think | Lera Boroditsky', 'thumbnail_id_3.jpg', 'https://www.youtube.com/watch?v=RKK7wGAYP6k', 'Language', 3)
video_4= Video('The Insane Engineering of the X-15', 'thumbnail_id_4.jpg', 'https://www.youtube.com/watch?v=7zR26e504uI', 'Engineering', 4)
video_5 = Video('The essence of calculus', 'thumbnail_id_5.jpg', 'https://www.youtube.com/watch?v=WUvTyaaNkzM', 'Math', 5)
video_6 = Video('Solar System 101 | National Geographic', 'thumbnail_id_6.jpg', 'https://www.youtube.com/watch?v=libKVRa01L8', 'Space', 6)
video_7 = Video('Introduction to Evolution and Natural Selection', 'thumbnail_id_7.jpg', 'https://www.youtube.com/watch?v=GcjgWov7mTM&list=PL7A9646BC5110CF64', 'Biology', 7)
video_8 = Video('Natural Selection - Crash Course Biology #14', 'thumbnail_id_8.jpg', 'https://www.youtube.com/watch?v=aTftyFboC_M', 'Biology', 8)
video_9 = Video('Moon 101 | National Geographic', 'thumbnail_id_9.jpg', 'https://www.youtube.com/watch?v=6AviDjR9mmo', 'Space', 9)
video_10 = Video('Computer Networks: Crash Course Computer Science #28', 'thumbnail_id_10.jpg', 'https://www.youtube.com/watch?v=3QhU9jd03a0', 'Computer Science', 10)
video_11 = Video('Mathematics is the queen of Sciences', 'thumbnail_id_11.jpg', 'https://www.youtube.com/watch?v=8mve0UoSxTo', 'Math', 11)
video_12 = Video('Superhuman Geniuses (Extraordinary People Documentary) | Real Stories', 'thumbnail_id_12.jpg', 'https://www.youtube.com/watch?v=xvDuqW9SFT8', 'Music', 12)


video_list = [video_1, video_2, video_3, video_4, video_5, video_6, video_7, video_8, video_9, video_10, video_11, video_12]

@app.route("/")
def home():
    title = 'Online STEM Education'
    # Fill this to populate home page
    return render_template('home.html', title = title, video_list = video_list)

@app.route("/page1")
def page1():
    return render_template('page1.html', title = 'page1')

@app.route("/page2")
def page2():
    return render_template('page2.html')

@app.route("/video/<video_id>")
def video_page(video_id):
    #look up info based on video_id
    #video id would be better if pulling from db
    #send video data in a video_object to populate page

    # Create a video object to generalize the information being passed to page
    for video in video_list:
        if video.get_id() == video_id:
            v = video
            break
        else:
            v = Video('Error')

    return render_template('videopage.html', video_data=v.data())

@app.get("/search")
def search():
    #this route should do something with the search
    args = request.args
    page = 'search_results.html'
    title = 'Search Results'
    if args.get('q') != '':
        term = args.get('q')        
        return render_template(page, term=term, video_list=video_list)
    

    return render_template(page, title=title)

@app.route("/advanced_search")
def advanced_search():
    page = 'advanced_search.html'
    title = 'Advanced Search'
    #TODO: meaningful categories from database categorization
    categories = ['Science', 'Math', 'History', 'Social Studies', 'Language', 'Writing', 'Music']
    subcategories = ['subcategory 1', 'subcategory 2', 'subcategory 3', 'subcategory 4', 'subcategory 5']
      

    return render_template(page, title=title, categories=categories, subcategories=subcategories)

# EOF
# TODO: Remove debug run
if __name__ == '__main__':
    app.run(debug=True)
# EOF
