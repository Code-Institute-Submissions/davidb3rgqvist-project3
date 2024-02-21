![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!


https://www.asciiart.eu/image-to-ascii

WordStream: French Edition is an engaging language learning game designed to help you master essential French vocabulary effortlessly. Immerse yourself in the game, learn the top 1000 words, and watch your language skills flow with ease.

## Deployed page
The deployed WordStream website can be accessed using the following URL: [WordStream Deployment](https://davidb3rgqvist.github.io/project2/)

## Responsive Test
For a quick overview of responsiveness, we utilized [Am I Responsive](https://ui.dev/amiresponsive).

## Table of Contents
1. [UX - Five Planes](#ux---five-planes)
2. [Future Features](#future-features)
3. [Technology Used](#technology-used)
4. [Testing](#testing)
5. [Development](#development)
6. [Deployment](#deployment)
7. [Credits](#credits)

## UX - Five Planes
Strategy:
WordStream is a language learning game designed to help users master the 1000 most common French words for effective language acquisition. The game focuses on providing an interactive and engaging learning experience, aiming to kickstart users' ability to speak French.

User Goals:
Learn Core Vocabulary: Users aim to master the 1000 most common French words to kickstart their ability to speak the language.
Effective Learning: Users seek an efficient and effective learning experience, acquiring words gradually through practice.
Interactive Learning: Users are looking for an interactive and engaging method to enhance their language skills.
Owner Goals:
User Retention: The primary goal is to keep users engaged and motivated to continue their language learning journey.
Educational Impact: The owner aims to contribute positively to users' language acquisition.
User Satisfaction: Ensuring that users find the game enjoyable and beneficial for language learning
Scope:
Learning Mechanism: The primary function is to present users with French-English word pairs for learning.
Feedback System: Provide instant feedback on correct and incorrect answers, reinforcing learning.
Replayability: Allow users to play the game repeatedly to reinforce vocabulary and improve retention.
Shuffling Words: Implement a mechanism to shuffle words on page reload, providing a fresh learning experience.
Screen shots of the pages with comments

Structure:
Flashcard Interface: Use a flashcard format to present words, focusing on one word at a time for effective learning.
User Input: Incorporate a text input for users to type their answers.
Feedback Display: Display a visual cue (e.g., green flash) for correct answers and provide the correct word on mistakes.
Audio Feedback: Include the option for users to listen to the correct pronunciation.
Skeleton:
Start Button: Initiate the game with a "Start Game" button.
User Input Field: Allow users to type their answers.
Submit Button: Trigger the evaluation of user input.
Correct/Wrong Display: Visually indicate correct and incorrect answers.
Play Again Button: Provide an option to restart the game.
Exit to Scoreboard Button: Allow users to view their high scores.
Wireframe link

Surface:
Visual Design: Use a visually appealing and intuitive design to enhance the overall user experience.
Color Scheme: Employ a color scheme that is both engaging and comfortable for extended usage.
Responsive Design: Ensure the game is accessible and functional across various devices.
Audio Feedback: Incorporate audio elements for the correct word and word pronunciation.
Clear Typography: Use clear and readable fonts for an optimal reading experience.
Visual ID

Future Features
We plan to enhance the website with the following features:

More languages.
Filter option to be able the practice the words the the user finds harder.
Top ten user highscore.
3d effect when flipping the flashcards.
Technology Used
Front-end: HTML, CSS, JavaScript
Figma for wireframes
ChatGPT - for AI assistance
Adobe Photoshop for image editing
Adobe express for image content
Adobe Illustrator for graphic content
www.w3.org: Utilized to perform validation test of HTML and CSS.
https://jshint.com/: Utilized to perform validation test of JavaScript.
https://ui.dev/amiresponsive: Utilized for a quick overview of the responsivness.
Testing
Testing was an integral part of the website development process. We performed comprehensive tests across various devices and screen sizes to ensure a seamless user experience. This included functional testing to verify proper functionality of all features, as well as responsive testing to guarantee optimal display on different devices. Additionally we performed serval validation tests.

HTML Validation of index.html, no errors found
CSS Validation of style.css, no errors found
JavaScript Validation, no errors found
Lighthouse report
Responsiveness overview
Development
In crafting WordStream Learning, our development journey revolved around harnessing the power of HTML5, CSS3, and JavaScript. These technologies served as the backbone, providing a solid foundation for the website's structure, style, and interactive features. Our approach embraced a mobile-first philosophy, ensuring a seamless experience across various devices. To bring our vision to life, we leveraged Figma for meticulous UI/UX design and relied on Git and GitHub for effective version control.

As we chart the course for future development, we've identified key areas that can further enrich the WordStream Learning experience:

User-Centric Enhancements: Place a premium on user feedback to enhance the overall user experience. Consider implementing user registration, profile management, and avenues for user-generated content, fostering a more personalized connection.

Feature Expansion: Enrich the platform by introducing advanced search filters, seamless integration with social media platforms, and engaging features such as forums or challenges. These additions will contribute to a vibrant and interactive community.

Improving Accessibility: Strive for inclusivity by ensuring adherence to accessibility standards, catering to users with diverse needs and disabilities.

Continual Testing and Optimization: Uphold a commitment to excellence through an ongoing testing strategy. Identify and address bugs, enhance performance, and validate design changes to ensure a polished user experience.

Community Engagement: Cultivate a sense of community by encouraging user-driven content creation. Welcome feedback with open arms and respond promptly to user queries or concerns, fostering a responsive and vibrant community.

Security Measures: Fortify the platform with robust security measures. Safeguard user data, mitigate potential vulnerabilities, and proactively prevent security breaches to uphold user trust.

By embracing these strategic steps, our vision for WordStream Learning is not just a website but a dynamic hub for language learning. This roadmap emphasizes user-centric design, feature richness, accessibility, continuous improvement, community engagement, and robust security. As we embark on this journey, we remain committed to delivering a learning experience that goes beyond expectations.

Deployment
Deployed page The deployment process involved leveraging GitHub Pages, an integrated service provided by GitHub, to publish the website directly from the project's repository. Here are the steps for deployment:

GitHub Repository: The Free Gym Locator's codebase resides in a GitHub repository. - Repository

Branch Setup: Utilizing the default 'main' branch to host the deployable code.

Configuration: Configuring the repository settings within the GitHub repository's settings page to select the branch to deploy.

GitHub Pages: Enabling GitHub Pages from the repository settings to initiate the deployment process.

Verification: Verifying the deployment status and ensuring the website is live and accessible at the specified GitHub Pages URL.

Accessing the Deployed Site
The deployed WordStream website can be accessed using the following URL: https://davidb3rgqvist.github.io/project2/

The GitHub Pages deployment offers a convenient way to share the WordStream website with users