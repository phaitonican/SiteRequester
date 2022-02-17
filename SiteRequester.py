import requests
import time

class SiteRequester:

    url ="https://twitch.tv/phaiton12"
    
    def request_url(self):
        r = requests.head(self.url)
        print("Response: " + str(r))

    def repeat_function(self, function, repeating_time):
        while True:
            function()
            print("Repeating after " + str(repeating_time) + " seconds.")
            time.sleep(repeating_time)

    def repeat_request_url_function(self, repeating_time):
        self.repeat_function(self.request_url, repeating_time)


SiteRequester = SiteRequester()

SiteRequester.repeat_request_url_function(3)