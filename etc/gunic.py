CONFIG = {
    'mode': 'django',
    'environment': {
        'PYTHONPATH': '/home/box/web/ask/',
    },
    # 'working_dir': '/',
    # 'user': 'www-data',
    # 'group': 'www-data',
    'args': (
        # '--bind=127.0.0.1:8000',
        '--workers=4',
        # '--worker-class=egg:gunicorn#sync',
        # '--timeout=30',
        'settings',
    ),
}
