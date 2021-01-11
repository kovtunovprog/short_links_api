from apps.short_links_api.views import CreateShortLinkView, ShortLinkInstanceView
from loader import api


# short_links_api.add_resource(HelloApi, '/short_links_api/1.0/short_links')
api.add_resource(CreateShortLinkView, '/short_links_api/1.0/short_links')
api.add_resource(ShortLinkInstanceView, '/short_links_api/1.0/short_links/<int:short_link_id>')
