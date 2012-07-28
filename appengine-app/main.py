#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	 http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

from google.appengine.api import channel
from google.appengine.ext.webapp import template

class MainHandler(webapp2.RequestHandler):
	def get(self):
		token = channel.create_channel('foo')
		params = { 'token': token }
		self.response.out.write(template.render('index.html', params))
	def post(self):
		token = self.request.get('token')
		message = self.request.get('m')
		channel.send_message(token, message)

class JqueryHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(template.render('jquery.js', {}))

app = webapp2.WSGIApplication([('/', MainHandler), ('/jquery.js', JqueryHandler)],
							  debug=True)