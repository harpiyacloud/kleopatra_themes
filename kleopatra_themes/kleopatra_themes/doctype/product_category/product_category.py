# Copyright (c) 2022, Harpiya Software Technologies and contributors

#import harpiya
from harpiya.website.website_generator import WebsiteGenerator
from harpiya.website.utils import clear_cache
from slugify import slugify

class ProductCategory(WebsiteGenerator):
    def autoname(self):
        # to override autoname of WebsiteGenerator
        self.name  = slugify(self.title)

    def on_update(self):
        clear_cache()

    def set_route(self):
        # Override blog route since it has to been templated
        self.route = 'product/' + self.name