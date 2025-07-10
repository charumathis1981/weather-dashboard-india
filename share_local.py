#!/usr/bin/env python3
"""
Local Network Sharing Script for Weather Dashboard
Run this to get shareable URLs for your local network
"""

import socket
import subprocess
import platform

def get_local_ip():
    """Get the local IP address"""
    try:
        # Connect to a remote server to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

def get_public_ip():
    """Get public IP address"""
    try:
        import requests
        response = requests.get('https://api.ipify.org?format=text', timeout=5)
        return response.text.strip()
    except:
        return "Unable to determine"

def check_port_open(port=8080):
    """Check if the port is open and accessible"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('localhost', port))
        sock.close()
        return result == 0
    except:
        return False

def main():
    print("🌐 Weather Dashboard - Sharing Information")
    print("=" * 50)
    
    # Check if app is running
    if not check_port_open(8080):
        print("❌ Weather Dashboard is not running on port 8080")
        print("   Please start the app first: python3 app.py")
        return
    
    print("✅ Weather Dashboard is running!")
    print()
    
    # Local access
    print("🏠 LOCAL ACCESS:")
    print(f"   http://localhost:8080")
    print(f"   http://127.0.0.1:8080")
    print()
    
    # Local network access
    local_ip = get_local_ip()
    print("📱 LOCAL NETWORK SHARING:")
    print(f"   http://{local_ip}:8080")
    print("   → Share this URL with devices on the same WiFi")
    print()
    
    # Public IP (for reference)
    public_ip = get_public_ip()
    print("🌍 PUBLIC IP (for cloud deployment reference):")
    print(f"   {public_ip}")
    print("   → This is your router's public IP")
    print()
    
    # Platform-specific firewall instructions
    system = platform.system()
    print("🔥 FIREWALL SETUP:")
    if system == "Darwin":  # macOS
        print("   macOS: System Preferences → Security & Privacy → Firewall")
        print("   Allow incoming connections for Python")
    elif system == "Windows":
        print("   Windows: Windows Defender Firewall → Allow an app")
        print("   Add Python to allowed apps")
    else:  # Linux
        print("   Linux: sudo ufw allow 8080")
    print()
    
    print("🚀 FOR INTERNET SHARING:")
    print("   See DEPLOYMENT.md for cloud deployment options")
    print("   Recommended: Railway (railway.app) - Free & Easy")
    print()
    
    # QR Code suggestion
    try:
        import qrcode
        print("📱 QR CODE:")
        qr = qrcode.QRCode(version=1, box_size=1, border=1)
        qr.add_data(f"http://{local_ip}:8080")
        qr.make(fit=True)
        qr.print_ascii(invert=True)
    except ImportError:
        print("📱 QR CODE: Install 'qrcode' package to generate QR codes")
        print("   pip install qrcode[pil]")

if __name__ == "__main__":
    main()
