Title: Automation Using Python
date: 2018-06-08 06:00
authors: Matthew Kudija
comments: true
slug: python-automation
tags: python, makefile, make, automation, subprocess

<!-- PELICAN_BEGIN_SUMMARY -->

I previously wrote about [automation using Makefiles](http://matthewkudija.com/blog/2018/03/15/makefile-automation/) to bundle together running multiple scripts into a single command. Using the subprocess library we can perform the same tasks entirely in Python.

<!-- PELICAN_END_SUMMARY -->


# Why Python?

Make is a quick and easy to use tool for automation, and may be a good option. But Python offers certain advantages:

- Make isn't necessarily installed on Windows machines, but if the scripts you are automating are in Python it may be easier to automate with Python.
- Likewise, if you are already working in Python there is not new Make syntax to learn. 


# Writing a Makefile Equivalent in Python
To start, our entire Python equivalent of a [Makefile](https://github.com/mkudija/blog/blob/master/content/downloads/code/Makefile) is below:


```python
import sys
import subprocess

cwds = ['../CommercialData/', '../MarketView/', '../FleetView/']

def help():
    print('\nMakefile to update websites on MAG GitHub pages                                   ')
    print('                                                                                    ')
    print('Usage:                                                                              ')
    print('   python make.py html                                                              ')
    print('   <verify you like the changes that were made>                                     ')
    print('   python make.py publish                                                           ')
    print('                                                                                    ')
    print('Commands:                                                                           ')
    print('   python make.py data                MILE_file_copy and update_utilization         ')
    print('   python make.py html                make data, then regenerate the websites       ')
    print('   python make.py html-only           regenerate the websites (no data update)      ')
    print('   python make.py publish             publish regenerated websites to GitHub      \n')


def data():
    subprocess.call('python value_pickle.py', cwd='../MILE_Data/', shell=True)
    subprocess.call('python MILE_file_copy.py', cwd='../MILE_Data/', shell=True)
    subprocess.call('python update_utilization.py', cwd='../MILE_Data/', shell=True)


def html():
    for cwd in cwds:
        subprocess.call('python build.py', cwd=cwd, shell=True)


def publish():
    for cwd in cwds:
        print('\n')
        subprocess.call('git pull origin master', cwd=cwd, shell=True)
        subprocess.call('git add -A', cwd=cwd, shell=True)
        subprocess.call('git commit -m "auto-regenerate from python"', cwd=cwd, shell=True)
        subprocess.call('git push origin master', cwd=cwd, shell=True)
    print('\nDone.')


if __name__=='__main__':

    if sys.argv[1]=='help':
        help()
    elif sys.argv[1]=='data':
        data()
    elif sys.argv[1]=='html':
        data()
        html()
    elif sys.argv[1]=='html-only':
        html()
    elif sys.argv[1]=='publish':
        publish()
```

We need the `sys` library to parse arguments for the commands, and the `subprocess` library to execute the commands. We want to use this by calling `python make.py <command>`, so we structure a function for each of the primary commands of `help`, `data`, `html`, and `publish`. Each command is assigned the appropriate function(s) to perform the required operations. 

The functions themselves then use the `subprocess` library to issue the needed shell commands. If these commands are to be performed in another directory, it is easy to specify the correct directory with the `cwd` argument. 


# Executing the File

Back to our example, the previous process required us to:

- `cd` into each repo
- run `python build.py` update files
- commit the changes
- repeat for each

Using this automated file, the process now is simply:

- `cd` in to the directory containing `Makefile`
- `python make.py publish`


# Conclusion

Whenever you find yourself doing the same rote task often it may be a good time to ask yourself if some simple automation is appropriate. For anything you perform at the command line, a simple file like this Makefiles can be a lightweight automation solution.