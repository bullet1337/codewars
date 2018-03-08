# https://www.codewars.com/kata/5a57d101cadebf03d40000b9
import requests
import re


def get_leaderboard_honor():
    return [int(match.group(1)) for match in
            re.finditer('<tr data-username.*?<td.*?</td><td.*?</td><td.*?</td><td>(\d+)',
                        requests.get('https://www.codewars.com/users/leaderboard').content.decode('utf8'))]