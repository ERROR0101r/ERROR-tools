import requests
import json
import socket

def get_ip_info(ip_address):
    try:
        # Validate IP address
        socket.inet_aton(ip_address)
        
        # Use ip-api.com (free tier)
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        
        if data['status'] == 'success':
            print("\n" + "="*50)
            print(f"📡 IP Information for {ip_address}")
            print("="*50)
            print(f"🌍 Country: {data.get('country', 'N/A')}")
            print(f"🏙️ Region: {data.get('regionName', 'N/A')}")
            print(f"🏠 City: {data.get('city', 'N/A')}")
            print(f"📮 ZIP: {data.get('zip', 'N/A')}")
            print(f"📍 Coordinates: {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")
            print(f"🛜 ISP: {data.get('isp', 'N/A')}")
            print(f"🏢 Organization: {data.get('org', 'N/A')}")
            print(f"🔄 AS Number: {data.get('as', 'N/A')}")
            print("="*50)
            
            # Additional threat intelligence (using AbuseIPDB API - requires free API key)
            print("\n🔒 Threat Intelligence:")
            try:
                abuse_response = requests.get(
                    f"https://api.abuseipdb.com/api/v2/check",
                    headers={"Key": "YOUR_ABUSEIPDB_API_KEY", "Accept": "application/json"},
                    params={"ipAddress": ip_address}
                )
                abuse_data = abuse_response.json().get('data', {})
                print(f"🛡️ Abuse Confidence: {abuse_data.get('abuseConfidenceScore', 'N/A')}/100")
                print(f"🚨 Total Reports: {abuse_data.get('totalReports', 'N/A')}")
                print(f"🕒 Last Reported: {abuse_data.get('lastReportedAt', 'N/A')}")
            except:
                print("ℹ️ Add your AbuseIPDB API key for threat data")
            
        else:
            print("❌ Error: Could not retrieve IP information")
            
    except socket.error:
        print("❌ Invalid IP address format")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

def main():
    print("""
    🌐 IP Information Tool
    ----------------------
    This tool provides PUBLICLY AVAILABLE information about:
    - Geolocation
    - ISP details
    - Threat intelligence
    
    🔐 Privacy Note: Only retrieves information already publicly accessible
    """)
    
    while True:
        print("\nOptions:")
        print("1. Check IP information")
        print("2. Exit")
        
        choice = input("Select option: ")
        
        if choice == "1":
            ip = input("Enter IP address: ")
            get_ip_info(ip)
        elif choice == "2":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()