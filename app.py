from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form.get('link')
        if link:
            try:
                yt = YouTube(link)
                stream = yt.streams.get_highest_resolution()
                video_title = yt.title
                stream.download('static/videos')
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
