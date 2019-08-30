from myFunction import set1,set0,get_bit,get_xor,txt_to_bin,bin_to_txt,get_pos_array
import cv2


txt_bit = txt_to_bin("hello dhrubo")
txt_ln = len(txt_bit)


pos_array = get_pos_array("password")
pa_ln = len(pos_array)



image = cv2.imread("e.png")
h,w,ch = image.shape



msb_p = 8
txt_b_cntr = 0
pss_a_cntr = 0
flag = True


for x in range(0,w):
    for y in range(0,h):
        pix_num = image[y,x][0]
        if get_bit(pix_num,msb_p) == 1:     #------- filtering

            t_b = txt_bit[txt_b_cntr]       #------- get text bit
            t_b = ord(t_b) - ord('0')


            p = pos_array[pss_a_cntr]       #------- get position
            pss_a_cntr += 1
            if pss_a_cntr == pa_ln:
                pss_a_cntr = 0
                

            im_b = get_bit(pix_num,p+1)     #------ get pixel position bit
            
            xor_b = get_xor(im_b,t_b)       #------ xor txt_bit and img_bit
            
            
            if xor_b == True:               #------- store bit to LSB
                bval = set1(pix_num,1)
            else:
                bval = set0(pix_num,1)

            image[y,x][0] = bval



            txt_b_cntr += 1
            if txt_b_cntr >= txt_ln:
                flag = False
                break

    if flag == False:
        break

            
cv2.imwrite('output.png', image)
