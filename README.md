# Midwest Radio Death Notices Python
This is a python program I made for getting the obituaries from midwestradio.ie
I created this as a test for a mycroft.ai skill I wanted to create to get obituaries
from a website. This is part of a couple of ideas I have to create mycroft skills to
assist elderly people and make mycroft more accessable to a usually non-tech audience.

# Requirements
- Python 3.x
- Pyttsx3

# Installation
```bash
git clone https://github.com/RyanJennings1/midwest-death-notices-python.git
```

```python
sudo pip3 install pyttsx3
```

## Pyttsx3
To include speech functionality in python install pyttsx3

## USAGE
```
python3 main.py [parameter]

Parameters:
    --help              - Display this menu
    -v, --version       - Display version number
    --speech            - Text to speech obituaries
```

## IDEAS TO IMPLEMENT
* Ability to pause speech during talking
* Ability to repeat what was said
* Ability to repeat a specific name
