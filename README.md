# ARP-Spoofer

This tool is used for ARP Spoofing and to intercept communication between network devices.


# Information
This tool is for educational purpose only, usage of arp spoofer for attacking targets without prior mutual consent is illegal. Developer assume no liability and is not responsible for any misuse or damage cause by this program.

# Download 
	
	git clone https://github.com/inavedanjum/arp-spoofer.git
	cd arp-spoofer
	chmod +x network_scanner.py
	
# Usage
	
	python3 arp_spoofer.py -t <target> -s <spoofip>
                        or 
	python3 arp_spoofer.py --targetip <target> --spoofip <spoofip>

	example:
	python3 arp_spoofer.py -t 10.1.1.7 -s 10.1.1.1
	

# Install Modules 

	pip3 install -r requirements.txt
