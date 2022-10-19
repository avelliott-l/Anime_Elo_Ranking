# Anime_Elo_Ranking

Status -- In Development

Implementation:
I created a program that calculates ratings for and ranks the anime that I have watched through a simplified decision making process that focuses on choosing between 2 animes at a time rather than comparing an anime to the full list.
I separated my solution into smaller problems and tasks and wrote functions that followed this hierarchy of organization. The program takes user input to add an anime to the list of watched animes and then prompts the user with a max of 10 questions prompting them to compare the show with one other anime they already watched. My solution then utilizes the Elo rating system to calculate scores for each anime which are dynamically updated and reorganized after each ranking. The user can then choose to view either their top 10 animes or the full ranking as logged.
I implemented additional functionalities into the program which allow me to easily record my list of anime to watch in a centralized document. More importantly, the program has a function which will randomly recommend an anime to start from my list.

Future Considerations:
In future implementations I intend to expand the anime class to include additional descriptive features for each show such as whether it is Shounen or Shojo, the serie’s length, etc. The next step would be to reiterate on the current functions to allow more specialized actions such as displaying a ranking of all anime in a specific genre or recommending an anime to start based on criteria set by the user. In the long term I aim to translate this simple terminal program into a web app.
