CONFIG = {
    'working_dir': '/home/box/web',
    'args': (
        '--bind=0.0.0.0:8080',
        '--timeout=60',
        '--workers=16',
        'hello:app'
    )
}
