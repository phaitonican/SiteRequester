FROM python:3
ADD SiteRequester.py /
CMD [ "python", "./SiteRequester.py" ]