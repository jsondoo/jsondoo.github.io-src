# About

Source code for generating static files for [my site](https://jdoo.ca)

Powered by Pelican.

```
pelican content                       # generate static files
cd output && python -m pelican.server # localhost:8000
pelican content -s publishconf.py     # generate static files for production
```