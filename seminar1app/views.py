import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, 'seminar1app/index.html')


def about(request):
    logger.debug('About us page accessed')
    return render(request, 'seminar1app/about.html')
