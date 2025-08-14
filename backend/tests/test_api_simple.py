import urllib.request
import json

try:
    print("Testing API endpoint...")
    response = urllib.request.urlopen(
        'http://127.0.0.1:8000/api/v1/vehicle-positions')
    data = json.loads(response.read().decode())
    print(f'✅ API Status: Success')
    print(f'🚍 Vehicle count: {len(data)}')
    if data:
        print('\n📍 Sample vehicle:')
        sample = data[0]
        print(f'   Vehicle ID: {sample.get("vehicle_id")}')
        print(f'   Route ID: {sample.get("route_id")}')
        lat = sample.get('lat')
        lon = sample.get('lon')
        speed = sample.get('speed_kmh')
        print(f'   Location: ({lat}, {lon})')
        print(f'   Speed: {speed} km/h')
        print(f'   Updated: {sample.get("updated_at")}')
        print('\n🎉 Real-time GTFS data integration successful!')
    else:
        print('❌ No vehicle data returned')
except Exception as e:
    print(f'❌ API Error: {e}')
