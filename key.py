import os

token = os.getenv('COOKIE')
devCode = os.getenv('devCode')
WEAPI = os.getenv('WEAPI')
WEUSERID = os.getenv('WEUSERID')

if token == None:
	token = 'eyJhbGciOiJIUzI1NiJ9.eyJjcmVhdGVkIjoxNzMzNzg4NTU0MDM2LCJ1c2VySWQiOjE1MDA0NDk0fQ.bh9kwray4Jvy_HI3SYorFNhgeQTJRz34_X4w2Vqa75w'
if devCode == None:
	devCode = '7rjth7p2eccL4WCgrOonPojEOoe2tABD'
