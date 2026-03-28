(base) phani@Gnanendras-MacBook-Pro 10FASTAPI_examples % python -m venv ml_fast_api
(base) phani@Gnanendras-MacBook-Pro 10FASTAPI_examples % source ml_fast_api/bin/activate
(ml_fast_api) (base) phani@Gnanendras-MacBook-Pro 10FASTAPI_examples % pip install -r requirements.txt 

How to run fastapi ap:

Without host and port:

If code under if __name__=='__main__':  is 
uvicorn.run(debug=True)
In terminal:
python -m uvicorn <filename>:app
python -m uvicorn california_app_fast_api:app

If code is:
uvicorn.run(app,host="0.0.0.0",port=8000)
In terminal:
python -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload


By default, FASTAPI will run on below ports
127.0.0.1:8000





Flask is a webframework
Flask is used to get end points for the application
to trigger in webbrowser

Example:
We can create a function and print the functionoutput in terminal
-------------------------------------------------------------------------------
Now we will create functions, now this this function will generate endpoints.
That endpoints will trigger in webbrowser to display the output.
===============================================================================
package:Flask
pip install Flask
Run following command in mac terinal:
pip install -r requirements.txt
===============================================================================
Task: ex1.py === convert into application using flask
We want to see output of ex1.py in web browser
===============================================================================
# Create virtual environment
python -m venv ml_flasl
# To activate virtual environment
Win:
ml_flask\Scripts\activate
Mac Terminal:
source ml_flask/bin/activate
# Run the following after (ml_flask) appears next to base (in Mac) or (ml_flask) appears next to. C:\Users\omkar\ (in Windows terminal)
pip install -r ml_flask_requirements.txt
# run the command
python lr_california_flask.py