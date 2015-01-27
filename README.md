tw4d
====

tw4d is pretty Twitter client for Cinema4D console.
search timeline "Cinema4d", "C4D".

![](./tw4d.png)

## Setup

#### 1. Get Twitter Developer "Consumer Key" & "Consumer Secret".

https://apps.twitter.com/

`"Create New App" -> get "ConsumerKey(API Key)" & "ConsumerSecret(API Secret)"`

![](./get_twitter_dev_key.png)

#### 2. Change the `tw4d.py`.

```python
CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'
```

#### 3. Python 3rd library install.

- [tweetpy](https://github.com/tweepy/tweepy)
- [oauthlib](https://github.com/idan/oauthlib)
- [requests](https://github.com/kennethreitz/requests)
- [requests_oauthlib](https://github.com/requests/requests-oauthlib)

in C4D `Edit -> Preference -> Open Preferences Folder`

![](./open_preferences_folder.png)

copy and unzip the downloaded files.

```
/library/python/packages/win64/
|- tweepy(source directory)
|- oauthlib(source directory)
|- requests(source directory)
|- requests_oauthlib(source directory)
```

![](./3rd_library_install.png)

#### 4. The python module of Cinema4D, change the SSL build.

Install (just for me option) the [Python2.6](https://www.python.org/download/releases/2.6.6/).

**_!!! backup original c4d-python directory._**

copy
`C:\Python26\...`
to
`C:\Program Files\MAXON\CINEMA 4D R14\resource\modules\python\res\Python.win64.framework\...`.

#### 5. Copy `tw4d.py` to script folder.

## let's

open console window. run script `tw4d.py` !

the first time must be set OAuth and enter PIN code.
