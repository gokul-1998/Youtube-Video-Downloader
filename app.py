from flask import Flask, render_template, request
from pytube import YouTube
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form.get('link')
        if link:
            try:
                videos_folder = 'static/videos'
                for file_name in os.listdir(videos_folder):
                    if file_name.endswith(".mp4"):
                        file_path = os.path.join(videos_folder, file_name)
                        os.remove(file_path)
                yt = YouTube(link)
                stream = yt.streams.get_highest_resolution()
                video_title = yt.title+".mp4"
                print(video_title)
                video_title = yt.title.replace('|', '-') + ".mp4"
                print(video_title)
                stream.download('static/videos',filename=video_title)
                # to set a filename, insert the filename in the download() function

                # to download in a specific folder, insert the folder name in the download() function
                # stream.download('folder_name')

                message = f"Downloaded '{video_title}' successfully!"
            except Exception as e:
                message = f"An error occurred: {str(e)}"
        else:
            message = "Please enter a valid YouTube link."
        print("downloaded")
        return render_template('index.html', message=message,video_file=video_title)
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
