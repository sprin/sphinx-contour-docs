"""
Sphinx extension to create links to Contour documents (typically requirements
items).

    :contour:`1412342`

links to https://www.contourhosted.com/perspective.req?projectId=2271&docId=1412342

when CONTOUR_PROJECT_ID = 2271 in Sphinx's conf.py.
"""

import urllib
from docutils import nodes, utils

CONTOUR_DOC_FORMAT = 'https://www.contourhosted.com/perspective.req?projectId={project_id}&docId={doc_id}'

def contour_doc(name, rawtext, text, lineno, inliner, options={},
    content=[]):
    env = inliner.document.settings.env
    project_id =  env.config.CONTOUR_PROJECT_ID

    if not project_id:
        raise Exception(
            'CONTOUR_PROJECT_ID is not set in conf.py. Set it to '
            'the numeric projectId as seen in email links.'
        )

    ref = CONTOUR_DOC_FORMAT.format(
     project_id = project_id,
     doc_id = urllib.quote(text, safe=''),
    )
    node = nodes.reference(rawtext, utils.unescape(text), refuri=ref, **options)
    return [node],[]

# Register the :contour: directive

def setup(app):
    app.add_config_value('CONTOUR_PROJECT_ID',
                         None,
                         'env')
    app.add_role('contour', contour_doc)

