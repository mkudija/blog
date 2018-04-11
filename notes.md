# Notes on creating the blog

```
$ conda create -n pelican-blog python=3.5 jupyter notebook
$ source activate pelican-blog
$ pip install pelican
$ pip install Markdown
$ pelican-quickstart
$ git submodule add git://github.com/danielfrg/pelican-ipynb.git plugins/ipynb
$ git submodule add git://github.com/getpelican/pelican-plugins.git plugins/pelican-plugins
```

Theme from here: http://jakevdp.github.io/ and http://danielfrg.com/

Output to `docs/` for gh-pages


## Code Highlighting

### Option 1: syntax-highlighting
- http://docs.getpelican.com/en/3.6.3/faq.html?highlight=syntax%20highlighting
- `pygmentize -S monokai -f html -a .highlight > pygment.css`
- save that file to /Users/matthewkudija/Documents/GitHub/blog/theme/templates/pygments.css
- add this code block to the top of `/Users/matthewkudija/Documents/GitHub/blog/theme/templates/main.css`:
```css
.highlight pre, .highlighttable pre {
    background: #272822;
    color: #f8f8f2;
}
```


### Option 2: https://github.com/gilsondev/pelican-clean-blog
- modify base.html with this at ~line 59:

```html
 <!-- Code highlight color scheme -->
    <!-- FROM HERE: https://github.com/gilsondev/pelican-clean-blog -->
      <!--   {% if COLOR_SCHEME_CSS %}
            <link href="{{ SITEURL }}/{{ THEME_STATIC_DIR }}/css/code_blocks/{{ COLOR_SCHEME_CSS }}" rel="stylesheet">
        {% else %}
            <link href="{{ SITEURL }}/{{ THEME_STATIC_DIR }}/css/code_blocks/darkly.css" rel="stylesheet">
        {% endif %} -->
``` 

- add .css files to /Users/matthewkudija/Documents/GitHub/blog/theme/static/css/code_blocks from https://github.com/gilsondev/pelican-clean-blog/tree/master/static/css/code_blocks

- add COLOR_SCHEME_CSS = 'github_jekyll.css' to pelicanconf.py