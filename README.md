# Project 1: Movie Trailer Website
### by Shalvi Saxena

Movie trailer website project, part of the Udacity [Full Stack Web Developer
Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## What it is and does

A Python program that produces the HTML for a movie website that displays
a number of movies. Click on a movie poster to play its trailer.

## Required Libraries and Dependencies

Python 2.x is required to run this project. The Python executable should be in
your default path, which the Python installer should have set.

## Project contents

This project consists for the following files:

* entertainment_center.py - main Python script to run
* media.py - contains the class Movie that stores movie details
* fresh_tomatoes.py - creates the HTML file for the website (Udacity supplied)

## Quick Start

After downloading the project files, a movie trailer page can be created by 
importing media.py and fresh_tomatoes.py at the start of your Python script.
Then create idividual Movie objects by calling media.Movie() and supplying it 
with six arguments -- title, storyline, genre, imbd rating, poster_url, and trailer_url. Lastly, to 
generate the movie trailers page, call fresh_tomatoes.open_movies_page() and 
supply it with an array of the movie objects you created.



## How to Run Project

```

import media
import fresh_tomatoes

#information for object arguments
title = "Harry Potter"
storyline= "Rescued from the outrageous neglect of his aunt and uncle, a young boy with a great destiny proves his worth while attending Hogwarts School of Witchcraft and Wizardry."
genre= "Adventure, Family, Fanatsy"
imbd rating= "7.5"
poster_url = "http://cdn.playbuzz.com/cdn/c1e7b97f-42d8-41a5-8e14-0d816e3c1160/37202648-8c3d-45ce-abcc-c7affcb612a7.jpg"
trailer = "https://www.youtube.com/watch?v=PbdM1db3JbY"

# Create Movie object
harry_potter = media.Movie(movie_title, movie_storyline, movie_genre, movie_rating, poster_image, trailer_youtube)

```



Download the project zip file to you computer and unzip the file. Or clone this
repository to your desktop.

Open the text-based interface for your operating system (e.g. the terminal
window in Linux, the command prompt in Windows).

Navigate to the project directory and type in the following command:

```bash
python entertainment_center.py
```

Your default browser should launch a new tab displaying the movie trailer website.