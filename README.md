# 0. Introduction

As both an aspiring guitarist and product analytics/data science professional, I thought it would be a great idea to merge my interests into one project - using data to explore basic guitar music theory and to inform my next steps for learning guitar.

#### Guitar Motivation
For the last year I have been self teaching myself guitar. Like all things I've self-taught in the past, I have spent endless hours on youtube, learning new songs, chords, etc. I feel like I've got the basics down now and can learn most songs after watching a youtube video or finding the chords online. However, I'm hungry now to get into that next level of understanding - music theory. I want to know what and why I'm playing. I've found myself asking questions like - what chords sound good together? Why does chord x always show up after chord y? How can I think about starting to write my own music? What song should I be learning next? I've started diving into these questions through youtube, but like anything, I believed data could help guide my learning and decision making.

#### Data Motivation
Over the last few years, I've really found my interests converging at the intersetion of product and data. In school I was lucky enough to get involved in classes all over the data science spectrum, touching subjects and projects varying from ML to Data Visualization Interaction. Now as a Product manager, I am actively involved in analyzing our business data to help us make decisions on how to build our products!

Although I've done a lot so far, there's still so many more skills that I want to build upon in this space. For example, I've often worked with dirty data, usually in the form of logs generated from our software at work. However, I've never really had to gather it myself. And although I've gotten to answer some really cool questions with data, I've never been able to use data to explore a subject I really know nothing about.

#### Project  Overview

So for this project, I will be working down the data science pipeline from A-Z to explore the basics of music theory while simultaneosly building out my data science skills!

This notebook contains a majority of my work, broken up by each step in the process

1. Data Collection through Web Scraping

2. Data Cleaning and Exploratory Data Analysis

3. Takeaways and Next Steps


## 1. Data Collection through Web Scraping


The first step of the process was finding or creating an approptiate data set of guitar chords/tabelature. Specifically, I wanted a large data set of guitar tabelature from a variety of different difficulty levels, genres, artists, etc. One of my main objectives for this project was to build out my own ETL pipeline. With that in mind I decided to build a web scraper. 

I scraped my data from the popular guitar chords website ultimate-guitar.com. To scrape the site I utilized the selenium data package. This was my first time web scraping so I relied heavily on this amazing [youtube tutorial](https://www.youtube.com/watch?v=Xjv1sY630Uc) from Tech With Tim ! The code for my scraper can be found in the scraping folder in my git. But I will give a brief overview of my process here...


#### Choosing a site to scrape

There are a few different websites that host guitar tabs, but the most popular by far is ultimate-guitar.com. I considered some other sites as well, but UG seemed to have by far the most inventory of tabs. More importantly, each tab seems to follow a similar format - which is great for scraping capabilities. 

Unfortunately, UG does not have a single location that lists all of it's tabs, so I had to get a bit creative. I decided to break the scraping up into two parts. First, using the search page on UG to find the links to different song tabs, and stored that data in a csv. Second, I used that list I generated of song tabs and scraped through each song one by one, and stored that data in a csv.

#### Gathering a list of tabs to scrape

To gather the list of song url's, I played around with the url of the explore page. I itiratevely changed the url to filter by different genres and decades, resulting in different results in the search page. For each decade/genre combination, I would use selenium to grab all the urls from that page, navigate to the next page (often there were about 20 pages of results), then grabbed those urls as well. I would then change the decade/genre filter and go again.

#### Scraping tabs

Scraping the actual tabs once I had the URLs for them was rather straightforward. From each page, I gathered all information available about the song (chords, difficulty, capo, etc).

#### Results and Takeaways

In the end, I finished with a dataset of a little under 10,000 unique song tabs for guitar. I actually had a list of 30k tabs to eventually scrape, but unfortunately UG kicked me off the site for generating too much traffic. I had no idea this was a thing, but after reading about similar incidents online I decided to shut down the remaining scraping. I am a big user of UG and don't want to break any of their rules further! This was a great lesson though for future scraping activities - make sure to understand the site's guidelines regarding scraping before moving forward!


## 2. Data Cleaning and EDA

In school, we learned that these were two, almost sequential, parts of the data science pipeline. I realized pretty quickly stepping out on my own self-guided project that they are quite overlapping. I was able to quickly notice some low hanging fruit in the data, but it took some stepping through the data to get all the issues ironed out.

In the EDA itself I walk through each of the fields available in my data set to get a lay of the land. I then dive a little bit deeper into the chords of each song to learn some more about trends within the chord makeup of a song!


#### 3. Takeaways and Next Steps

Overall I'm really happy I started this project. I've always wanted to do a data science project on my own outside of school, but getting started seemed to be the hardest first step. Here's a couple of my takeaways and lessons learned from this project.

1. Web Scraping is fun! This was really my first time ever trying this out on my own. Selenium is an amazing tool that is pretty easy to pick up once you get the general concepts. Again, I cannot recommend TechWithTim enough for anyone looking to get started.

2. Stop striving for perfection. Since this was the first project I've done on my own and was planning on making public, I found myself trying to be very careful about what I was doing. I wanted to make sure every graph was insightful, or that every block of code was clean. This is so against how I usually write code and solve problems, and really slowed me down to start. A much better approach is to be messy, ask questions, dive deep. And then finally - go back and clean up your code!

3. Pandas is incredible. I feel like I have only scraped the surface on how valuable a tool this is.


I am pausing this project for now to start on a new one. But there are definitely some interesting next steps to take with this data set. I could see myself coming back to tackle some myself in the near future. With the NBA playoffs going on right now I just really want to dive into some NBA data. Here are some next steps/ideas for the future though.

1. Clean up chords to a more suitable and consistent format. There are so many different chords in this data set, but with a bit stronger knowledge of music theory, one could easily slice and dice these with some NLP.

2. Combine this data with Spotify Data. Can you find some patterns in the feeling of songs from the underlying chords?

3. Convert chords into their numerical equivalent. This is going to take some work to get keys for songs that don't have them yet and quite a few assuptions. 







