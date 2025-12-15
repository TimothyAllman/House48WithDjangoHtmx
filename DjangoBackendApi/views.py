from datastar_py.consts import ElementPatchMode
from datastar_py.django import DatastarResponse
from datastar_py.django import ServerSentEventGenerator as SSE

from django.template.loader import render_to_string



def NewOutputEndpoint(request):
    item_count = 800

    return DatastarResponse([
        SSE.patch_elements(
            render_to_string('NewOutput.html')
        ),
        SSE.patch_elements(
            render_to_string('NewCount.html', context=dict(count=item_count))
        ),
    ])

