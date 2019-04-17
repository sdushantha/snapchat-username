#!/usr/bin/env python3
import requests


def main():
    username = input("Username: ")
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://accounts.snapchat.com/",
        "Cookie": "xsrf_token=PlEcin8s5H600toD4Swngg; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        }

    url = "https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={}&xsrf_token=PlEcin8s5H600toD4Swngg".format(username)

    r = requests.post(url, headers=headers)
    data = r.json()

    status = data.get("reference").get("status_code")
    sugestions = data.get("reference").get("suggestions")

    if status == "OK":
        print("Username is available")
    elif status == "TAKEN":
        print("Username is unavailable")

        if len(sugestions):
            print("Available usernames")

            for suggestion in sugestions:
                print("  ", suggestion)
        else:
            print("Username suggestions are not available")

    elif status == "TOO_LONG":
        print("Usernames cannot be longer than 15 character")

main()
