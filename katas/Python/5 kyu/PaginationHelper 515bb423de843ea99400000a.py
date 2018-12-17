# https://www.codewars.com/kata/515bb423de843ea99400000a
from math import ceil


class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = len(collection)
        self.items_per_page = items_per_page
      
    def item_count(self):
        return self.collection
  
    def page_count(self):
        return ceil(self.collection * 1.0 / self.items_per_page)
      
    def page_item_count(self, page_index):
        page_first_index = page_index * self.items_per_page
        if page_first_index > self.collection:
            return -1
        elif page_first_index + self.items_per_page >= self.collection:
            return self.collection % self.items_per_page
        else:
            return self.items_per_page

    def page_index(self, item_index):
        return item_index // self.items_per_page if 0 <= item_index < self.collection else -1
  