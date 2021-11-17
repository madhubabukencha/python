import re

text = '''
Remcos is a RAT type malware which means that attackers use it to perform
actions on infected machines remotely. This malware is extremely actively
caped up to date with updates coming out almost every single month. 
Our analysis are tagged as Remcos_34q5t, Remcos_d43rf, Remcos_sdw32, Remcos_bvd21
obtaining the unique following indicators: indicator1[.]com, 1[.]1[.]1[.]1,
hxxps[:]//indicator1[.]com/malicious.docx
Remcos RAT is a dangerous trojan available to attackers for a relatively
inexpensive price.
'''

# Brief explanation:
# re.findall(r"for names| for ip | for url | for domain", text)
indicators = re.findall(r'[A-Za-z]*_[a-z1-9A-Z]*|'
                        r'[1-9]\[\.\][1-9]\[\.\][1-9]\[\.\][1-9]|'
                        r'[\:\[\]\/\/a-z1-9]*\[\.\]com\/[a-z]*\.[a-z]*|'
                        r'[a-zA-Z1-9]*\[\.\]com', text)
print(indicators)
