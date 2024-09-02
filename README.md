# UploadVault 🔒

UploadVault is a secure web application that allows users to upload and save their files on another computer easily. The application provides a simple interface for uploading files, viewing uploaded files, and downloading them when needed. 

## Table of Contents
- [Screenshots](#screenshots)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)


## Screenshots

<img width="400" alt="Screenshot 2024-09-01 at 8 11 13 PM" src="https://github.com/user-attachments/assets/3d9cd04b-39fc-4c80-8528-23431802aff2">
<img width="400" alt="Screenshot 2024-09-01 at 8 11 27 PM" src="https://github.com/user-attachments/assets/a0e159f2-ee7f-4d96-8417-2f7bbe9899ce">

## Features
- **Drag & Drop File Upload:** A seamless drag-and-drop interface for file uploads.
- **File Viewing and Downloading:** Users can view a list of uploaded files and download them securely.
- **Password Protection:** Access to files is protected with a password prompt to ensure only authorized users can view them.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/junaid-mahmood/UploadVault.git
   cd UploadVault
   pip install -r requirements.txt

## Usage

1.
```
  python3 app.py
```
2. Navigate to localhost:5000 or 127.0.0.1:5000


## Files and Structure

- **index.html:** Main page for uploading files with drag-and-drop functionality.
- **view_files.html:** Page displaying the list of files on the server, with options to download.
- **password_prompt.html:** Password input page to protect access to the file viewer.
- **app.py:** Backend script handling file uploads, security, and routing.





