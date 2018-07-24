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

Building a basic website is an important skill for the entrepreneur, employee, and citizen of the Internet. Using these skills to share your work online has benefits to you and others that justify the costs in time and effort required. My goal is that after reading this post you will:

1. Agree that controlling your web domain and sharing your work online has benefits, and that basic web design skills can aid in this.
2. Understand the basic concepts required to build and operate a website, regardless of technology choices.
3. Be able to build a simple static website by following my detailed instructions which use a set of popular (and free) technologies. 

The sections below are aligned with these three goals. Let's get started.

<!-- PELICAN_END_SUMMARY -->


<!-- [TOC] -->

<!-- MarkdownTOC autolink="true" levels="1,2" -->

- [Part I: Why to Share Online \(from your own domain\)](#part-i-why-to-share-online-from-your-own-domain)
  - [Why to Share Online](#why-to-share-online)
  - [Why You Should Share From Your Own Domain](#why-you-should-share-from-your-own-domain)
- [Part II: Introductory Concepts](#part-ii-introductory-concepts)
  - [Web Hosting](#web-hosting)
  - [Domain Names](#domain-names)
  - [Static Website](#static-website)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)
  - [Python](#python)
- [Part III: Tutorial](#part-iii-tutorial)
  - [Choosing Tools & Services](#choosing-tools--services)
  - [Setting up GitHub Pages](#setting-up-github-pages)
  - [HTML Template](#html-template)
  - [Using Python to auto-generate your website](#using-python-to-auto-generate-your-website)
  - [Add Extras](#add-extras)
  - [Other Notes](#other-notes)
- [Closing Thoughts](#closing-thoughts)
  - [Resources](#resources)

<!-- /MarkdownTOC -->


# Part I: Why to Share Online (from your own domain)

## Why to Share Online

### Benefits to You
Sharing your work online brings benefits that can't be had working in seclusion. 

**Learning**

The single most important reason to share your work is for the learning it fosters in you. Sharing publicly can be uncomfortable but it forces you to learn. In fact, the discomfort may have a great deal to do with it.

Sharing is a risk, in that others may ignore you, or at worst ridicule you. But public sharing/teaching forces you to refine your thinking so as to not embarass yourself. But people pointing out your mistakes is a quick way to learn.

This post, for instance, started as a simple gh-pages tutorial but caused me to think deeply about the purpose of the Internet.

They say that "teaching is the best way to learn". On the Internet your students are anyone who finds what you share to be useful or interesting (as well as your future self, who very well may thank you for taking the time to write up your findings). 

Even if you have already gone through the work of developing an idea or program or other finished product, *explaining* it helps cement your learning: "The act of transforming ideas into words is an amazingly efficient way to solidify and refine your thoughts about a given topic."[^preston-werner]

[^preston-werner]: Tom Preston-Werner, “Blogging Like a Hacker,” Tom Preston-Werner's Blog, November 11, 2008, [`http://tom.preston-werner.com/2008/11/17/blogging-like-a-hacker.html`](http://tom.preston-werner.com/2008/11/17/blogging-like-a-hacker.html).

Plus, it freezes the topic in its freshest form for your later self to revisit and re-learn from. Notes to a future self are often reason enough to write something down in the first place.
  
> The learning in writing these blog posts was immense. While these blog posts are public, I think I am the biggest beneficiary. Not only does one gain a good understanding of the concept involved, but one also gains confidence about the subject and one's ability to understand! The key lesson is to document your learnings, understandings, and try to abstract out your specific problem and think of teaching the concept to someone who doesn't know much about your problem.<br>–Nipun Batra[^nipunbatra]

[^nipunbatra]: Nipun Batra, “CS Ph.D. lessons to my younger self,” Nipun Batra's Blog, January 7, 2018, [`https://nipunbatra.github.io/blog/2018/cs-phd-lessons.html`](https://nipunbatra.github.io/blog/2018/cs-phd-lessons.html).


**Build a Body of Work**

Sharing your work online is the first step in building a meaningful body of work. You will be able to take pride in pointing to something you created, and it might open other opportunities for you as well.

Academics, artists, craftsmen might have a body of work built more naturally by virtue of the products they produce. For a typical knowledge worker this might not be so easy. Taking the time to fashion your more nebulous contributions into tangible pieces of work that can be shared online is a way to allow your...What you write up and share may be the first steps of something bigger that won't materialize for quite some time. I like the story of how during World War I William Churchill "carefully filed memoranda, documents, and letters, explaining, in a letter to Clementine on July 17, 1915, 'Someday I should like the truth to be known.'"[^manchester] He went on to write *The World Crisis*, his 6-volume history of the war that secured his family's livelihood for many years. 

[^manchester]: William Mancheseter, [*The Last Lion: Winston Spencer Churchill: Visions of Glory, 1874-1932*](https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=the+last+lion+visions+of+glory) (New York: Little, Brown, and Company, 1983), 767.


A spacecraft's heatshield is ablative in that it peels away as it rejects heat. Let your work be the opposite and be an accretive force. 

Building anything worthwile takes time and energy. More than actively pursuing a goal, sharing online is a mindset of always improving and adding. 

>One little blog post is nothing on its own, but publish a thousand blog posts over a decade, and it turns into your life's work. My blog has been my sketchbook, my studio, my gallery, my storefront, and my salon. Absolutely everything good that has happened in my career can be traced back to my blog. My books, my art shows, my speaking gigs, some of my best friendships—they all exist because I have my own little piece of turf on the Internet.<br>–Austin Kleon[^kleon]

[^kleon]: Austin Kleon, [*Show Your Work!*](https://www.amazon.com/Show-Your-Work-Austin-Kleon/dp/076117897X/ref=sr_1_1?ie=UTF8&qid=1532378760&sr=8-1&keywords=show+your+work) (New York: Workman, 2014), 66-67.


Beyond the satisfacion of having something to point to, there may be practical benefits as well (though understand there is change involved also): 
  - yes there are practical benefits, but those are not the focus: job, portfolio, connections, etc.
  - more important is the learning in yourself and the satisfaction you receive from distilling some knowledge or wisdom




**Feedback**

I haven't gotten much feedback on what I have just recently started sharing online, but I imagine this could be a key benefit. The reality of the internet is that it shrinks the world making geographic proximity irrelevant in finding and conversing with people who share similar interests. 

Rude feedback can be ignored, but even negative feedback will help you if received in the right frame of mind. There's no quicker way to learn than by having others point out your mistakes.

  - "you are who you spend your time with" and you need to challenge yourself by people better than yourself: even if physically isolated the Internet provides ready access to the people you want in your life



**Business**

It goes without saying that if you want to build a business in today's world an online presence is required for all but the rarest exceptions. You need a way to reach customers, accept payments, respond to questions, and build a network. A website need not be complex or expensive (or built by a professional) to meet these basic needs. 


**Not Fame**

You'll notice that fame isn't on this list, though an honest self-examination by any author will probably reveal some desire for accolades. This is a poor reason to share online. Simple math says that your chances of achieving fame are not high, and I'll wager that the majority of what people post online languishes in obscurity. Plus, you might not even want what you're looking for: "When you find yourself pining for fame and recognition, stop and consider what it might actually feel like when you get it—why you think you’ll be the exception to the rule and will find happiness in what nearly everyone else in history has found to be a chimera."[^holiday]

[^holiday]: Ryan Holiday, “The Most Successful People Are The Ones You’ve Never Heard Of (And Why They Want It That Way),” Thought Catalog, March 20, 2018, [`https://thoughtcatalog.com/ryan-holiday/2018/03/the-most-successful-people-are-the-ones-youve-never-heard-of-and-why-they-want-it-that-way/`](https://thoughtcatalog.com/ryan-holiday/2018/03/the-most-successful-people-are-the-ones-youve-never-heard-of-and-why-they-want-it-that-way/).


**Offload and record your thoughts**:
  - doesn't need to be public, but doing the above publicly serves this end
  - notes to your future self (useful and ...)
  - serves as a journal of your intellectual development


Wow, so sharing your work can benefit you a lot. But guess what, it can help other people too.





### Benefits to Others

A lot of what I know—apart from what I have read in [books](http://matthewkudija.com/reading)—I learned from what other people have shared online. Since you're reading this you probably have as well. Sharing some of your knowledge online is the best way to pay it forward to others. 

One challenge to overcome is the desire to only share what is *perfect*. But much of what you produce will be *useful* long before it is *perfect*. 

![alt]({filename}/images/sharing.png)

Granted you won't know what may be *useful* to someone else, but if you have put any amount of time into learning somehting you are probably underestimating rather than overestimating what may be useful. 

Just remember that it must be *shared on the internet* to ever be useful to someone else. What you produce cannot help other people if it exists soley in your head, in a notebook, or on your computer. 

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">&quot;Things that are still on your computer are approximately useless.&quot; -<a href="https://twitter.com/drob?ref_src=twsrc%5Etfw">@drob</a> <a href="https://twitter.com/hashtag/eUSR?src=hash&amp;ref_src=twsrc%5Etfw">#eUSR</a> <a href="https://twitter.com/hashtag/eUSR2017?src=hash&amp;ref_src=twsrc%5Etfw">#eUSR2017</a> <a href="https://t.co/nS3IBiRHBn">pic.twitter.com/nS3IBiRHBn</a></p>&mdash; Amelia McNamara (@AmeliaMN) <a href="https://twitter.com/AmeliaMN/status/926509282874585089?ref_src=twsrc%5Etfw">November 3, 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


"Documenting your findings in public (regardless of outcomes!) is a worthy contribution to society, full stop. If you’re doing something new, and you care about understanding the problem, people will pay attention."[^nadiaeghbal]

[^nadiaeghbal]: Nadia Eghbal, “The independent researcher,” Nadia Eghbal's Blog, June 27, 2018, [`https://nadiaeghbal.com/independent-research`](https://nadiaeghbal.com/independent-research).





  - David Robinson "why you should blog" [^robinson]

[^robinson]: David Robinson, “Advice to aspiring data scientists: start a blog,” Variance Explained, November 14, 2017, [`http://varianceexplained.org/r/start-blog/`](http://varianceexplained.org/r/start-blog/).




  - think of all that you've learned from blogs, etc.
  - feeling of just discovering someone and being nourished by their thinking: recently JMW, AJ, MMM
  - contributes to the original vision of the Internet
  - "The duty of a man is to be useful to his fellow-men; if possible, to be useful to many of them; failing this, to be useful to a few; failing this, to be useful to his neighbors; and failing them, to himself: for when he helps others, he advances the general interests of mankind." - Seneca, [*On Leisure*](http://www.bartleby.com/library/prose/4636.html)
  - Helpful: In a remarkable essay titled “On Leisure,” published after Seneca retired, the philosopher wrote in an oblique way about his own experiences: “The duty of a man is to be useful to his fellow-men; if possible, to be useful to many of them; failing this, to be useful to a few; failing this, to be useful to his neighbors, and, failing them, to himself: for when he helps others, he advances the general interests of mankind.”


**Domocracy in the public square**: need to have a voice in the public square

  - builds a strong democracy: for our democracy to be healthy we need a serious conversation in the public square - the Internet is a public square
  - FT, etc.
  - Toqueville...?






Independent research notes: https://nadiaeghbal.com/independent-research
- "You don’t need a PhD to study something you care about. You don’t need to publish papers in academic journals to become widely respected. You just need a curious mind, a bankroll, and a commitment to learning in public."


Show Your Work

- Learn in front of others: "The best way to get started on the path to sharing your work is to think about what you want to learn, and make a commitment to learning it in front of others." (19)
- "in this day and age, if your work isn't online, it doesn't exist" (23)
- Domain: "Social networks are great, but they come and go...If you're really interested in sharing your work and expressing yourself, nothing beats owning your own space online." (66)
- Domain: "The beauty of owning your own turf is that your can do whatever you want with it...You don't have to make compromises." (69)
- "The minute you learn something, turn around and teach it to others." (117)

Silence in the age of noise

- “Sometimes it makes more sense to make life more difficult than necessary” (46)






## Why You Should Share From Your Own Domain
- **Control Your Data**: cultivate your own garden, rather than someone else's garden; link to it from Facebook/Twitter, but content resides on your domain
- **Control Your Message**:
- **Better Understand the Internet**:
- **Support the good parts of the Internet, not the bad**:
  - does not support corporations that want to own your attention and sell your data
  - does not support a culture of anonymous sharing that leads to misinformation and ad homenin attacks





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

[^hedgehog]: Alan Jacobs. "[Tending the Digital Commons: A Small Ethics toward the Future.](http://iasc-culture.org/THR/THR_article_2018_Spring_Jacobs.php)" *The Hedgehog Review* Vol. 20, No. 1 (2018): The Hedgehog Review. Web. 28 Mar. 2018.



Cite this: Audrey Watters: http://hackeducation.com/2017/04/04/domains [^hackeducation]
- "Students and staff can start to see how digital technologies work – those that underpin the Web and elsewhere. They can think about how these technologies shape the formation of their understanding of the world – how knowledge is formed and shared; how identity is formed and expressed."
- "But you can publish stuff on your own site first, and then syndicate it to these other for-profit, ad-based venues."
- "That’s your domain. You cultivate ideas there – quite carefully, no doubt, because others might pop by for a think. But also because it’s your space for a think."

[^hackeducation]: Audrey Watters, “Why 'A Domain of One's Own' Matters (For the Future of Knowledge),” Hack Education, April 4, 2017, [`http://hackeducation.com/2017/04/04/domains`](http://hackeducation.com/2017/04/04/domains).


Cite this: https://dancohen.org/2018/03/21/back-to-the-blog/ [^dancohen]

[^dancohen]: Dan Cohen, “Back to the Blog,” Dan Cohen's Blog, March 21, 2018, [`https://dancohen.org/2018/03/21/back-to-the-blog/`](https://dancohen.org/2018/03/21/back-to-the-blog/).


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

Can still be frustrating though: http://veekaybee.github.io/2015/05/30/static-sites-suck/

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