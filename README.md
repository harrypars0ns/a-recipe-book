# London Skate-Spot Finder

Interactive Front End Development Milestone Project.

As a Skater I always found finding skate spots an annoying task, you either go out and look for them yourself or wait for another skater to take you.
I always wanted a simple site I could go to online to see all parks and spots in London.

This website is basically an interactive digital pocket guide to all the best skateparks and spots in London. It has the exact locations of more than 20 street spots and over 30 skateparks. This is perfect for skateboarders of all levels of ability.
From looking up where your local park is when you start skating, to the explorers trying to find that secret ledge that you've only seen in videos there's a use case for every skater.


## UX

### Strategy

I want to let people find the spot they want as quickly and in as few clicks as possible. The site should be aesthetically pleasing, simple and professional.

### Scope

The function of the site will be to give skateboarders and spectators a simple way to find places all around London to skateboard. You will be able to filter the location and type of the spot easily or search for the spot by name in an input box.

### Structure

The site was designed to be as user friendly as possible. I wanted to make sure that the UX was viable for people with bad eye-sight, people with dyslexia,
those who aren't comfortable using complex websites and the elderly (even if some users are not skaters some like to take their kids and grandkids to skateparks or just find places to watch skateboarding).

Whether you are a pro-skater, rookie or a parent looking for somewhere to take a child the London Skate-Spot Finder will give you no problems in your user experience.

### Skeleton
[Wireframe plan 1]  (https://github.com/harrypars0ns/milestone-2/blob/master/wireframes/LSSFwireframe.png)

[Wireframe plan 2]  (https://github.com/harrypars0ns/milestone-2/blob/master/wireframes/LSSFwireframe2.png)

### Surface
 
I want my users to be able to have to read as few words as possible to find the spot they need. 

The simple black text on white achieves this while still looking striking and professional.
The font sizes have been set to the biggest and most legible they can without sacrificing the usability and aesthetic of the website.

## Features

The Map is generated using the Google Maps API, it gives the user an impeccable experience in scrolling around the map
as well as having plenty of landmark information amongst the array of spot markers. I have buttons that work as a navigation point to filter spots by location (North, East, South, West and Central) and type (Skatepark or Street Spot).

There is a search bar at the bottom of the site that lets you search for the spot by name, and will filter to just your chosen spot on a click of a submit button or 'Enter' keypress. 

### Features Left to Implement

- When I have time I would like to make: A profile data base so skaters could sign-in and add their own spots to their map, as well as being able to favorite certain spots.

- Another great feature would be to add a direction/journey planner to show what public transport people can use to get to a spot from their GPS location.

- I would like to add more information such as address, difficulty, pictures and maybe links to YouTube videos for each spot in the info window.

- A weather layer for the map would be a useful feature controlled with a toggle button in the Nav.

## Technologies Used

- HTML
- CSS
- [Bootstrap](https://getbootstrap.com/)
    - The project uses **Bootstrap** for aiding placement and responsive design.
- [Google Fonts](https://fonts.google.com/)
    - The project uses the **Google Fonts** typeface 'Exo' in varying weights and sizes.
- [Google Maps Javascript API](https://developers.google.com/maps/documentation/javascript/tutorial)
    - The project uses the **Google Maps Javascript API** to generate the fully interactive map, markers and info-windows.

## Testing
 
When clicking the buttons the site would jump back to the top of the page almost looking like it was refreshing.
I gave the anchor-tag an href of its own ID so the screen will not move while clicking the buttons.

When first building the web-app I had the Nav Buttons (location filters) at the top of the screen, 
adhering to established design techniques. This gave me a few problems. Firstly when using the map you had to 
scroll all the way up past the title and logo every time you wanted to filter the spots. This made for a bad user experience.
I made the nav bar sticky so that you wouldn't need to scroll all the way up but it looked horrible when it scrolled over the title and logo.
Moving it down still looked professional and familiar while sacrificing none of the design or UX. 

Another reason for moving the nav down below the title was that it aided in making the site responsive on all screens, landscape or portrait. 
I was using a lot of media queries to make the site look good and still be easy to use. The site now works with 
very few media queries, looks good, feels good and all the text is extremely legible for any user.

While testing my app I came across a problem when you entered a spot name in the text-input that did not exist.
The map would wipe all markers off the map leaving the user confused. In the case of a typo I wanted all the markers to display.
The problem was that all of my event handlers were inside of the function that was being called for 'markers.length' (the total number of markers).
This made me realise that despite everything looking good there was something seriously wrong going on in the Javascript.
I had functions within functions that shouldn't have been there and moving them out messed up the scope of most of the variables.

This is when I underwent the massive task of refactoring the whole of my Javascript code. I started by defining all my global variables
and laying out what steps I wanted the site to take as it loaded. I placed my pieces of code within functions so everything was clear and separate.
I call these functions inside the initMap() function which is called straight away. The adding of event handlers is only being called once now. 

To fix the typo error I had to make a clear difference between the Google Maps markers that are rendered and the information that they
take to determine their position, name, content, type etc. First I made an empty array called mapMarkers which is where I wanted my selected Google Maps markers to be pushed to.
I put the array of markerData inside a function that returned the array, this allowed me to make a newMarker
by looping through the 'markerData' array, calling createMarker(markerData[i]) and pushing the newMarker to the empty mapMarker array to be rendered. 
If the text input does not match any of the markerData 'isSpotFound' is false, this selects all markers to be shown.

I ran the CSS and HTML through the W3C Jigsaw validator with no errors found. The Javascript was run through the JSHint validator with no major issues.

The site works across many browsers including: Chrome, Firefox, Safari and Edge.


## Deployment

I am hosting the site on GitHub pages on the master branch. I had a already commited to GitHub a few times before 
I actually put code on GitHub Pages. To do this I went into the settings tab in my GitHub repository and scrolled 
down to the GitHub Pages section, selected "master branch" as the source, and clicked 'Save'. 
This created the link to where my code is being published: "https://harrypars0ns.github.io/milestone-2/".  

If you want to run the code locally you can use 'git clone'. Alternatively you 
can download all the files in a .zip file and open 'index.html' in your browser of choice.


## Credits

### Content

I built the Nav buttons from scratch. The text input was built from scratch. All HTML, CSS and javascript was written by me. 
The map and markers are generated by the Google Maps Javascript API. 


### Media
I used Pexels (stock images) for my image, I only needed one icon.

### Acknowledgements

- I used the Bootstrap grid for responsive placement. (https://getbootstrap.com/docs/4.4/layout/grid/)

- The map and markers are generated by the Google Maps Javascript API. (https://developers.google.com/maps/documentation/javascript/tutorial)

 
