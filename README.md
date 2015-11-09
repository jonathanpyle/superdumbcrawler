# superdumbcrawler
Site crawler written in python 2.7.5.

- Takes 2 arguments from command line - URL to crawl and optional --debug flag.
- Crawls all links to pages within the same FQDN as the supplied URL.
- Outputs a simple list of all internal and external links encountered during the crawl.
- Output is sent to stdout

# Example usage
python superdumbcrawler.py --debug http://wiprodigital.com

# Installation/Setup Notes
- Requires python 2.7 and lxml library. 
- Ensure 'python 2.7' and 'pip' are installed with your system's package manager (e.g. 'sudo apt-get -y install python-pip')
- To add the required lxml library, 'sudo pip install lxml'

# Limitations
- Ignores frames and iframes
- Uses naive lxml document encoding guesses
- HTTPS supported but very little testing conducted
- Output is a simple list, not a proper sitemap.xml

