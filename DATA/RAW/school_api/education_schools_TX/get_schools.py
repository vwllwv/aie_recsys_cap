import os

num_pages = 206 # 50 schools per page

for i in range(1,num_pages+1):
	print("Get Page "+ str(i).zfill(3) )
	try:
		os.system("curl -X GET --header 'Accept: application/json' 'https://api.schooldigger.com/v1.2/schools?st=TX&page=" + str(i) + "&perPage=50&appID=7944558b&appKey=2d946c1dffd5b40801713f40c98d1ce4' -o schools" + str(i).zfill(3) + ".json")
	except:
		print("Error: cannot get page "+str(i))