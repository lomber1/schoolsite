
class Article:
    title_raw = None
    content_html_str = None
    publish_date_raw = None
    category_raw = None
    views_raw = None

    def __init__(self):
        pass

    def got_any_data(self):
        if self.title_raw is not None and \
           self.content_html_str is not None:
            return True

        else:
            return False
