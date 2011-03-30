from django.utils import simplejson
from dajaxice.core import dajaxice_functions
from dajax.core import Dajax

def myexample(request):
    return simplejson.dumps({'message':'Hello World'})


def showalert(request):
	dajax = Dajax()
	#dajax.alert("foo")
	#dajax.redirect("http://www.google.com",delay=0)
	dajax.script('alert("foo")')
	return dajax.json()

dajaxice_functions.register(showalert)
dajaxice_functions.register(myexample)
