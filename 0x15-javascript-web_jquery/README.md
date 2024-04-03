# 0x15. JavaScript - Web jQuery

## Description
This repository contains solutions to the tasks assigned in the 0x15. JavaScript - Web jQuery project.

## Resources
Read or watch:
- What is JavaScript?
- Selector
- Get and set content
- Manipulate CSS classes
- Manipulate DOM elements
- API Introduction
- GET & POST request
- JQuery Ajax Tutorial #1 - Using AJAX & API’s
- What went wrong? Troubleshooting JavaScript
- JQuery
- JQuery API
- JQuery Ajax

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why JQuery makes front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
- How to select HTML elements in JavaScript
- How to select HTML elements with JQuery
- Differences between ID, class, and tag name selectors
- How to modify an HTML element's style
- How to get and update an HTML element's content
- How to modify the DOM
- How to make a GET request with JQuery Ajax
- How to make a POST request with JQuery Ajax
- How to listen/bind to DOM events
- How to listen/bind to user events

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files will be interpreted on Chrome (version 57.0)
- All files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant with the flag --global $: semistandard *.js --global $
- You must use JQuery version 3.x
- You are not allowed to use var
- HTML should not reload for each action: DOM manipulation, update values, fetch data…

## Quiz questions
Great! You've completed the quiz successfully! Keep going!

## Tasks
### 0. No JQuery
- Write a JavaScript script that updates the text color of the <header> element to red (#FF0000). You must use document.querySelector to select the HTML tag. You can’t use the JQuery API.

### 1. With JQuery
- Write a JavaScript script that updates the text color of the <header> element to red (#FF0000). You can’t use document.querySelector to select the HTML tag. You must use the JQuery API.

### 2. Click and turn red
- Write a JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header. You can’t use document.querySelector to select the HTML tag. You must use the JQuery API.

### 3. Add .red class
- Write a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header. You can’t use document.querySelector to select the HTML tag. You must use the JQuery API.

### 4. Toggle classes
- Write a JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header. The <header> element must always have one class: red or green, never both at the same time and never empty. If the current class is red, when the user clicks on DIV#toggle_header, the class must be updated to green; and the reverse. You can’t use document.querySelector to select the HTML tag. You must use the JQuery API.

### 5. List of elements
- Write a JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item. The new element must be: <li>Item</li>. The new element must be added to UL.my_list. You can’t use document.querySelector to select the HTML tag. You must use the JQuery API.

### 6. Change the text
- Write a JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header. You can’t use document.querySelector to select the HTML tag. You must use the JQuery API.

### 7. Star wars character
- Write a JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json. The name must be displayed in the HTML tag DIV#character. You can’t use document.querySelector to select the HTML tag. You must use the JQuery API.

### 8. Star Wars movies
- Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json. All movie titles must be listed in the HTML tag UL#list_movies. You can’t use document.querySelector to select the HTML tag. You must use the JQuery API.

### 9. Say Hello!
- Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello. The translation of “hello” must be displayed in the HTML tag DIV#hello. You can’t use document.querySelector to select the HTML tag. You must use the JQuery API. Your script must work when it is imported from the <head> tag.
