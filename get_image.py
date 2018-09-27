import cherrypy
from cherrypy import expose
import urllib.request

urllib.urlretrieve

class ImageDownloader:

    @expose
    def get_image(self):
        return request_image(self)

    @expose
    def request_image(self):
	resource = urllib.urlopen("http://cdn.collider.com/wp-content/gallery/featured-thumbs-d/daredevil-season-3-image-2-copy.jpg")
	output = open("file01.jpg","wb")
	output.write(resource.read())
	output.close()
       	return output

cherrypy.quickstart(ImageDownloader())