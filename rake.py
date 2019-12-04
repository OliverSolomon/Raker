#!/usr/bin/python3
"""webscrapper for the jumia site(phones & Tablets section)"""
from bs4 import BeautifulSoup
from requests import get
import os

#checks if there is a jumia.txt file and deletes it(ensuring new data is created every time)
for i in os.listdir():
	if i == 'jumia.txt':
		print("\nYou have a file with the results of an earlier scrap")
		os.remove('jumia.txt')
		print("\tFile has been deleted successfully.")
	else:
		pass

url = 'https://www.jumia.co.ke/phones-tablets/all-products/?page=1'

def rake():
	print("you can take a cup of coffee to weather the short 3 minute wait\n")
	print("\tResults will be posted to a 'jumia.txt' file\n")
	#loop generates new url's to facilitate scrapping through multiple pages
	for j in range(1,30):
		#empty list variable
		links,discounts,specs,prices,brands=[],[],[],[],[]
		url_num = url.replace(url[-1], str(j))
		response = get(url_num)

		#print(response.text[:500])# prints out sample code from site to see if we're on the right track
		html_soup = BeautifulSoup(response.text, 'html.parser')

		#finds all instances of the brand
		for brands_found in html_soup.find_all('span', class_= 'brand'):
			brands.append(brands_found)
		#finds all instances of specs found
		for specs_found in html_soup.find_all('span', class_="name"):
			specs.append(specs_found)
		#price
		for price in html_soup.find_all('span', class_="price"):
			prices.append(price)

		for discount in html_soup.find_all('span', class_ = "sale-flag-percent"):
			discounts.append(discount)
		#link to device
		for link in html_soup.find_all('a', class_= 'link'):
			links.append(link['href'])

		#writes data into text file for analysis
		for i in range(len(discounts)):
			data = brands[i].text  + ":\t\t" + discounts[i].text + ":\t\t\t" + prices[i].text + ":\t\t\t\t" + specs[i].text + ":\t\t\t\t" + links[i]
			with open('jumia.txt','a') as f:
				f.write(data + "\n" )
				f.close()
	print("Scrapping completed successfully!\n\tAbout " + str(len(discounts)* 30) + " Results found.\n")

rake()