
import os,cv2,random,time
import numpy as np

def create_image(path):

    width, height = 800, 400

    if not os.path.exists(path):
        os.mkdir(path)

    for h in range(0,24):
        # if h<=9:
        #     str_h = '0'+str(h)
        # else:
        str_h = h

        if not os.path.exists(os.path.join(path,str(str_h))):
            os.mkdir(os.path.join(path,str(str_h)))
        for m in range(0,60):

            # if m<=9:
            #     str_m = '0'+str(m)
            # else:
            str_m = m

            int_random = random.randint(1,15)

            if int_random%3 == 0:
                continue

           
            if not os.path.exists(os.path.join(path,str(str_h),str(m))):
                os.mkdir(path=os.path.join(path,str(str_h),str(m)))
            new_path = os.path.join(path,str(str_h),str(m))


            for s in range(0,60):

                # if s<=9:
                #     str_s = '0'+str(s)
                # else:
                str_s = s







                image = np.zeros((height, width, 3), dtype=np.uint8)


                current_time = f'{str_h}_{str_m}_{str_s}'

                # Set font type, size, and color
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 4
                font_color = (
                    random.randint(0, 255),  # Red component
                    random.randint(0, 255),  # Green component
                    random.randint(70, 255)   # Blue component
                )
                font_thickness = 8

                # Get the text size
                text_size = cv2.getTextSize(current_time, font, font_scale, font_thickness)[0]

                # Calculate the text position to be centered
                text_x = (image.shape[1] - text_size[0]) // 2
                text_y = (image.shape[0] + text_size[1]) // 2

                # Add the time text to the image
                cv2.putText(image, current_time, (text_x, text_y), font, font_scale, font_color, font_thickness)

                # Save the image to a file
                output_path = f"{str_h}_{str_m}_{str_s}.png"
                cv2.imwrite(os.path.join(new_path,output_path), image)
                print(f"Image saved as {output_path}")


if __name__=='__main__':
    create_image(path = 'generate_images')