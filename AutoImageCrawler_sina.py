import os
import urllib2
from sgmllib import SGMLParser

#Parameters

imagesPath = 'images_sina/'
site_path = 'http://photo.auto.sina.com.cn'
href_prefix = '/picture/'
char_download = '\xcf\xc2\xd4\xd8\xb8\xdf\xc7\xe5\xcd\xbc'
addr_suffixs = ['/1_1.html','/5_1.html','/7_1.html','/9_1.html']

site_addr = 'http://data.auto.sina.com.cn/'

timeout = 30


#Exception logs
markLogName = 'Exception_mark.txt'
imageLogName = 'Exception_image.txt'
markLog = open(markLogName,'w')
imageLog = open(imageLogName,'w')


#Parsers and downloader

class MarkList(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.list = []
		self.count = 0
	def start_a(self, attrs):
		autolog = [v for k, v in attrs if k=="autolog"]
		if len(autolog)>0:
			autolog = autolog[0]
		else:
			autolog = -1
		href = [v for k, v in attrs if k=="href"]
		title = [v for k, v in attrs if k=="title"]
		if autolog == '14' and title and href:
			self.count += 1;
			pair = {'num':self.count,'title':title[0],'href':href[0]}
			self.list.append(pair)

class ImageList(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.list = []
		self.count = 0
	def start_a(self, attrs):
		href = [v for k, v in attrs if k=="href"]
		for c in href:
			if (href_prefix in c):
				self.count += 1;
				self.list.append(c)

class DownloadFinder(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_a = ""
		self.href = ""
		self.list = []
	def start_a(self, attrs):
		self.is_a = 1
		self.href = [v for k, v in attrs if k=="href"]
	def end_a(self):
		self.is_a = ""
		self.href = ""
	def handle_data(self,text):
		if self.is_a ==1 and char_download in text:
			self.list.extend(self.href)

def downloadImage(address,savePath):
	splitPath = address.split('/')
	name = splitPath.pop()
	filepath = savePath+name
	url = urllib2.urlopen(address,None,timeout)
	image = url.read()
	file = open(filepath,'wb')
	file.write(image)
	url.close()
	file.close()


	
	
#Parsing the whole database: http://db.auto.sohu.com/

url1 = urllib2.urlopen(site_addr,None,timeout)
content1 = url1.read()
marklist = MarkList()
marklist.feed(content1)
url1.close()
#save
#filename = "marklist.txt"
#target = open(filename, 'w')
#target.truncate()
#target.write(str(marklist.list))




#Parsing every auto mark in the database

for mark in marklist.list:
	id = mark['num']
	title = mark['title']
	
	if id>=169:
		#Making directory for downloaded images
		savePath = imagesPath+str(id)+" "+title+"/"
		if not os.path.exists(savePath):
			os.makedirs(savePath)
		
		#Finding all images of a certain mark
		addr = mark['href']+'/1_1.html'
		#Dealing with exceptions
		try:
			url2 = urllib2.urlopen(addr,None,timeout)
			content2 = url2.read()
			imagelist = ImageList()
			imagelist.feed(content2)
			url2.close()

			
			#Downloading every image
			
			for href in imagelist.list:
				fullhref = site_path+href
				#Dealing with exceptions
				try:
					url3 = urllib2.urlopen(fullhref,None,timeout)
					content3 = url3.read()
					dlFinder = DownloadFinder()
					dlFinder.feed(content3)
					url3.close()
					if dlFinder.list:
						downloadImage(dlFinder.list[0],savePath)
						print savePath+"    "+dlFinder.list[0]
				except Exception as err:
					print err
					print fullhref,dlFinder.list[0],savePath
					imageLog.writelines(dlFinder.list[0]+'@'+savePath)
					pass
			
		except Exception as err:
			print err
			print addr
			markLog.writelines(addr)
			pass
			
			
		#Finding all images of a certain mark
		addr = mark['href']+'/5_1.html'
		#Dealing with exceptions
		try:
			url2 = urllib2.urlopen(addr,None,timeout)
			content2 = url2.read()
			imagelist = ImageList()
			imagelist.feed(content2)
			url2.close()

			
			#Downloading every image
			
			for href in imagelist.list:
				fullhref = site_path+href
				#Dealing with exceptions
				try:
					url3 = urllib2.urlopen(fullhref,None,timeout)
					content3 = url3.read()
					dlFinder = DownloadFinder()
					dlFinder.feed(content3)
					url3.close()
					if dlFinder.list:
						downloadImage(dlFinder.list[0],savePath)
						print savePath+"    "+dlFinder.list[0]
				except Exception as err:
					print err
					print fullhref,dlFinder.list[0],savePath
					imageLog.writelines(dlFinder.list[0]+'@'+savePath)
					pass
					
		except Exception as err:
			print err
			print addr
			markLog.writelines(addr)
			pass
					
			
			
		#Finding all images of a certain mark
		addr = mark['href']+'/7_1.html'
		#Dealing with exceptions
		try:
			url2 = urllib2.urlopen(addr,None,timeout)
			content2 = url2.read()
			imagelist = ImageList()
			imagelist.feed(content2)
			url2.close()

			
			#Downloading every image
			
			for href in imagelist.list:
				fullhref = site_path+href
				#Dealing with exceptions
				try:
					url3 = urllib2.urlopen(fullhref,None,timeout)
					content3 = url3.read()
					dlFinder = DownloadFinder()
					dlFinder.feed(content3)
					url3.close()
					if dlFinder.list:
						downloadImage(dlFinder.list[0],savePath)
						print savePath+"    "+dlFinder.list[0]
				except Exception as err:
					print err
					print fullhref,dlFinder.list[0],savePath
					imageLog.writelines(dlFinder.list[0]+'@'+savePath)
					pass
					
		except Exception as err:
			print err
			print addr
			markLog.writelines(addr)
			pass

					
					
					
		#Finding all images of a certain mark
		addr = mark['href']+'/9_1.html'
		#Dealing with exceptions
		try:
			url2 = urllib2.urlopen(addr,None,timeout)
			content2 = url2.read()
			imagelist = ImageList()
			imagelist.feed(content2)
			url2.close()

			
			#Downloading every image
			
			for href in imagelist.list:
				fullhref = site_path+href
				#Dealing with exceptions
				try:
					url3 = urllib2.urlopen(fullhref,None,timeout)
					content3 = url3.read()
					dlFinder = DownloadFinder()
					dlFinder.feed(content3)
					url3.close()
					if dlFinder.list:
						downloadImage(dlFinder.list[0],savePath)
						print savePath+"    "+dlFinder.list[0]
				except Exception as err:
					print err
					print fullhref,dlFinder.list[0],savePath
					imageLog.writelines(dlFinder.list[0]+'@'+savePath)
					pass
						
		except Exception as err:
			print err
			print addr
			markLog.writelines(addr)
			pass
	

markLog.close()
imageLog.close()