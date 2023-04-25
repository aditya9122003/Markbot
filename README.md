# Markbot
Zense Hacknite Winning Submission - Discord Track

Members : Krutik Patel, Aditya Garg

What the project does:

Through our project, we can browse through some famous e-commerce websites like Amazon, Flipkart, Snapdeal and Pepperfry. By this we mean, that we can search for any product using some simple and easy commands, and get the desired results. Also, the project has a local market, by which anyone can add their products in inventory(market) and search for products available in the marketplace. It also has the facility of cart and wish list, which dms privately your cart items.

How it was built:
 
We built our project, using ideas of web scraping and database. For this we used a module named “Selenium” and database named “SQLite3”. The commands involving Flipkart, Amazon etc, are built using “Selenium”. On the other hand, the local market place is built using database.
•	We accessed elements on the target web page, and automated the process of browsing through the web page using the technique of web scraping.
•	We used SQLite3 and stored the added product info, when the add instruction was passed. The same information was retrieved when the search instruction was passed.

"$hello"- prints "Hello there!"
"$help"- prints a help list
"$compare"- compares the products entered by user, and gives appropriate result. For example, “$compare iPhone 13 vs iPhone 12” gives the result, comparing the 2 phones.
"$market"- which should print the way to progress ahead; for example, if you give command of the type “$market flipkart rubik’s cube”, it should show the result of all the rubik’s cubes available on Flipkart. Similarly, we can implement the same in Amazon, Snapdeal and Pepperfry, and access local market.
  commands in "$market"- 
  1) "$market flipkart product"- searches for the product in Flipkart
  2) "$market amazon product"- searches for the product in amazon
  3) "$market snapdeal product"- searches for the product in snapdeal
  4) "$market pepperfry product"- searches for the product in pepperfry
  5) "$market flipkart ~a"- opens the main flipkart website. Similar applies to Amazon, Snapdeal, Pepperfry.
  6) "$market flipkart ~x"- opens the deals of the day page. Similar applies to Amazon which opens the same.
  7) “$market local add” – this command adds the product into the inventory. The user has to specify the product info after this command. For example- “$market local add --product--description--seller--price—image http link--thumbnail http link”. Here the image and thumbnail have to be http links. Make sure to add "--" between the terms.
  8) “$market local search”- this command searches for the product name in the inventory. For example- “$market local search name”.
  9) If inventory channel is created, your added product would be displayed in inventory channel, with reactions underneath them. The reactions are cart and wish-list, once you react to the message in inventory, a private dm would be sent to you by the bot itself, which would contain the message you reacted to and would say, item updated in cart.


How to run:

To run this bot, here are some basic requirements-
i)	Firstly, we need to have Windows operating system in our laptops (Selenium path is different on another operating system). Also, Google Chrome should be installed beforehand.
ii)	Next, we need to install “chromedriver.exe” file. For this we can go to the site, https://sites.google.com/chromium.org/driver/ and download the appropriate version of the driver or the version nearest to it. Next, make a folder in C Drive in your laptop, and name it SeleniumDrivers.  Next, paste the downloaded zip file in this folder and extract it there. So, basically your folder of SeleniumDrivers should consist of an exe file and a zip folder. 
iii)	Next, import or install all the required modules in your system. For this run these commands-
pip install discord
pip install selenium
pip install discord.ext
iv)	If you are using the bot on your server, make a inventory channel and replace the channel ID in “Bot_commands/variable/channelIDS” with the new inventory channel ID you created on your server. 
Now, we have implemented the basic introductory commands- if the below commands don't work, you can try it on our server:https://discord.gg/frqTbRQS
i)	“$hello”- which should print “Hello there”.
ii)	“$market”- which should print the way to progress ahead; for example, if you give command of the type “$market flipkart rubik’s cube”, it should show the result of all the rubik’s cubes available on Flipkart. Similarly, we can implement the same in Amazon, Snapdeal and Pepperfry, and access local market.
iii)	“$compare” command compares the products entered by user, and gives appropriate result. For example, “$compare iPhone 13 vs iPhone 12” gives the result, comparing the 2 phones.

   It also has commands like “$market ~amazon”, which gives deals of the day on Amazon.
iv)	To access local market place, there are 2 commands-
•	“$market local add” – this command adds the product into the inventory. The user has to specify the product info after this command. For example- “$market local add –product—description—seller--price—image http link—thumbnail http link”.
•	“$market local search”- this command searches for the product name in the inventory. For example- “$market local search --name”.
•	The inventory has all the items available.
