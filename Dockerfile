FROM python:3
ADD SiteRequester.py /
RUN pip install requests
CMD [ "python", "-u", "./SiteRequester.py" ]