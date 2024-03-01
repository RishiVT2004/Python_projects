# Python_projects

This files contain all the projects on Python programmming language I mad eduring my python journey 

## [1]. Youtube Video Downloader 
   ### 1. Made a auutomated youtube video downloader sing the tkinter library and importing youtube and filedialog function
   ### 2. it takes a url of a video, an da path location where the video needs to be saved, url is typed manually in terminal while the path location is selected by instantiating a tkinter window (root) firstly
   ### 3. YouTube is used to define the url , to download the best quality of stream we use  and to get download resolution 
         [stream = yt_vid.streams.filter(progressive=True,file_extension="mp4")]
         
   ### 4. and to download best resolution video -: 
         [highest_res_stream = stream.get_highest_resolution()]
         [highest_res_stream.download(output_path=path)]
         
   ### 5. def open_file_save(): is used to define file location using tkinter window
   ### 6. And then the program is ruun and videos are downloaded to the location successfully (might tae few  min if wifi speed is low)
