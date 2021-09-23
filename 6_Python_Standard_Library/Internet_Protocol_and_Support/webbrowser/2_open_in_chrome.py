"""
This program shows how to change a default browser while
opening a web page
"""
import webbrowser


website_url = "https://www.python.org"
sec_url = "https://www.programiz.com/python-programming"

# Chrome exe path
chrome_exe = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

# Register to avail web browser issues
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_exe))
webbrowser.get('chrome').open(website_url)

# To open url in new tab
webbrowser.get('chrome').open_new_tab(sec_url)