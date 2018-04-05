class search(object):
    def __init__(self):
        self.method = 'project.search'
        self.parameters = {
            'queryKey': '',
            'constraints': {
                'ids': [],
                'phids': [],
                'name': '',
                'members': [],
                'watchers': [],
                'status': '',
                'isMilestone': True,
                'icons': [],
                'colors': [],
                'parents': [],
                'ancestors': [],
            },
            'attachments': {
                'subscribers': None
            },
            'order': {},
            'before': {},
            'after': {},
            'limit': {},
        }
