
# Network Traffic Analyzer Tool

A powerful Python-based network analysis tool with real-time traffic monitoring, machine learning anomaly detection, and interactive visualizations for comprehensive network security analysis.

**Built with:** Python · Scapy · scikit-learn · Matplotlib · Rich

---

## 🎯 Project Architecture

![Project Overview](Project%20overview%20—%20the%206%20capabilities%20in%20a%20hub-and-spoke%20layout.png)

---

## ✨ Key Features

- **🔍 Real-Time Network Traffic Monitoring** - Capture and analyze live packets dynamically
- **📊 Advanced Data Visualization** - Three built-in visualization types:
  - **IP Distribution Graph** - Top talkers and traffic patterns
  - **Protocol Distribution** - TCP/UDP/ICMP breakdown
  - **Network Pathway Graph** - Device connection mapping
- **🤖 Machine Learning Anomaly Detection** - Isolation Forest algorithm for threat detection
- **💾 Packet Capture & Storage** - Export to .pcap format for forensics
- **📈 Interactive Dashboard** - Multi-tab Rich interface for real-time analysis
- **🛡️ Security Focused** - Identify suspicious traffic patterns automatically

## Prerequisites

- Python 3.x
- Required Python packages:
  - scapy
  - psutil
  - colorama
  - requests
  - scikit-learn
  - matplotlib
  - rich

---

## 📥 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/trabelssi/network_analyzer_tool.git
   cd network_analyzer_tool
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure IPStack API**:
   - Sign up at [IPStack](https://ipstack.com/) for a free API key
   - Add your API key to `net_analyzer.py` (line 16):
   ```python
   IPSTACK_API_KEY = 'your_api_key_here'
   ```

---

## 🔄 How It Works

![Data Pipeline](Data%20pipeline%20—%20step-by-step%20flow%20from%20interface%20to%20output.png)

## 🤖 Anomaly Detection (Isolation Forest)

![Anomaly Detection](ML%20anomaly%20detection%20—%20how%20Isolation%20Forest%20works%20with%20your%20features.png)

The tool uses **unsupervised machine learning** to identify suspicious traffic patterns:
- **No labeled data required** - Works on raw network traffic
- **Real-time scoring** - Each packet analyzed live
- **Multi-feature detection** - Analyzes packet size, protocol, ports, IP behavior
- **Visual alerts** - Anomalies highlighted in the dashboard

---

## 📊 Visualizations

![Visualizations](3%20built-in%20visualizations%20—%20the%20bar%20chart%2C%20protocol%20donut%2C%20and%20network%20graph.png)

The tool generates three interactive charts:
1. **IP Distribution Bar Chart** - Identifies top talkers
2. **Protocol Breakdown Donut** - Shows TCP/UDP/ICMP ratios
3. **Network Pathway Graph** - Maps device connections and traffic flow

---

## 🚀 Quick Start

### Option 1: Live Network Traffic

```bash
sudo python net_analyzer.py
# Select network interface (e.g., eth0, wlan0)
# Enter number of packets to capture
# View real-time analysis and visualizations
```

### Option 2: Test with Example Data

```bash
python generate_example_data.py
# Generates 100 sample packets
python net_analyzer.py
# Load example_traffic.pcap for testing
```

---

## 📋 Example Workflow

```bash
$ sudo python net_analyzer.py
Available network interfaces:
  1. eth0
  2. wlan0
  
Select interface (1-2): 2
Enter number of packets to capture: 100
Capturing on wlan0...

Captured 100 packets
Do you want to save? (yes/no): yes
Filename: network_capture
✅ Saved to network_capture.pcap

Visualization Menu:
  1. IP Distribution
  2. Protocol Distribution
  3. Network Pathway
  4. Anomalies
  5. Exit
  
Select (1-5): 1
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Packet Capture** | Scapy |
| **ML Algorithm** | Scikit-learn (Isolation Forest) |
| **Visualization** | Matplotlib, NetworkX |
| **UI/Dashboard** | Rich |
| **Geo-Lookup** | IPStack API |
| **Language** | Python 3.x |

---

## 📂 Project Structure

```
network_analyzer_tool/
├── net_analyzer.py              # Main application
├── generate_example_data.py      # Example data generator
├── requirements.txt             # Dependencies
├── LICENSE                      # MIT License
└── README.md                    # This file
```

---

## 🎓 Use Cases

✅ **Network Security** - Detect DDoS attacks, port scans, exfil attempts  
✅ **Performance Monitoring** - Identify traffic bottlenecks  
✅ **Forensics** - Analyze captured traffic for incidents  
✅ **Learning** - Understand network protocols and ML applications  

---

## 📝 Example

Here is a brief example of running the tool:

```bash
$ sudo python net_analyzer.py
Available network interfaces:
eth0
wlan0
Enter the name of the network interface you want to capture traffic on: wlan0
Enter the number of packets to capture: 100
Analyzing traffic on wlan0...
...
Do you want to save the captured packets? (yes/no): yes
Enter the output file name for the captured packets (without extension): capture
Captured packets saved to capture.pcap

Visualization Options:
1. IP Distribution
2. Protocol Distribution
3. Packet Length Distribution
4. Anomalies
5. Exit
Enter your choice: 1
```

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Amine Trabelssi**

- GitHub: [@trabelssi](https://github.com/trabelssi)
- Project: [network_analyzer_tool](https://github.com/trabelssi/network_analyzer_tool)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

## 🙏 Acknowledgments

- Built with [Scapy](https://scapy.net/) for packet manipulation
- Machine learning powered by [scikit-learn](scikit-learn.org/)
- Rich dashboard using [Rich](https://rich.readthedocs.io/)
- Geolocation via [IPStack](https://ipstack.com/)
