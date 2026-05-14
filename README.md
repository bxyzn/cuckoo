# Cuckoo

A lightweight remote to control media, works through a website hosted locally through python

## Features
- Website/Remote accessible by any device in the network
- No additional apps required
- Can manage all media being run on the local machine

## Getting started
### Prerequisites
- playerctl
Playerctl is a lightweight media control daemon for debian based linux operating systems
- Python3
-Python-Flask: to host the site

*Installation* :
```
sudo apt update && sudo apt install playerctl python3 python3-flask
git clone https://github.com/bxyzn/cuckoo
cd cuckoo
python3 app.py

```

The project is open-source, feel free to modify to your liking or suggesting changes

- The website template is stored inside ./cuckoo/templates
- Remember when using flask, to link other local scripts or css files, create a folder called static and store them inside that

```
cuckoo
|
|-app.py
|-templates
    |-index.html
|-static //create static folder inside the cuckoo folder
    |-style
        |-css files
    |-js
        |-js files

```

-instead of `src='script.js` use `src="{{ url_for('static', filename='js/script.js') }}" ` for css and `src="{{ url_for('static', filename='js/script.js') }}" ` for js
