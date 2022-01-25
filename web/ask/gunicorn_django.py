#wsgi_django.py
CONFIG = {
		'mode':'wsgi',
		#'working_dir':'/home/box/web/ask',
                'working_dir':'/home/user1/stepik/stepic_web/web/ask',
		'python':'/usr/bin/python3',
		'args':(
			'--bind=0.0.0.0:8000',
			'--workers=1',
			'--timeout=60',
			'ask.wsgi:application'
		)
	}
