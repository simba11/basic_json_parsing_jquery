from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.views.generic import ListView
from contact.models import Contact
from forms import NewContact
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt

class IndexView(ListView):
	template_name = 'index.html'
	context_object_name = 'latest_contact_list'
	def get_queryset(self):
		sim = self.request.method
		if self.request.method == 'GET':
			return Contact.objects.all()
		elif self.request.method == 'POST':
			new(self.request)

@csrf_exempt
def detail(request, contact_id):
	c = get_object_or_404(Contact, pk=contact_id)
	if request.method == 'GET':
		return render_to_response('detail.html', {'contact': c})
	elif request.method == 'DELETE':
		c.delete()
		return HttpResponseRedirect('/contact/')
	elif request.method == 'PUT':
		data = simplejson.loads(request.body)
		c.first_name = data['first_name']
		c.last_name = data['last_name']
		c.phone = data['phone']
		c.email = data['email']
		c.notes = data['notes']
		c.save()
		return HttpResponseRedirect('/contact/')

@csrf_exempt
def new(request):
	if request.POST:
		form = NewContact(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contact/')
	else:
		form = NewContact()

	args = {}
	args.update(csrf(request))
	args['form'] = form

	return render_to_response('new.html', args, context_instance=RequestContext(request)) 

@csrf_exempt
def JSONResponse(request, contact_id, extension):
	c = get_object_or_404(Contact, pk=contact_id)
	if request.method == 'GET':
	    to_json = {
	        "first_name": c.first_name,
	        "last_name": c.last_name,
	        "phone": c.phone,
	        "email": c.email,
	        "notes": c.notes
	    }
	    return HttpResponse(simplejson.dumps(to_json, sort_keys=True), mimetype='application/json')
	else:
		return render_to_response('detail.html', {'contact': c})
