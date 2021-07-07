# Source for http://matthewkudija.com/blog

This repository contains the source for http://matthewkudija.com/blog/.

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

After reinstalling Python, I did this:

```
$ conda install -c conda-forge pelican
$ pip install pelican markdown
```

Build the html:

```
$ make publish
```

## Modifying the theme

### Colors
Set color theme to               


### Bigfoot footnotes

Add [bigfoot.js](http://www.bigfootjs.com/) footnotes by adding the following items to the `theme/` directory:

```
├── static
│   ├── css
│   │   └── bigfoot-default.css
│   └── js
│       ├── bigfoot.js
│       └── bigfoot.min.js
```
Note: to get the width to work, I added a `*7` to line 447 in `bigfoot.js`:
```javascript
maxWidth = Math.min(maxWidth, $this.find(".bigfoot-footnote__content").outerWidth() + 1)*7;
```

For fun I changed the color of the footnote when activated (line 41 in `bigfoot-default.css`):
```css
  background-color: #3377b3;
```


Add the following to `theme/templates/base.html`:
- `<link rel="stylesheet" href="../../../../theme/css/bigfoot-default.css" />` (within the `<head>` tag)
- just before the close of the `</body>` tag: 

```javascript
<script type="text/javascript" src="../../../../theme/js/bigfoot.js"></script>
<script type="text/javascript">
    $.bigfoot (
    {

    }
    );
</script>
```

