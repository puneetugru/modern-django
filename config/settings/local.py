from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='a2)=h%_(lc0v#kk!n&vp^q)tx2wecoayu-a*1=26z+-s+1ic&u')

DEBUG = env.bool('DJANGO_DEBUG', default=True)