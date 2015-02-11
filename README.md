# Why?

Venmo doesn't allow you to prevent someone from paying you.
Why would you *not* want money, you ask? 
Maybe someone did you a favor and won't let you pay them back. 
Maybe you did the favor and you want to maintain the upper hand when the time comes by not accepting a payment now.
Whichever your case, what you need is payback.

# Usage

1. Get your Venmo access token: https://venmo.com/account/settings/developers
2. Get your user id and the id of the user who is trying to be overly generous or trying to hold something over you.
3. Get the time at which you were "even" with the other person in ISO 8601 format.
4. Run the script with the above information, and your target will be paid the appropriate amount.

You'll probably want to run this as a cron job on a server every few minutes so you don't have to 
keep manually paying the person back if they're persistent. Sooner or later they'll get the idea.

This has not been extensively tested, so if you start losing money at a precipitous rate becasue of some bug, 
you have been warned, and please see LICENSE before suing.
