# Python_projects

This files contain all the projects on Python programmming language I made during my python journey 

## [1]. Automated Youtube Video Downloader 

   ### 1. Made a auutomated youtube video downloader sing the tkinter library and importing youtube and filedialog function
   ### 2. it takes a url of a video, an da path location where the video needs to be saved, url is typed manually in terminal while the path location is selected by instantiating a tkinter window (root) firstly
   ### 3. YouTube is used to define the url , to download the best quality of stream we use  and to get download resolution 
         [stream = yt_vid.streams.filter(progressive=True,file_extension="mp4")]
         
   ### 4. and to download best resolution video -: 
         [highest_res_stream = stream.get_highest_resolution()]
         [highest_res_stream.download(output_path=path)]
         
   ### 5. def open_file_save(): is used to define file location using tkinter window
   ### 6. And then the program is ruun and videos are downloaded to the location successfully (might tae few  min if wifi speed is low)

## [2.] Randomized Maths Quiz Generator

   ### 1. Made a randomized Math's question generator, using operations like '+','-','*','/'
   ### 2. User will input how many questions need to be generated and the program will detect and return if the answer is correct or not.
   ### 3. It also has a time tracker, if the questions aren't solved within given time you will fail the quiz 

## [3.] QR Code Generator 

   ### 1. the library of qrcode is imported using command : pip install qrcode
   ### 2. we take data as a url of the website we need to generate qr of as input and pass to def gen_QR(data)
   ### 3. in def gen_QR(data) we set a qr code named qr and describe it's version,size,border size. Then tthe data is added into it and and image is made using qr.make_image() where it's background and foreground colors are                  selected.
       
