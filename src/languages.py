from operator import itemgetter
import collections, urllib, tldextract, re, logging

logging.basicConfig()

lang = []
tlds = []
domains = []
langtlds = []
langdomains = []

#Takes a list and turns it into a dictionary of counts
def make_counter(data):
	count = collections.Counter()
	for item in data:
		count[item] += 1
	count_list = []
	for key in count:
		count_list.append([key,count[key]])
	count_list=sorted(count_list, key=itemgetter(1),reverse=True)
	return count_list

#Takes a dictionary and turns it into a tsv
def write_counter(data,name):
	path = '../Output/' + name + '.tsv'
	with open(path,'wb') as f:
		for item in data:
			if isinstance(item[0],str):
				row = item[0] + '\t' + str(item[1]) + '\n'
			else:
				row = item[0][0] + '\t' +item[0][1] + '\t'+str(item[1]) + '\n'
			f.write(row)

# This bit takes forever and a half, don't run it
# Opens every url from the source and returns a file of the redirect links
'''
# Tracking/Progress code for when this inevitably breaks
i=
with open('../Output/links_source.tsv','r') as f:
	for row in f:
		try:
			print row
			link = urllib.urlopen(row).geturl()
			urllib.urlopen(row).close()
			links.append(link)
		except:
			links.append('')
			print i

with open('../Output/links.txt','a') as f:
	for item in links:
		f.write(item)
		f.write('\n')
		links = []
'''

# Process the links for lanuages, TLDs, and domains, then make some big ol' lists
with open('../Output/links.txt','r') as f:
	for row in f:
		row = row.rstrip('\n')
		if re.search('translate',row):
			lang_code=row[-2:]
			if re.search(r'news\.google',row):
				url_match = re.search(r'%3D(http.+)',row)
			else:
				url_match = re.search(r'=(http.+)',row)
			url = urllib.unquote(url_match.group(1))
			tldextract.extract(url).tld,tldextract.extract(url).domain
		else:
			lang_code='en'
			tld = tldextract.extract(row).tld
			domain = tldextract.extract(row).domain
		lang.append(lang_code)
		tlds.append(tld)
		domains.append(domain)
		langtlds.append((lang_code,tld))
		langdomains.append((lang_code,domain))
			
# Make all the dictionaries and tsv's
lang_list = make_counter(lang)
write_counter(lang_list,'languages')
url_count = make_counter(tlds)
write_counter(url_count,'TLDs')
domain_count = make_counter(domains)
write_counter(domain_count,'domains')
langtlds_count = make_counter(langtlds)
write_counter(langtlds_count,'langtlds')
langdomains_count = make_counter(langdomains)
write_counter(langdomains_count,'langdomains')

