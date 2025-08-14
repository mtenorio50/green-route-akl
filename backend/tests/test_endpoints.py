import urllib.request
import json

# Test different AT API endpoints to find the correct ones
endpoints_to_test = [
    "/gtfs/v3/",
    "/gtfs/v3/stops",
    "/gtfs/v3/routes",
    "/gtfs/v3/trips",
    "/gtfs/v3/stops-nearby",
    "/realtime/v2/",
    "/realtime/v2/vehicle-positions"
]

base_url = "https://api.at.govt.nz"
headers = {
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': '2fa50e2cd58543a9bc6cb06aa5da8989',
}

for endpoint in endpoints_to_test:
    try:
        url = f"{base_url}{endpoint}"
        print(f"\nTesting: {url}")

        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)

        print(f"✅ SUCCESS - Status: {response.getcode()}")

        # Try to read a small portion of the response
        data = response.read()[:500]  # First 500 bytes
        print(
            f"Response preview: {data.decode('utf-8', errors='ignore')[:100]}...")

    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error {e.code}: {e.reason}")
    except Exception as e:
        print(f"❌ Error: {e}")
