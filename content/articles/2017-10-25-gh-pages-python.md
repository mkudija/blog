Title: How and Why to Share Your Work Online
date: 2017-10-25 06:00
updated: 2018-03-30 06:00
authors: Matthew Kudija
comments: true
slug: gh-pages-python
tags: gh-pages, python, html, css, javascript, web
status: draft
<!-- Title: Step-by-Step Manual Guide to GitHub Pages -->


<!-- PELICAN_BEGIN_SUMMARY -->
<!-- ![alt]({filename}/images/gh-pages-python-2.png) -->

Building a basic website is an important skill for the entrepreneur, employee, and citizen of the Internet. My goal is that after reading this post you will:

1. Agree that controlling your web domain has benefits, and that basic web design skills can aid in this.
2. Understand the basic concepts required to build and operate a website, regardless of technology choices.
3. Be able to build your own simple static website by following my detailed instructions which use a set of popular (and free) technologies. 

The sections below are aligned with these three goals. Let's get started.

<!-- PELICAN_END_SUMMARY -->

[TOC]

# Part I: Why to Share Online (from your own domain)

## Why to Share Online

### Benefits to You
- **Learning**: sharing publicly forces you to learn
  - "teaching is the best way to learn": on the Internet your students are anyone who finds what you share to be useful or interesting (as well as your future self)
  - publich sharing/teaching forces you to refine your thinking so as to not embarass yourself. This post, for instance, started as a simple gh-pages tutorial but caused me to think deeply about the purpose of the Internet.
  - "The learning in writing these blog posts was immense. While these blog posts are public, I think I am the biggest beneficiary. Not only does one gain a good understanding of the concept involved, but one also gains confidence about the subject and one's ability to understand! The key lesson is to document your learnings, understandings, and try to abstract out your specific problem and think of teaching the concept to someone who doesn't know much about your problem." -[CS Ph.D. lessons to my younger self](https://nipunbatra.github.io/blog/2018/cs-phd-lessons.html), 2018-04-10
  - "The act of transforming ideas into words is an amazingly efficient way to solidify and refine your thoughts about a given topic." -[Blogging Like a Hacker](http://tom.preston-werner.com/2008/11/17/blogging-like-a-hacker.html), 2018-04-10
- **Feedback**: 
  - "you are who you spend your time with" and you need to challenge yourself by people better than yourself: even if physically isolated the Internet provides ready access to the people you want in your life
- **Body of Work**: practical and satisfaction
  - it gives you a public body of work to point to
  - yes there are practical benefits, but those are not the focus: job, portfolio, connections, etc.
  - more important is the learning in yourself and the satisfaction you receive from distilling some knowledge or wisdom
  - "During [WWI Churchill] had carefully filed memoranda, documents, and letters, explaining , in a letter to Clementine on July 17, 1915, 'Someday I shd like the truth to be known.'" (*The Last Lion*, 767)
- **Offload and record your thoughts**:
  - doesn't need to be public, but doing the above publicly serves this end
  - notes to your future self (useful and ...)
  - serves as a journal of your intellectual development
- **Business**:
  - if you are an entrepreneur, you need to reach customers
  - helps you network, etc.
- **Fame**:
  - notice that fame isn't on this list: "When you find yourself pining for fame and recognition, stop and consider what it might actually feel like when you get it—why you think you’ll be the exception to the rule and will find happiness in what nearly everyone else in history has found to be a chimera."-[Ryan Holiday](https://thoughtcatalog.com/ryan-holiday/2018/03/the-most-successful-people-are-the-ones-youve-never-heard-of-and-why-they-want-it-that-way/)

### Benefits to Others
- **Share info**: 
  - image of "on your computer" vs. "on the Internet"


<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">&quot;Things that are still on your computer are approximately useless.&quot; -<a href="https://twitter.com/drob?ref_src=twsrc%5Etfw">@drob</a> <a href="https://twitter.com/hashtag/eUSR?src=hash&amp;ref_src=twsrc%5Etfw">#eUSR</a> <a href="https://twitter.com/hashtag/eUSR2017?src=hash&amp;ref_src=twsrc%5Etfw">#eUSR2017</a> <a href="https://t.co/nS3IBiRHBn">pic.twitter.com/nS3IBiRHBn</a></p>&mdash; Amelia McNamara (@AmeliaMN) <a href="https://twitter.com/AmeliaMN/status/926509282874585089?ref_src=twsrc%5Etfw">November 3, 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



  - David Robinson "why you should blog" [^robinson]

  [^robinson]: [*Advice to aspiring data scientists: start a blog*](http://varianceexplained.org/r/start-blog/) by David Robinson



  - think of all that you've learned from blogs, etc.
  - feeling of just discovering someone and being nourished by their thinking: recently JMW, AJ, MMM
  - contributes to the original vision of the Internet
  - "The duty of a man is to be useful to his fellow-men; if possible, to be useful to many of them; failing this, to be useful to a few; failing this, to be useful to his neighbors; and failing them, to himself: for when he helps others, he advances the general interests of mankind." - Seneca, [*On Leisure*](http://www.bartleby.com/library/prose/4636.html)
- **Domocracy in the public square**: need to have a voice in the public square
  - builds a strong democracy: for our democracy to be healthy we need a serious conversation in the public square - the Internet is a public square
  - FT, etc.
  - Toqueville...?
  - Helpful: In a remarkable essay titled “On Leisure,” published after Seneca retired, the philosopher wrote in an oblique way about his own experiences: “The duty of a man is to be useful to his fellow-men; if possible, to be useful to many of them; failing this, to be useful to a few; failing this, to be useful to his neighbors, and, failing them, to himself: for when he helps others, he advances the general interests of mankind.”


Independent research notes: https://nadiaeghbal.com/independent-research

- "Do whatever you can’t stop thinking about. Documenting your findings in public (regardless of outcomes!) is a worthy contribution to society, full stop. If you’re doing something new, and you care about understanding the problem, people will pay attention."
- "You don’t need a PhD to study something you care about. You don’t need to publish papers in academic journals to become widely respected. You just need a curious mind, a bankroll, and a commitment to learning in public."


Show Your Work

- Learn in front of others: "The best way to get started on the path to sharing your work is to think about what you want to learn, and make a commitment to learning it in front of others." (19)
- "in this day and age, if your work isn't online, it doesn't exist" (23)
- Domain: "Social networks are great, but they come and go...If you're really interested in sharing your work and expressing yourself, nothing beats owning your own space online." (66)
- Domain: "The beauty of owning your own turf is that your can do whatever you want with it...You don't have to make compromises." (69)
- Body of work: "One little blog post is nothing on its own, but publish a thousand blog posts over a decade, and it turns into your life's work. My blog has been my sketchbook, my studio, my gallery, my storefront, and my salong. Absolutely everything good that has happened in my career can be traced back to my blog. My books, my art shows, my speaking gigs, some of my best friendships—they all exist because I have my own little piece of turf on the Internet." (66-67)
- "The minute you learn something, turn around and teach it to others." (117)

Silence in the age of noise

- “Sometimes it makes more sense to make life more difficult than necessary” (46)






## Why You Should Share From Your Own Domain
- **Control Your Data**:
- **Control Your Message**:
- **Better Understand the Internet**:
- **Support the good parts of the Internet, not the bad**:
  - does not support corporations that want to own your attention and sell your data
  - does not support a culture of anonymous sharing that leads to misinformation and ad homenin





The web, as envisioned by its inventor Sir Tim Berners-Lee, exists to enable "human communication, commerce, and opportunities to share knowledge."[^vision]
[^vision]: [World Wide Web Consortium (W3C) Mission](https://www.w3.org/Consortium/mission#vision)

The emergence of major web companies that control content creation—Facebook, etc.—endanger some of this vision by:

- pragmatic
- allows you to own your platform and message
- contributes to a healthy Internet (control personal data and information spread; not [too] relient on the corporations that own the Internet)
- take responsibility for what we say
- helps you understand how the Internet really works and impacts your life

Writing in *The Hedgehog Review*, Alan Jacobs shares his thoughts about the dangers of 


[*Tending the Digital Commons: A Small Ethics toward the Future*](http://iasc-culture.org/THR/THR_article_2018_Spring_Jacobs.php) by Alan Jacobs[^hedgehog]

> I think every young person who regularly uses a computer should learn the following:
> 
> 1. how to choose a domain name<br>
> 2. how to buy a domain<br>
> 3. how to choose a good domain name provider<br>
> 4. how to choose a good website-hosting service<br>
> 5. how to find a good free text editor<br>
> 6. how to transfer files to and from a server<br>
> 7. how to write basic HTML, including links to CSS (Cascading Style Sheet) files<br>
> 8. how to find free CSS templates<br>
> 9. how to fiddle around in those templates to adjust them to your satisfaction<br>
> 10. how to do basic photograph editing<br>
> 11. how to cite your sources and link to the originals<br>
> 12. how to use social media to share what you’ve created on your own turf rather than create within a walled factory<br>
> 
> One could add considerably to this list, but these, I believe, are the rudimentary skills that should be possessed by anyone who wants to be a responsible citizen of the open Web—and not to be confined to living on the bounty of the digital headmasters.

[^hedgehog]: Jacobs, Alan. "[Tending the Digital Commons: A Small Ethics toward the Future.](http://iasc-culture.org/THR/THR_article_2018_Spring_Jacobs.php)" *The Hedgehog Review* Vol. 20, No. 1 (2018): The Hedgehog Review. Web. 28 Mar. 2018.

Cite this: http://hackeducation.com/2017/04/04/domains[^domains]
[^domains]: http://hackeducation.com/2017/04/04/domains




# Part II: Introductory Concepts
Since one of the benefits of sharing your work through your domain is building a basic understanding of the technologies that power the Internet, let's review those technologies.

## Web Hosting
A website is just a collection of files, and those files need to stored somewhere. That somewhere is a computer connected to the internet, a server (TK). 

## Domain Names
The domain name is the address of your website, familiar as: `https://domain.com`. You can accept the default domain provided by the web hosting company you use (`.github.io` or `wordpress.com` for example), or you can purchase a custom domain (`your_name.com`). 

## Static Website


## HTML
Again, a website is just a collection of files. The primary files are written in HTML, or hyper-text markup language. The basic building block of your website is the `index.html` file, which gives the text to render on your webpage along with simple formatting tags. A line of HTML looks like this to define a heading and paragraph:

```html
<h1>Heading</h1>

<p>Text of your paragraph.</p>
```


## CSS
While HTML defines the content of your website, CSS (Cascading Style Sheet) defines how that content is formatted. CSS, usually given in `main.css`, defines the layout, colors, typeface, and other formatting elements of your website. Example CSS to determine the fontsize of a paragraph element looks like this:

```css
p {
	fontsize: 14;
	fontcolor: Red;
}
```

We reference a stylesheet in HTML like this:
```html
assets/main.css...
```



## JavaScript
HTML and CSS are primarily static. Dynamic elements of a website are commonly written in JavaScript. JavaScript looks like this


We reference a JavaScript script in HTML like this:
```html
<script>javascript.js</script>
```


## Python
<!-- Python is not required  -->


# Part III: Tutorial
Describe the example we will build....(recipes)

## Choosing Tools & Services
- GitHub is free, and that make this more accessible
  - Alan Jacobs actually recommends GitHub in his article
  - also includes version control
  - don't need to choose a domain name if you don't want to
- text editor



## Setting up GitHub Pages
- how to enable
- options for where to host (master, docs/, gh-pages branch)


## HTML Template
### Selecting a template
###Modifying a template
- Navigating HTML
- CSS colors


## Using Python to auto-generate your website
There are many great static site genrators
- `build.py`


## Add Extras
### Google Analytics

### Disqus Comments

### Mailchimp Subscribe (email is the way to build your platform, from Ryan Holiday in *Perennial Seller*)

### Formspree

### Favicon

### 404 page

### CNAME


## Other Notes
- previewing locally
- mobile preview
- right click-inspect element
- adding password protection


# Closing Thoughts


## Resources
- github
- html
- html5up templates
- css
- gh-pages
- markdown
- markdown2.py
- pelican