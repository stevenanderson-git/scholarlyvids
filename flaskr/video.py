class Video:
    # Instead this should be created via a unique ID instead of string
    def __init__(self, video_title, thumbnail = 'gen_tech.jpg', video_url = '#', category = 'Unassigned', video_id = 0):
        # TODO: implement functional ID currently all videos will be ID1
        self.video_id = video_id
        # This should fetch the video title based on ID
        self.video_title = video_title
        # Access database and pull the rest of data to be accessed
        # Default Thumbnail
        self.thumbnail = 'thumbnails/' + thumbnail
        self.video_url = video_url
        self.category = category

    def data(self):
    #create json to encapsulate video data
        video_data = {
            'video_id': self.video_id,
            'video_title': self.video_title,
            'thumbnail': self.thumbnail,
            'video_url': self.video_url,
            'runtime': '1:23:45',
            'views': 'at least 1',
            'summary': 'long text description that will go here',
            'transcript_link': 'someurlvalue_clickme_other_place_on_site?',
            'category': self.category
        }
        return video_data
    
    def set_id(self, video_id):
        self.video_id = video_id


    def get_id(self):
        return str(self.video_id)

    def set_thumbnail(self, thumbnail):
        # Changes thumbnail if different than default
        self.thumbnail='thumbnails/{thumbnail}'
