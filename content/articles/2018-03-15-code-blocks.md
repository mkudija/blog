Title: Code Block Highlighting
date: 2018-03-15 06:00
comments: true
slug: code-block
tags: python, makefile, make

<!-- ![alt]({filename}/images/carpet.jpeg) -->

<!-- PELICAN_BEGIN_SUMMARY -->

I test code block highlighting...

<!-- PELICAN_END_SUMMARY -->


Python:
```python
    Jinja2==2.6
    Pygments==1.6
    Unidecode==0.04.12
    argparse==1.2.1
    blinker==1.2
    docutils==0.10
    feedgenerator==1.5
    pelican==3.2
    pytz==2013b
    six==1.3.0
    wsgiref==0.1.2
```

None:
```
    Jinja2==2.6
    Pygments==1.6
    Unidecode==0.04.12
    argparse==1.2.1
    blinker==1.2
    docutils==0.10
    feedgenerator==1.5
    pelican==3.2
    pytz==2013b
    six==1.3.0
    wsgiref==0.1.2
```

Console: 
```console
    New python executable in duncanlock.net-pelican/bin/python
    Installing distribute.........done.
    Installing pip...............done.
    virtualenvwrapper.user_scripts creating
    [...]
    Creating /home/duncan/dev/duncanlock.net-pelican
    Setting project for duncanlock.net-pelican to /home/duncan/dev/duncanlock.net-pelican
```


Bash: 
```bash
    # virtualenvwrapper config
    export PROJECT_HOME=~/dev
    export WORKON_HOME=~/dev/virtualenvs
```

Markdown:
```markdown
Coming up in Part 2:
--------------------------

- Content creation work-flow
- Creating & customizing your theme
- Custom Jinja filters
- Configuring your Pelican site

  - Date based post URLs: ``/blog/2013/05/03/post-title-goes-here/``
  - Plugins
  - Extra files to copy over
  - Twitter Cards
  - Favicons, sitemaps, Google Analytics,
  - etc...
``