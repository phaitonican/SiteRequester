FROM python:3
ADD SiteRequester.py /
RUN pip install request
CMD [ "python", "./SiteRequester.py" ]