from flask import Flask, render_template, request, jsonify, json, url_for
from werkzeug.utils import redirect
from video import Video

app = Flask(__name__)

cstring='Math 1st Grade'

video_1 = Video('Fact Family Triangles - Addition and Subtraction Cartoon | Math for 1st Grade | Kids Academy', 'thumbnail_id_1.jpg', 'https://www.youtube.com/watch?v=9IhZDEffyTk&list=PLiMIqKsOLxPxJEYh-CFNMlQjPx3fVKZOn', cstring, 1)
video_2 = Video('Comparing Numbers: 2-Digit Numbers | Math for 1st Grade | Kids Academy', 'thumbnail_id_2.jpg', 'https://www.youtube.com/watch?v=Fui9VPoiIWc&list=PLiMIqKsOLxPxJEYh-CFNMlQjPx3fVKZOn&index=4', cstring, 2)
video_3 = Video('Input and Output Tables - Find the Rule | Math for 1st Grade | Kids Academy', 'thumbnail_id_3.jpg', 'https://www.youtube.com/watch?v=nkIUE_sK4zQ&list=PLiMIqKsOLxPxJEYh-CFNMlQjPx3fVKZOn&index=5', cstring, 3)
video_4 = Video('Reading Bar Graph for Kids | Measurement and Data | Math for 1st Grade | Kids Academy', 'thumbnail_id_4.jpg', 'https://www.youtube.com/watch?v=LpdMMdU7IGM&list=PLiMIqKsOLxPxJEYh-CFNMlQjPx3fVKZOn&index=6', cstring, 4)
video_5 = Video('Bar Graphs for Kids | Math for 2nd Grade | Kids Academy', 'thumbnail_id_5.jpg', 'https://www.youtube.com/watch?v=lGZSfupOKB8&list=PLiMIqKsOLxPxJEYh-CFNMlQjPx3fVKZOn&index=7', cstring, 5)
video_6 = Video('Solving Word Problems | Math for 1st Grade | Kids Academy', 'thumbnail_id_6.jpg', 'https://www.youtube.com/watch?v=cqtXCzNEz0U&list=PLiMIqKsOLxPxJEYh-CFNMlQjPx3fVKZOn&index=8', cstring, 6)
video_7 = Video('Base Ten Blocks - Comparing Numbers | Math for 1st Grade | Kids Academy', 'thumbnail_id_7.jpg', 'https://www.youtube.com/watch?v=zU5LwvJJt5Y&list=PLiMIqKsOLxPxJEYh-CFNMlQjPx3fVKZOn&index=9', cstring, 7)
video_8 = Video('Learn Addition and Counting | Mental Math for 1st Grade | Kids Academy', 'thumbnail_id_8.jpg', 'https://www.youtube.com/watch?v=J8PQNQ2rYFU&list=PLiMIqKsOLxPxJEYh-CFNMlQjPx3fVKZOn&index=10', cstring, 8)
video_9 = Video('Skip Counting by 10 for Kids | How to Skip Count | Kids Academy', 'thumbnail_id_9.jpg', 'https://www.youtube.com/watch?v=8_aYQrFIKeU&list=PLiMIqKsOLxPxJEYh-CFNMlQjPx3fVKZOn&index=11', cstring, 9)
video_10 = Video('2 Dimensional Shapes: Vertices | Math for 1st Grade | Kids Academy', 'thumbnail_id_10.jpg', 'https://www.youtube.com/watch?v=Jyh15pyQ1xc&list=PLiMIqKsOLxPxJEYh-CFNMlQjPx3fVKZOn&index=12', cstring, 10)
video_11 = Video('Fact Families - Addition and Subtraction | Math for 1st Grade | Kids Academy', 'thumbnail_id_11.jpg', 'https://www.youtube.com/watch?v=76Ex6Z5DcN4&list=PLiMIqKsOLxPxJEYh-CFNMlQjPx3fVKZOn&index=13', cstring, 11)
video_12 = Video('Counting with Tally Marks and Tally Charts | Math for Kindergarten & 1st Grade | Kids Academy', 'thumbnail_id_12.jpg', 'https://www.youtube.com/watch?v=-pEA3w8SQws&list=PLiMIqKsOLxPxJEYh-CFNMlQjPx3fVKZOn&index=3', cstring, 12)


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
    categories = ['Science', 'Math', 'History', 'Social Studies', 'Language', 'Writing', 'Music', 'Engineering']
    subcategories = ['subcategory 1', 'subcategory 2', 'subcategory 3', 'subcategory 4', 'subcategory 5']
      

    return render_template(page, title=title, categories=categories, subcategories=subcategories)

# EOF
# TODO: Remove debug run
if __name__ == '__main__':
    app.run(debug=True)
# EOF
