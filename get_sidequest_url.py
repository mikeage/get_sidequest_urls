import argparse
import requests

SIDEQUEST_API_URL = "https://api.sidequestvr.com"


def get_app_id(app):
    if app.isdigit():
        return app

    app_id = app.split("/")[4]
    assert app_id.isdigit()
    return app_id


def get_token(app_id):
    url = "%s/generate-install" % SIDEQUEST_API_URL
    payload = {"msg": {"apps_id": app_id}}
    headers = {
        "Origin": "https://sidequestvr.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://sidequestvr.com/",
        "User-Agent": "Please-make-URLs-Available-Again-For-Offline",
    }
    r = requests.post(url, json=payload, headers=headers)
    if not r.ok:
        print("%s" % r.text)
        assert r.ok
    return r.json()["data"]["key"]


def get_game_url(key):
    url = "%s/install-from-key" % SIDEQUEST_API_URL
    headers = {
        "Origin": "https://sidequestvr.com",
        "User-Agent": "Please-make-URLs-Available-Again-For-Offline",
    }
    payload = {"token": key}
    r = requests.post(url, headers=headers, json=payload)
    if not r.ok:
        print("%s" % r.text)
        assert r.ok
    for dl_url in r.json()["data"]["apps"][0]["urls"]:
        if dl_url["extn"] in ("apk", "obb", "mod"):
            print("%s" % dl_url["link_url"])


def main(args):
    for app in args.app:
        key = get_token(get_app_id(app))
        get_game_url(key)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("app", nargs="+")
    main(parser.parse_args())
