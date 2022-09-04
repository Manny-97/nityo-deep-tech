# Extract Table

Code to extract text from images
Run the following command to change directory
```
cd text-extract
```
Run to create virtual environment
```
python3 -m venv venv
``` 
Run the following command to activate virtual environment
```
source venv/bin/activate 
```
Run the following command to install dependencies
```
pip install -r requirements.txt
```
Run the following to activate virtual environment
```
source venv/bin/activate    - for Mac
source venv/Scripts/activate   - for Windows
```

If you encounter file not found error as below:
```
FileNotFoundError: [Errno 2] No such file or directory:
```

Run the following command
```
brew install ghostscript
```

Run the following command to execute the script
```
python processor.py
```