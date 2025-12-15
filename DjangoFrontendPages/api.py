from django.http import StreamingHttpResponse
import time
from datastar_py.consts import ElementPatchMode
from datastar_py.django import DatastarResponse
from datastar_py.django import ServerSentEventGenerator as SSE
from datastar_py.django import datastar_response 

from django.template.loader import render_to_string


@datastar_response
def LiveDataFeedEndpoint(request):

    for i in range(1,12):
        current_time = time.strftime('%H:%M:%S')
        # Format the data as a Datastar fragment event
        myhtml= f"""
        <div id="time">Current Time: {current_time}</div>\n
        """
        yield SSE.patch_elements(myhtml)
        time.sleep(1)
