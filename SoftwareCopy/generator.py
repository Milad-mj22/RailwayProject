import os,cv2,random



encode_param = [int(cv2.IMWRITE_JPEG_LUMA_QUALITY), 80]


name = "1403-05-11_18-07-41-465097_11BG21_left"

img = cv2.imread(r'1403-05-11_18-07-41-465097_11BG21_left.jpeg')

main_path = 'test_data'



for year in range(1399,1403):

    for month in range(1,13):

        for day in range(1,29):

            path = "{}-{}-{}_{}-{}-{}-817020_11BG21_right.png".format(year,month,day,random.randint(0,23),random.randint(0,59),random.randint(0,59))



            new_path = os.path.join(main_path,path)

            cv2.imwrite(new_path,img,encode_param)