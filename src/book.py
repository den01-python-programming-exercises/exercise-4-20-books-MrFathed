class Book:
    def __init__(self, title, num_of_pages, pub_year):
        self.title = title
        self.num_of_pages = num_of_pages
        self.pub_year = pub_year

    def __str__(self):
        return self.title + ", " + str(self.num_of_pages) + " pages, " + str(self.pub_year)
        
    def get_title(self):
        return self.title

    def get_num_of_pages(self):
        return self.num_of_pages

    def get_publication_year(self):
        return self.pub_year