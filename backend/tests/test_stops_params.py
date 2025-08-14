import urllib.request
import json

# Test the stops endpoint with different parameters
base_url = "https://api.at.govt.nz"
headers = {
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': '2fa50e2cd58543a9bc6cb06aa5da8989',
}

# Test different parameter formats
test_cases = [
    {"endpoint": "/gtfs/v3/stops", "params": ""},
    {"endpoint": "/gtfs/v3/stops", "params": "?page[size]=10"},
    {"endpoint": "/gtfs/v3/stops", "params": "?page%5Bsize%5D=10"},  # URL encoded
    {"endpoint": "/gtfs/v3/stops", "params": "?limit=10"},
]

for test in test_cases:
    try:
        url = f"{base_url}{test['endpoint']}{test['params']}"
        print(f"\nTesting: {url}")

        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)

        print(f"✅ SUCCESS - Status: {response.getcode()}")

        data = json.loads(response.read())
        print(f"Response has {len(data.get('data', []))} items")

        if data.get('data'):
            first_stop = data['data'][0]
            attrs = first_stop.get('attributes', {})
            print(
                f"Sample stop: {attrs.get('stop_name', 'Unknown')} (ID: {first_stop.get('id', 'Unknown')})")

    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error {e.code}: {e.reason}")
        try:
            error_body = e.read().decode('utf-8')
            print(f"Error details: {error_body[:200]}...")
        except:
            pass
    except Exception as e:
        print(f"❌ Error: {e}")
