from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRequestError, TwitterConnectionError

try:
    o = TwitterOAuth.read_file('./env/credentials.txt')
    api = TwitterAPI(o.consumer_key, o.consumer_secret, o.access_token_key, o.access_token_secret)
    r = api.request('statuses/sample')

    for item in r:
        print(item)

except TwitterRequestError as e:
    print(e.status_code)
    for msg in iter(e):
            print(msg)

except TwitterConnectionError as e:
    print(e)

except Exception as e:
    print(e)