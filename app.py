from flask import Flask, render_template, request,send_from_directory
from utils import youtube_down
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form.get('link')
        print("aaaaaaa",link)
        if link:
            try:
                print("downloading inside try")
                pwd=os.getcwd()
                videos_folder = os.path.join(pwd, 'static','videos')
                try:
                    print(os.listdir(videos_folder))
                except Exception as e:
                    print("error",e)
                for file_name in os.listdir(videos_folder):


                    # remove all files in the videos folder
                    file_path = os.path.join(videos_folder, file_name)
                    # os.remove(file_path)
                print("removed")
                video_title=youtube_down(link)
                message = f"Downloaded '{video_title}' successfully!"
            except Exception as e:
                message = f"An error occurred: {str(e)}"
        else:
            message = "Please enter a valid YouTube link."
        print("downloaded")
        return render_template('index.html', message=message,video_file=video_title)
    
    return render_template('index.html')



@app.route('/videos/<path:filename>')
def download_file(filename):
    # /algorithms%20and%20programming:%20simple%20gcd
    print("filename",filename)
    file=filename+".webm"
    return send_from_directory('static/videos', file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
