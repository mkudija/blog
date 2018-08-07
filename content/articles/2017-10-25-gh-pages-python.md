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
- [Part III: Tutorial](#part-iii-tutorial)
  - [Choosing Tools & Services](#choosing-tools--services)
  - [1. Set Up GitHub Pages](#1-set-up-github-pages)
  - [2. Download Theme](#2-download-theme)
  - [3. Set Up Extras](#3-set-up-extras)
  - [4. Enable Bigfoot Footnotes](#4-enable-bigfoot-footnotes)
  - [5. Update Books](#5-update-books)
  - [6. Update Reading](#6-update-reading)
  - [7. Particle background](#7-particle-background)
  - [Other Notes](#other-notes)
- [Closing Thoughts](#closing-thoughts)
  - [Resources](#resources)

<!-- /MarkdownTOC -->


# Part I: Why to Share Online (from your own domain)

## Why to Share Online

### Benefits to You
Sharing your work online brings benefits that can't be had working in seclusion. 

**Learning**

The single most important reason to share your work online is for the learning it enables. Sharing publicly can be uncomfortable but the the additional pressure can help you learn with a rigor that would otherwise be lacking if it was just for yourself. 

Sharing is a risk in that others may ignore you or even ridicule you. Polishing your ideas enough to share online is often the final step needed to solidify your understanding of a topic. Also, hearing people point out your mistakes might not be fun but it is a quick way to learn from them.

They say that "teaching is the best way to learn". On the Internet your students are anyone who finds what you share to be useful or interesting (as well as your future self, who very well may thank you for taking the time to write up your findings). 

Even if you have already gone through the work of developing an idea or program or other finished product, *explaining* it helps cement your learning: "The act of transforming ideas into words is an amazingly efficient way to solidify and refine your thoughts about a given topic."[^preston-werner]

[^preston-werner]: Tom Preston-Werner, “Blogging Like a Hacker,” Tom Preston-Werner's Blog, November 11, 2008, [`http://tom.preston-werner.com/2008/11/17/blogging-like-a-hacker.html`](http://tom.preston-werner.com/2008/11/17/blogging-like-a-hacker.html).

Plus, it freezes the topic while it is fresh in your mind for your later self to revisit and re-learn from. Notes to a future self are often reason enough to write something down in the first place.
  
> The learning in writing these blog posts was immense. While these blog posts are public, I think I am the biggest beneficiary. Not only does one gain a good understanding of the concept involved, but one also gains confidence about the subject and one's ability to understand! The key lesson is to document your learnings, understandings, and try to abstract out your specific problem and think of teaching the concept to someone who doesn't know much about your problem.<br>–Nipun Batra[^nipunbatra]

[^nipunbatra]: Nipun Batra, “CS Ph.D. lessons to my younger self,” Nipun Batra's Blog, January 7, 2018, [`https://nipunbatra.github.io/blog/2018/cs-phd-lessons.html`](https://nipunbatra.github.io/blog/2018/cs-phd-lessons.html).


**Build a Body of Work**

Sharing your work online is the first step in building a meaningful body of work. You will be able to take pride in pointing to something you created, and it might open other opportunities for you as well.

A typical knowledge worker may not as naturally create this body of work as an academic, artist, or craftsman for instance. Taking the time to fashion your more nebulous contributions into tangible pieces of work that can be shared online is a way to ensure your work accumulates over time rather than simply being lost to time. 

Building anything worthwile takes time and energy. More than actively pursuing a goal, sharing online should come from a mindset of always improving.  What you write up and share may be the first tentative steps of something bigger that won't materialize for quite some time. I like the story of how during World War I William Churchill "carefully filed memoranda, documents, and letters" away for inclusion in his memoirs.[^manchester] He went on to write *The World Crisis*, a 6-volume history of the war that secured his family's livelihood for many years. What could have been lost was instead built up in small pieces as events happened and later assembled into a meaningful body of work. 

[^manchester]: William Mancheseter, [*The Last Lion: Winston Spencer Churchill: Visions of Glory, 1874-1932*](https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=the+last+lion+visions+of+glory) (New York: Little, Brown, and Company, 1983), 767. Full quote: "carefully filed memoranda, documents, and letters, explaining, in a letter to Clementine on July 17, 1915, 'Someday I should like the truth to be known.'"

Little pieces of effort and examples of work add up over time. A little bit each day is great. A little  each week adds up quickly: "If you do one little thing each week, imagine how much you can learn in a year."[^little] Even at a monthly cadence you can build a solid foundation over a few year's time, and a lot of the blogs I have learned from average maybe 12 posts per year, or one per month. With patience and a long horizon, every little bit bit counts: "One little blog post is nothing on its own, but publish a thousand blog posts over a decade, and it turns into your life's work."[^kleon]

[^kleon]: Austin Kleon, [*Show Your Work!*](https://www.amazon.com/Show-Your-Work-Austin-Kleon/dp/076117897X/ref=sr_1_1?ie=UTF8&qid=1532378760&sr=8-1&keywords=show+your+work) (New York: Workman, 2014), 66-67. Full quote: "One little blog post is nothing on its own, but publish a thousand blog posts over a decade, and it turns into your life's work. My blog has been my sketchbook, my studio, my gallery, my storefront, and my salon. Absolutely everything good that has happened in my career can be traced back to my blog. My books, my art shows, my speaking gigs, some of my best friendships—they all exist because I have my own little piece of turf on the Internet."

[^little]: Derya Little, [*From Islam to Christ*](https://www.amazon.com/Islam-Christ-Womans-through-Riddles/dp/1621641120/ref=sr_1_1?ie=UTF8&qid=1532269958&sr=8-1&keywords=from+islam+to+christ) (San Francisco: Ignatius, 2017), 201.

Practical benefits may come from this (job offers, friendships, etc.), but the intrinsic benefits will suffice. This body of work is a journal of your intellectual development, an online repository of knowledge for future reference, and something you can point to with satisfaction and say, "I did that."


**Feedback**

I haven't gotten much feedback on what I have just recently started sharing online, but I imagine this could be a key benefit. The reality of the internet is that it shrinks the world making geographic proximity irrelevant in finding and conversing with people who share similar interests. 

Rude feedback can be ignored, but even negative feedback will help you if received in the right frame of mind. There's no quicker way to learn than by having others point out your mistakes.

  - "you are who you spend your time with" and you need to challenge yourself by people better than yourself: even if physically isolated the Internet provides ready access to the people you want in your life



**Business**

It goes without saying that if you want to build a business in today's world an online presence is required for all but the rarest exceptions. You need a way to reach customers, accept payments, respond to questions, and build a network. A website need not be complex or expensive (or built by a professional) to meet these basic needs. 


**Not Fame**

You'll notice that fame isn't on this list, though an honest self-examination by any author will probably reveal some desire for accolades. This is a poor reason to share online. Simple math says that your chances of achieving fame are not high, and I'll wager that the majority of what people post online languishes in obscurity. Plus, you might not even want what you're looking for: "When you find yourself pining for fame and recognition, stop and consider what it might actually feel like when you get it—why you think you’ll be the exception to the rule and will find happiness in what nearly everyone else in history has found to be a chimera."[^holiday]

[^holiday]: Ryan Holiday, “The Most Successful People Are The Ones You’ve Never Heard Of (And Why They Want It That Way),” Thought Catalog, March 20, 2018, [`https://thoughtcatalog.com/ryan-holiday/2018/03/the-most-successful-people-are-the-ones-youve-never-heard-of-and-why-they-want-it-that-way/`](https://thoughtcatalog.com/ryan-holiday/2018/03/the-most-successful-people-are-the-ones-youve-never-heard-of-and-why-they-want-it-that-way/).

Wow, so sharing your work can benefit you a lot. But guess what, it can help other people too.


<details>
  <summary>Click to expand</summary>

**Offload and record your thoughts**:
  - doesn't need to be public, but doing the above publicly serves this end
  - notes to your future self (useful and ...)
  - serves as a journal of your intellectual development

</details>





### Benefits to Others

A lot of what I know—apart from what I have read in [books](http://matthewkudija.com/reading)—I learned from what other people have shared online. Since you're reading this you probably have as well. Sharing some of your knowledge online is the best way to pay it forward to others. 

One challenge to overcome is the desire to only share what is *perfect*. But much of what you produce will be *useful to others* long before it is *perfect*. 

![alt]({filename}/images/sharing.png)

Granted you won't know what may be *useful* to someone else, but if you have put any amount of time into learning somehting you are probably underestimating rather than overestimating how useful it could be. 

Just remember that it must be *shared on the internet* to ever be useful to someone else. What you produce cannot help other people if it exists soley in your head, in a notebook, or on your computer.[^robinson] 

[^robinson]: I came across this tweet here: David Robinson, “Advice to aspiring data scientists: start a blog,” Variance Explained, November 14, 2017, [`http://varianceexplained.org/r/start-blog/`](http://varianceexplained.org/r/start-blog/).

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">&quot;Things that are still on your computer are approximately useless.&quot; -<a href="https://twitter.com/drob?ref_src=twsrc%5Etfw">@drob</a> <a href="https://twitter.com/hashtag/eUSR?src=hash&amp;ref_src=twsrc%5Etfw">#eUSR</a> <a href="https://twitter.com/hashtag/eUSR2017?src=hash&amp;ref_src=twsrc%5Etfw">#eUSR2017</a> <a href="https://t.co/nS3IBiRHBn">pic.twitter.com/nS3IBiRHBn</a></p>&mdash; Amelia McNamara (@AmeliaMN) <a href="https://twitter.com/AmeliaMN/status/926509282874585089?ref_src=twsrc%5Etfw">November 3, 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


"Documenting your findings in public (regardless of outcomes!) is a worthy contribution to society, full stop. If you’re doing something new, and you care about understanding the problem, people will pay attention."[^nadiaeghbal]

[^nadiaeghbal]: Nadia Eghbal, “The independent researcher,” Nadia Eghbal's Blog, June 27, 2018, [`https://nadiaeghbal.com/independent-research`](https://nadiaeghbal.com/independent-research).







<details>
  <summary>Click to expand</summary>


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

</details>




## Why You Should Share From Your Own Domain
If we agree sharing your work online benefits you and others, let's discuss why sharing from your own domain is helpful, and it boils down to this: control. Control over your message, control over your data, learning how the internet works and participating in how it was originally envisioned.


**Control Your Message and Data**: cultivate your own garden, rather than someone else's garden; link to it from Facebook/Twitter, but content resides on your domain


Cite this: https://dancohen.org/2018/03/21/back-to-the-blog/ [^dancohen]
- “re-decentralize” the web

[^dancohen]: Dan Cohen, “Back to the Blog,” Dan Cohen's Blog, March 21, 2018, [`https://dancohen.org/2018/03/21/back-to-the-blog/`](https://dancohen.org/2018/03/21/back-to-the-blog/).



https://dancohen.org/2018/06/26/going-indie-on-social-media/
- notmywebsite.com/dancohen
- 

**Better Understand the Internet**

Cite this: Audrey Watters: http://hackeducation.com/2017/04/04/domains [^hackeducation]
- "Students and staff can start to see how digital technologies work – those that underpin the Web and elsewhere. They can think about how these technologies shape the formation of their understanding of the world – how knowledge is formed and shared; how identity is formed and expressed."
- "But you can publish stuff on your own site first, and then syndicate it to these other for-profit, ad-based venues."
- "That’s your domain. You cultivate ideas there – quite carefully, no doubt, because others might pop by for a think. But also because it’s your space for a think."

[^hackeducation]: Audrey Watters, “Why 'A Domain of One's Own' Matters (For the Future of Knowledge),” Hack Education, April 4, 2017, [`http://hackeducation.com/2017/04/04/domains`](http://hackeducation.com/2017/04/04/domains).


**Support the good parts of the Internet, not the bad**:
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


With that as inspiration, the rest of this post is devoted to building up the 12 points Jacobs suggests. 





# Part II: Introductory Concepts
Since one of the benefits of sharing your work through your domain is building a basic understanding of the technologies that power the Internet, let's review the basics of those technologies.

**Web Hosting**
A website is just a collection of files, and those files need to stored somewhere. That somewhere is a computer connected to the internet, a server (TK). 

**Domain Names**
The domain name is the address of your website, familiar as: `https://domain.com`. You can accept the default domain provided by the web hosting company you use (`.github.io` or `wordpress.com` for example), or you can purchase a custom domain (`your_name.com`). 

**Static Website**


**HTML**
Again, a website is just a collection of files. The primary files are written in HTML, or hyper-text markup language. The basic building block of your website is the `index.html` file, which gives the text to render on your webpage along with simple formatting tags. A line of HTML looks like this to define a heading and paragraph:

```html
<h1>Heading</h1>

<p>Text of your paragraph.</p>
```


**CSS**
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



**JavaScript**
HTML and CSS are primarily static. Dynamic elements of a website are commonly written in JavaScript. JavaScript looks like this


We reference a JavaScript script in HTML like this:
```html
<script>javascript.js</script>
```


**Python**
<!-- Python is not required  -->


# Part III: Tutorial

The rest of this post is a step-by-step guide to building a static website. The example we will work through is a webiste my wife and I made to record and share the recipes we make: [`kudijakitchen.com`](http://kudijakitchen.com/)

## Choosing Tools & Services
Take this for what is it: an example illustrating just one of a myriad of ways to accomplish the goal of getting your work online. I made decisions about what technologies and services to use motivated by a desire to control my content and take advantage of free services, but you can find many easier[^easier], or just different, solutions to meet your preferences.

[^easier]: Yes, building a static website can be frustrating while you learn how to do so: Vicki Boykis, “Man, do static sites suck,” Vicki Boykis's Blog, May 30, 2015, [`http://veekaybee.github.io/2015/05/30/static-sites-suck/`](http://veekaybee.github.io/2015/05/30/static-sites-suck/).

For this tutorial, we will host our webiste using [GitHub Pages](https://pages.github.com/). Some benefits of this approach are that it is free, version controlled, and 

- GitHub is free, and that make this more accessible
  - Alan Jacobs actually recommends GitHub in his article
  - also includes version control
  - don't need to choose a domain name if you don't want to
- text editor


## 1. Set Up GitHub Pages
The first step is to set up a GitHub repository to host the files for your webiste. [GitHub](https://github.com/) is a hosting service for version controlled projects, and you'll want to start by making an account if you don't already have one. Then you can create your `<username>.github.io` repository (folder). 

The next step is to configure GitHub Pages. The [GitHub Pages welcom page](https://pages.github.com/) has simple instructions

- Setup your `<user>.github.io` repository.
- Under **Settings** > **GitHub Pages** you can enable GitHub Pages and select the source as either the master branch (root) of your repository, or the Docs folder. Select one and commit your website assets to that location (`index.html`, assets, etc.)
- If you have an active website at `<user>.github.io`, enabling GitHub Pages in other repositories on your account will make them visible from your main website. For instance, my website home is [matthewkudija.com](http://matthewkudija.com/), hosted in my [mkudija.github.io](https://github.com/mkudija/mkudija.github.io) repository. My blog is in the [blog](https://github.com/mkudija/blog) repository, and located therefore at [matthewkudija.com/blog](http://matthewkudija.com/blog).


## 2. Download Theme
- Find and download a theme. Some good (free) places to look include:
  - [HTML5UP](https://html5up.net/)
  - [Pelican Themes](https://github.com/getpelican/pelican-themes)
  - Find a website you like and inspect it, or better yet find a site hosted publicly on GitHub pages to view its whole source code.
- Customize theme to your liking.
  - This can be little things like changing the colors and typeface to larger things like adding functionality.
  - You don't need to commit your changes to GitHub to see the results. You can view them locally by right clicking on the file and opening in a web browser. Tip: using Safari you can go to **Develop** > **Enter Responsive Design Mode** to see how your site will look on different screens. This is great for making sure that what you see on a desktop when editing it will work well on mobile.
  - If you get stuck, it's easy to get help. You can hire someone on Fiverr for as little as $5 ($7 with their fee) to fix an issue on your website. I recommend [musebkhalid](https://www.fiverr.com/musebkhalid/create-remix-update-and-recover-web-pages?ref_ctx_id=1ca3bd97-b64d-4042-90b4-70582610f333).
- Alternatively, with a little HTML and CSS you can build a simple website yourself from scratch.

## 3. Set Up Extras
### 404.html
The default 404 page on GitHub pages is this:

![alt text](images/GitHub_404.png)

If you would like a 404 page to match your theme, you can add a custom [`404.html`](https://github.com/mkudija/mkudija.github.io/blob/master/404.html) to your root directory.

### CNAME
If you want a custom domain (i.e. matthewkudija.com instead of mkudija.github.io), perform the following:
1. Buy the domain from your preferred DNS provider. I use Host Gator.
2. Add a [CNAME](CNAME) file to your directory. This should contain just the domain: `matthewkudija.com`. 
3. Configure the A-record with the DNS provider to point to GitHub pages. I called Host Gator customer service and they got it set up. Refer to the [documentation](https://help.github.com/articles/setting-up-an-apex-domain/).
4. For Hostgator, set nameservers as:
- NS1.LAUNCHPAD.COM 
- NS2.LAUNCHPAD.COM
- NS3.LAUNCHPAD.COM 
- NS4.LAUNCHPAD.COM

#### HTTPS

https://help.github.com/articles/troubleshooting-custom-domains/#https-errors
Custom domains configured with A records
If you configured your custom domain using an A record, your A record must point to one of the following IP addresses for HTTPS to work:

185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153

### favicon.ico
Create or find a square image to use as your favicon. Go to one of the many favicon generator sites (such as [this](https://realfavicongenerator.net/)) to generate your favicon.

### robots.txt
I added a robots.txt but removed it after seeing that it messed up Google search results.

### sitemap.xml
I added a sitemap to aid in searching (and perhaps eventually get sitelinks on the search result) from [xml-sitemaps.com](https://www.xml-sitemaps.com).

### meta tag
I updated the meta tag to improve search results.

```html
<meta name="description" content="add a description of your site here">
<meta name="keywords" content="add, some, keywords, you, want, here"> 
```

### Google Analytics
Set up [Google Analytics](https://analytics.google.com/analytics/web/) to get your unique tracking ID and then copy the required code in to your HTML pages:

> This is the Global Site Tag (gtag.js) tracking code for this property. Copy and paste this code as the first item into the `<HEAD>` of every webpage you want to track. If you already have a Global Site Tag on your page, simply add the **config** line from the snippet below to your existing Global Site Tag.

```html
<!-- Global Site Tag (gtag.js) - Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-YOURID-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-YOURID-1');
  </script>
```


## 4. Enable Bigfoot Footnotes
See [this commit](https://github.com/mkudija/mkudija.github.io/commit/8f6ed3f882466ee92a2aa00a8afec854b9b390ec)
- to change button appearance, customize class "bigfoot-footnote__button" properties in [`bigfoot-default.css`](assets/css/bigfoot-default.css)
- to change popup appearance, customize class "bigfoot-footnote__content" properties in [`bigfoot-default.css`](assets/css/bigfoot-default.css)


## 5. Update Books
1. write book review in markdown
  * See [easybib](http://www.easybib.com/guides/citation-guides/chicago-turabian/footnotes/) exmple for footnote formatting: `Henry James, The Ambassadors (Rockville: Serenity, 2009), 34-40.` Footnotes in Markdown use this format:
```
"Blah blah blah."[^id] More words and more words.[^id2] Finally, let's add more words

[^id]: Footnote text for id1 goes here...
[^id2]: Footnote text for id2 goes here...
```

2. add cover image to [`images/books/`](images/books/)
3. add data in [`books/md/_content.xlsx`](books/md/_content.xlsx)
4. run [`books/md/_build.py`](books/md/_build.py) which creates an HTML file for each MD file defined in `_content.xlsx`\*
5. commit changes (including newly created html file)

\*Alternatively, individually convert from MD to HTML in the commany line by running [`markdown2.py`](/book-reviews/md/markdown2.py) (See [here](https://github.com/trentm/python-markdown2) for more information about markdown2 from @trentm):

```
python markdown2.py -x footnotes,smarty-pants,cuddled-lists,target-blank-links FNAME.md > FNAME.html
```


## 6. Update Reading
Run [`reading.py`](/reading/reading.py) to covert book list from Markdown to HTML. This also generates a plot.

```
python reading.py
```


## 7. Particle background
- Add particle background from http://jnicol.github.io/particleground/
- Config ~380 in `assets/js/jquery.particleground.js`


## Other Notes
- previewing locally
- mobile preview
- right click-inspect element
- adding password protection
- how to choose a license for your site

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