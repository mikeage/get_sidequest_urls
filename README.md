# Get URLs from SideQuestVR for direct download

Fork of https://github.com/hemachandsai/sidequest-hacks.git in python.

I wish this wasn't necessary, but sometimes, wget/curl is far more reliable than the sidequest downloader.

Code is tested with python3, but probably works on python2.

## Installation

You need the requests package; nothing else. If you don't have it:
```bash
pip install requests
```

## Execution
Give it one or more URLs to a sidequest app. You can also give it the number directly, if you prefer
```bash
python get_sidequest_url.py https://sidequestvr.com/app/567/cosmic-flow-a-relaxing-vr-experience
python get_sidequest_url.py 567
python get_sidequest_url.py https://sidequestvr.com/app/567/cosmic-flow-a-relaxing-vr-experience https://sidequestvr.com/app/1042/liminal
python get_sidequest_url.py 567 https://sidequestvr.com/app/1042/liminal
python get_sidequest_url.py 567 1042
```
