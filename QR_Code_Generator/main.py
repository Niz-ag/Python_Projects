import qrcode
import os
relative_path= os.path.dirname(os.path.realpath(__file__))
class QR_Code:
    
    def __init__(self,size:int,padding:int) -> None:
        self.qr= qrcode.QRCode(box_size=size, border=padding)
    
    def Generate_QR(self,filename:str,fg:str,bg:str):
        self.User_input = str(input("Enter the content\n"))
        try:
            self.qr.add_data(self.User_input)
            qr_image =self.qr.make_image(fill_color=fg,back_color=bg) 
            qr_image.save(f"{relative_path}/{filename}")
            print(f"successfully created your QR Code!")
        except Exception as e:
            print(f"Error: {e}")
user=QR_Code(100,2)
user.Generate_QR("QR_Code.jpg",'black','white')
file_name:str= user.User_input[:user.User_input.find('/')]
print(file_name)

os.rename(f"{relative_path}/QR_Code.jpg",f"{relative_path}\\{file_name}.jpg")
