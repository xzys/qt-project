# PiMarket -- BigRed//Hacks 2014
_http://qtproject-sachinrudr.rhcloud.com/_

Developed for Cornell's Hackathon last weekend, this is a web application developed to solve a common problem: people using facebook to sell textbooks, event etickets, and apartment sublets among other things. 

The market has 2 points of emphasis. 1, being that it is based around communitties, which are determined by the domain of the users' email addresses (e.g. @cornell.edu, @microsoft.com, etc.) We figured that people from these localized communitites would be closer to each other location-wise and also that there is a sense of trust with someone from the same such community even if those people have never met before. 

2, that the design reflect the type of item being sold. For the hackathon, we only implemented "Textbooks" and "Tickets", but each is customized. Tickets contain information that is relevant, such as the date of event, location, etc. The design reflects the type of item as well, for example, Textbooks show a picture of the textbook that could be used to judge its condition.

The app itself runs on a Django Python and MySQL backend that communicates to a simple javascript frontend through a simple API. We used bootstrap to quickly create a homepage and user interface.
