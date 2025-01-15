# Madflavas Weather App: Flava of the Day

## Overview
Madflavas Weather App is a Python application that provides daily weather updates with a unique twist. Each day, users receive a "Flava of the Day" that highlights a specific weather condition or feature, making weather updates more engaging and fun.

## Features
- Daily weather updates
- "Flava of the Day" highlighting unique weather conditions
- User-friendly interface

## Prequisites for Windows and Powershell
1 Installation of Tools
1.1 Install Python
Install python from this link: [Python Installation](https://www.python.org/ftp/python/3.13.1/python-3.13.1-amd64.exe)

Confirm python installation by running:
````
python --version
````
confirm pip has also been installed with this command:
````
pip --version
````
1.2 Create Your AWS Account and download the AWS CLI
Create your AWS Account by visiting the AWS Free Tier Signup Page and click create account

Create an IAM user by going to the IAM Section and click create user

Generate credentials for the user, and copy the Secret Key and Access Key

Download the AWS CLI from this link : Amazon CLI Install Page
Run the command to configure your aws cli:
````
aws configure
````
Input your access and secret key
Enter your default region; preferably us-east-1
Set your default output format to json

2 Workflow
2.1 Get OpenWeather API Key

Get the OpenWeather API Key by signing up to this page: OpenWeatherAPI
Once logged in, navigate to API Keys and generate a new key. Copy the generated key.

2.2 Set up Project Directory

Create the Structure for the Project
````
mkdir weather-dashboard
cd weather-dashboard
mkdir src tests data
New-Item -Path "src/__init__.py" -ItemType file
New-Item -Path "src/weather_dashboard.py" -ItemType file
echo ".env" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.zip" >> .gitignore
echo "boto3==1.26.137" >> requirements.txt 
echo "python-dotenv==1.0.0" >> requirements.txt 
echo "requests==2.28.2" >> requirements.txt
````



## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/tarran-ivory/madflavas-weather-app.git
   ```
2. Navigate to the project directory:
   ```
   cd madflavas-weather-app
   ```
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```
Visit `http://localhost:5000` in your web browser to access the app.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
