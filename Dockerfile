FROM python:3
ADD SiteRequester.py /
RUN pip install requests time
CMD [ "python", "./SiteRequester.py" ]