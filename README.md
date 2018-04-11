# Source for http://matthewkudija.com/pelican

This repository contains the source for http://matthewkudija.com/pelican/.

## Building the Blog

Clone the repository & make sure submodules are included

```
$ git clone https://github.com/mkudija/blog.git
$ git submodule update --init --recursive
```

Install the required packages:

```
$ conda create -n pelican-blog python=3.5 jupyter notebook
$ source activate pelican-blog
```

Build the html:

```
$ make publish
```
