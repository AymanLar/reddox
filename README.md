# reddox
<center><img src="assets/reddox.png" alt="reddox"></center>

## Get your subreddit posts documented in markdown and pdf automatically 🤖
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

Reddox is a tool to convert subreddit posts to a markdown file (to a pdf file)

[Tuto](https://i.imgur.com/bQWbzvq.gifv)

## Requirements
```
git clone git@github.com:Ayman-s-Lab/reddox.git
cd reddox/
pip install -r requirements.txt
```
### Usage
```bash
python redox.py
grip reddit.md
```
`grip` will render the markdown on **localhost** ... - just edit away and refresh the browser. Save as PDF ready 🚀.

# Here we Have other ways to convert markdown to PDF:

Here they are several methods for converting a Markdown (.md) formatted file to PDF, from UNIX or Linux machines.

- Using ```Pandoc```:
```bash
$ reddit.md -s -o posts.pdf
```
we still recommend to use `grip` to display markdown in the browser and then "Save as PDF" option in the Print dialog (for chrome based browsers), because it's lighter weight than installing LaTeX (required by pandoc for pdf generation).

- Using `node.js` based markdown-pdf`:
```bash
npm install -g markdown-pdf
markdown-pdf /path/to/markdown
```

![ayman](/assets/nwh.png)
