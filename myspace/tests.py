from django.test import TestCase

# Create your tests here.
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
request = RequestFactory().get("/")
# Add support  django messaging framework
request._messages = messages.storage.default_storage(request)