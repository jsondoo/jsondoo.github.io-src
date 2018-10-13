# About

Source code for generating static files for [my site](https://jdoo.ca)

Powered by Pelican.

## Testing Locally
```
pelican content                       # generate static files
cd output && python -m pelican.server # localhost:8000
```

## Deploying 

Generate content into your submodule then push the changes in your submodule.
```
pelican content -s publishconf.py     # generate static files for production
cd output
git add -A
git commit -m "commit msg"
git push
```