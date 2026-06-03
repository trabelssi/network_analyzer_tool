#!/usr/bin/env python3
"""
Example Data Generator for Network Analyzer Tool
Generates sample packet capture file for testing the network analyzer
"""

from scapy.all import IP, TCP, UDP, ICMP, Raw, wrpcap
import random
from datetime import datetime

def generate_example_packets():
    """Generate sample packets for testing"""
    packets = []
    
    # Sample IPs to use
    src_ips = ["192.168.1.100", "192.168.1.101", "192.168.1.102", "10.0.0.50"]
    dst_ips = ["8.8.8.8", "1.1.1.1", "142.250.185.46", "104.21.24.40"]
    
    # Generate 100 sample packets with mixed protocols
    for i in range(100):
        src_ip = random.choice(src_ips)
        dst_ip = random.choice(dst_ips)
        
        # Mix of protocols
        protocol_choice = random.choice(['TCP', 'UDP', 'ICMP'])
        
        if protocol_choice == 'TCP':
            packet = IP(src=src_ip, dst=dst_ip) / TCP(dport=random.choice([80, 443, 22, 21]))
        elif protocol_choice == 'UDP':
            packet = IP(src=src_ip, dst=dst_ip) / UDP(dport=random.choice([53, 123, 67]))
        else:  # ICMP
            packet = IP(src=src_ip, dst=dst_ip) / ICMP()
        
        # Add some packets with payload
        if random.choice([True, False]):
            packet = packet / Raw(load=b"X" * random.randint(50, 500))
        
        packets.append(packet)
    
    # Save to file
    output_file = "example_traffic.pcap"
    wrpcap(output_file, packets)
    print(f"✅ Example data generated: {output_file}")
    print(f"   Generated {len(packets)} sample packets for testing")
    return output_file

if __name__ == "__main__":
    generate_example_packets()
