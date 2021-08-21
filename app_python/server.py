"""Gunicorn server"""

from datetime import datetime
from pytz import timezone


def process_http_request(environ, start_response):
    """Response current Moscow time"""
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain; charset=utf-8'),
    ]
    start_response(status, response_headers)
    time = str(timezone('Europe/Moscow').localize(datetime.now())).encode('utf-8')
    return [time]
