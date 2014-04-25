import sys
import time
import json
import urllib2
from urllib import urlencode

try:
    ACCESS_TOKEN = sys.argv[1]
    YOUR_USER = sys.argv[2]
    TARGET_USER = sys.argv[3]
    EVEN_AT = sys.argv[4]
except IndexError:
    print "\nUsage: ~$ python payback.py access_token your_user_id target_user_id time_even_at\n"
    sys.exit(1)

def get_disparity(source, target):
    recents_request = urllib2.urlopen('https://api.venmo.com/v1/payments?access_token='+ACCESS_TOKEN)
    recents_response = recents_request.read()
    recents = json.loads(recents_response)['data']

    payments_from_target = payments_to_target = 0
    for entry in recents:
        if entry['date_created'] > EVEN_AT and entry['action'] == 'pay':
            if entry['actor']['id'] == target:
                payments_from_target += entry['amount']
            elif entry['actor']['id'] == source and entry['target']['user']['id'] == target:
                payments_to_target += entry['amount']
    return payments_from_target - payments_to_target

def pay(target, amount):
    data = urlencode({
        'access_token': ACCESS_TOKEN,
        'user_id': target,
        'note': 'Your payment was automatically refunded to you with Payback(tm), an application developed by Harrison Liddiard, at %s.' % time.strftime('%c'),
        'amount': amount
    })
    try:
        payment = urllib2.urlopen('https://api.venmo.com/v1/payments', data).read()
    except urllib2.HTTPError as e:
        return e.read()
    return payment


disparity = get_disparity(YOUR_USER, TARGET_USER)

if disparity > 0:
    payment = pay(TARGET_USER, disparity)
    print payment
