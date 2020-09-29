Title: How to Use a Pilot Watch
date: 2020-09-25 06:00
updated: 2020-09-25 06:00
authors: Matthew Kudija
comments: true
slug: pilot-watch
tags: pilot, flying, computer

<!-- PELICAN_BEGIN_SUMMARY -->

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/00-watch.jpg" width="75%" height="75%"></p>

This is a brief tutorial for performing basic computations using the E6B flight computer on a pilot watch.

<!-- PELICAN_END_SUMMARY -->

# What is an E6B?

An E6B flight computer is a circular slide rule used by pilots to make common aviation calculations. A pilot watch typically contains a simplified version of a full E6B like the one shown below.

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/00-e6b.jpg" width="75%" height="75%"></p>

A US Navy officer developed the E6B—or "whiz wheel"—in the 1930s and it was first used on a large scale in WWII[^e6b]. The design is pretty much unchanged since then and every student pilot learns how to make basic calculations for flight planning using a standard E6B. It found its way onto a watch with the Navitimer pilot watch introduced by Breitling in the 1950s[^navimeter], and we will use the popular [Citizen Skyhawk](https://www.citizenwatch.com/us/en/product/JY8075-51E.html) ([manual](https://cf-store.widencdn.net/citizenwatch/9/b/d/9bd923da-d55c-49d6-994a-9ee040b9200a.pdf?response-content-disposition=inline%3B%20filename%3D%22U680_full_instructions_DEFAULT.pdf%22&response-content-type=application%2Fpdf&Expires=1601093068&Signature=WIr5VlbfLJvIRCz~ut9sEhfGwwhVtJ~~Wt7mBp19SoBylcw8Swuvv-vgZr9N4GpcWC6Di8CDz6QD33SQzWnKokLiW4wU4XGI~Kc6M~c4U8RvAv~jIGJANLoNsgp7bmfiGQgzgwu~5tzcBYB9ZEdXGOuT8d8b3~DVxbF12d~UdYLme330rceMepnzD6ixcqM13Us3bhPBayYYZ2q9EP8HfuIs-plVnjMG2pnM4x0AlpztPybE8quxvoJPHwxECuTgaGlwTQS~n-Q9hFCAb-aO~JucKW7kYWlVzXRTwDJizhQ~brd5XFqRvY-fEN3Zikbk-dc5VbEdRtASab7vHEvPNg__&Key-Pair-Id=APKAJD5XONOBVWWOA65A)) for these examples.

[^e6b]: Valerio, Pablo. “E6B Computer: Celebrating 75 Years Of Flight.” InformationWeek, Information Week, 28 Dec. 2015, [www.informationweek.com/government/e6b-computer-celebrating-75-years-of-flight/a/d-id/1323695](www.informationweek.com/government/e6b-computer-celebrating-75-years-of-flight/a/d-id/1323695). 

[^navimeter]: “Pilot Chronograph Watch Functions &amp; How to Use a Chronograph Watch?” WatchGecko, 27 Feb. 2017, [www.watchgecko.com/pilot-chronograph-watch-functions/](www.watchgecko.com/pilot-chronograph-watch-functions/). 

# Examples

The pilot watch, like a standard E6B, consists of two concentric scales, one of which rotates. Notice that both have special markings for the **10** position. We will reference one or the other of these frequently to identify the solution opposite them. 

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/01-overview.png" width="75%" height="75%"></p>


## Division

The most common computations on a pilot watch involve multiplication and division. We will start with division since it is the most straightforward: simply rotate the bezel so the two numbers to divide are over each other and read the result opposite the **10**.

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/02-division.png" width="75%" height="75%"></p>

## Multiplication

Since division is easy to remember, the multiplication method I prefer is the exact opposite. Set the first number to multiply opposite the red **10**, go to the second number to multiply on the inner bezel, and read the answer opposite it.

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/03-multiplication-1.png" width="75%" height="75%"></p>

An alternative method is to rotate the white **10** opposite the first number, find the second number on the outer bezel, and read the result on the inner bezel opposite from it.

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/04-multiplication-2.png" width="75%" height="75%"></p>

Here is another multiplication example:

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/05-multiplication-example.png" width="75%" height="75%"></p>

For a final practical example, say you need to split a $77 bill between 3 people and want to include a 20% tip, how much does each person pay? First divide 77 by 3 to determine that each person owes about $25.50 before the tip. Moving from **10** up to **12** (or 1.2), we see that with the tip each person owes about $31.

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/14-bill.png" width="75%" height="75%"></p>


Inevitably I will forget exactly how to set the bezels and whether to read off the inside or outside one. To remind myself, I pick a simple relationship that I know the answer to and use that pattern to do the multiplication or division I can't do in my head.


## Conversions

The pilot watch has markings for several conversions including distance and fuel units. For example, it is easy to convert distance between nautical miles, statute miles, and kilometers.

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/06-conversion.png" width="75%" height="75%"></p>


You can also convert between pounds and kilograms:

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/07-conversion-2.png" width="75%" height="75%"></p>



## Distance, Rate, and Time

Next we will demonstrate how to solve for distance, rate, or time given the other two variables. These are given by the following relationship:

```
Distance [unit] = Rate [unit/time] * Time [time]
```

If the time units are the same, you can use the multiplication and division examples above with the **10** index. However, if one is in hours and one is in minutes, we instead reference the below relationships:

```
Distance [unit] = Rate [unit/hr]      * Time [min] * 1/60 [hr/min]
Distance [nm]   = Rate [knot = nm/hr] * Time [min] * 1/60 [hr/min]
Distance [gal]  = Rate [gal/hr]       * Time [min] * 1/60 [hr/min]
```

To save from needed to divide or multiply by 60 to convert between hours and minutes, we instead use **60** or **MPH** at the 12 o'clock position as the index rather than the **10**.

Distance (or amount, like gallons) is show on the outer bezel, time in minutes on the inner bezel, and the rate in distance per hour at the **60** position. I remember this as follows:

- **Rate** at the top
- **Time** in minutes on the inner bezel (closest to the hands of the watch that tell time)
- **Distance** on the outer bezel (which also has markings for distance and fuel conversions)

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/09-drt-1.png" width="75%" height="75%"></p>


First, let's calculate **rate**—or airspeed—given distance and time. Rotate the bezel so the distance on the outer ring is over the time on the inner bezel, and read the rate across from the 60 at the top of the watch.

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/10-drt-2.png" width="75%" height="75%"></p>

To calculate **time** (in minutes) given speed and distance, set your speed at the top position and read the time on the inner bezel across from the distance on the outer bezel. Note in this example that the distance units don't matter as long as they are consistent. Here they are mph and miles, but they could also be knots and nm, gal/hr and gallons, etc.

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/11-drt-3.png" width="75%" height="75%"></p>

Likewise, to calculate **distance** given speed and time, set your speed at the top position and read the distance on the outer bezel across fro mthe time on the inner bezel.

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/12-drt-4.png" width="75%" height="75%"></p>

As mentioned above, we can substitue other "distance" units, in this case gallons per hour and gallons rather than airspeed and distance.

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/13-drt-5.png" width="75%" height="75%"></p>

In this final example we calculate the distance from an airport to start a descent in two steps. 

1. First, divide the altitude to descend by the desired descent rate to calculate the time to descend.
2. Next, determine your speed in <code>nm/min</code> by dividing your speed in knots (<code>nm/hr</code>) by 60 either using the watch or mentally.
3. Finally, multiply the time to descend by your groundspeed to calculate the distance from the airport to start the descent. 

If you are able to complete step 2 in your head, you can get straight to the answer with the outer bezel set in one position as show below.

<p style="text-align:center;"><img src="{filename}../images/citizen-skyhawk-e6b/08-descent.png" width="75%" height="75%"></p>


# Resources

Here are some videos I found helpful that include additional examples for how to use a pilot watch:

- [How to Use Aviation Pilot Watch. Advanced Tutorial for Real Aviators. Part 1 of 2](https://youtu.be/vSUHCkvmYnE)
- [How to Use Aviation Pilot Watch. Advanced Tutorial for Real Aviators. Part 2 of 2](https://youtu.be/tOMuTMUJLcs)
- [How On Earth Does A Navitimer Work? | Watchfinder & Co.](https://youtu.be/GlX01j1sNvo)
- [How to use a Slide Rule Bezel on your Watch](https://youtu.be/RuK_77DEUfw)
