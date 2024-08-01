import os

token = os.getenv('COOKIE')
devCode = os.getenv('devCode')
WEAPI = os.getenv('WEAPI')
WEUSERID = os.getenv('WEUSERID')

if token == None:
	token = 'eyJhbGciOiJIUzI1NiJ9.eyJjcmVhdGVkIjoxNzIyNDczNDg1MTg1LCJ1c2VySWQiOjE1MDA0NDk0fQ.Td26GEbjUGdASwHl6spwogXlyI5pLJPUojJinyyqhG0'
if devCode == None:
	devCode = '3e1971c0-cf60-4d31-a415-175260f8b224'
