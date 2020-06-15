import requests
import os


# define stickers name for folder
stick_name = input("Sticker pack name: ")

# give fitst id of sticker in pack 
fstick_id = int(input("First stickers id: "))

# give count of stickers in pack
stick_count = int(input("Enter sticker count: "))



# make dir for stickers 
os.system('mkdir ./{}'.format(stick_name))


for i in range(fstick_id, stick_count+1):
	response = requests.get(("https://vk.com/sticker/1-" + str(i) + "-512"))
	
	file = open(('./{}/'.format(stick_name) + str(i) + ".png"), 'wb')
	file.write(response.content)
	file.close()
	print('{}, done!'.format(i)) # remove if you dont want see the progress
