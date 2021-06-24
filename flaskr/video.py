class Video:
    # Instead this should be created via a unique ID instead of string
    def __init__(self, video_title):
        # TODO: implement functional ID currently all videos will be ID1
        self.video_id = 1
        # This should fetch the video title based on ID
        self.video_title = video_title
        # Access database and pull the rest of data to be accessed
        # Default Thumbnail
        self.thumbnail = 'thumbnails/gen_tech.jpg'

    def data(self):
    #create json to encapsulate video data
        video_data = {
            'video_id': self.video_id,
            'video_title': self.video_title,
            'thumbnail': self.thumbnail,
            'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'runtime': '1:23:45',
            'views': 'at least 1',
            'summary': 'long text description that will go here',
            'transcript_link': 'someurlvalue_clickme_other_place_on_site?',
            'category': 'Technology'
        }
        return video_data
    
    def set_thumbnail(self, thumbnail):
        # Changes thumbnail if different than default
        self.thumbnail='thumbnails/{thumbnail}'
