# dita-tools
DITA tools

# Installation

## Environment

Assuming a working installation of Python 3.
```
pip install --upgrade pip
pip install --upgrade virtualenv
virtualenv -p /path/to/python3/python3 env
source env/bin/activate
```

## Setup

```
pip install -r reqs
```

## Running
Don't forget to run this once:
```
source env/bin/activate
```

To generate a single page:
```
python dita2html.py data/dita/content/authoring/emm1405090779098.ditamap data/PayZen.ditaval > out.html
```

To make a set of "Markdown" files for use in Jekyll:
```
python dita2html.py data/dita/content/authoring/emm1405090779098.ditamap data/PayZen.ditaval out_files
```
