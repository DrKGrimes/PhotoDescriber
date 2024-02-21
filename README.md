# PhotoDescriber
A simple script that uses OpenAI API to describe photos in a folder and produces a JSON file with output.

## Requirements
The only external package required by the script is REQUESTS, as base64, os, and json are part of the Python Standard Library and do not need to be installed separately. The requests library is used for making HTTP requests to the OpenAI API.

To install the packages listed in requirements.txt, run the following command in your terminal:

``` pip install -r requirements.txt ```

This will ensure that the requests library is installed in your environment, allowing the script to run successfully.

## API Key
You will need an OpenAI API key to run this script. This can be obtained from your OpenAI account.

The api key is read from a .env file. If you do not have one, create it. The format is as follows:

``` OPENAI_API_KEY=INSERT_API_KEY_HERE ```

## Instructions
Place all images you want a description for in the /Pictures folder

Run the script

```python3 photodescriber.py

This might take a moment or two to run. When complete, you will have a new file, image_descriptions.json, which will contain the descriptions

## Warning
Running image analysis can be costly! Be sure to check that you have sufficient funds to run this script. You bear all the responsibilities for the costs you incur
