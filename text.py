import pygame
from config import *

#rendering button texts on main page
playtext = buttonfont.render("play", True, colour)
quittext = buttonfont.render('quit', True, colour)
titletext = titlefont.render("CHEESEMANIA", True, colour_orange)
lbtitletext = titlefont.render("LEADERBOARD",True, colour_orange)
leaderboard_text = buttonfont.render("leaderboard", True, colour)
rules_text = buttonfont.render("rules", True, colour)


#rendering rules text
ruleslist1_text = smallfont.render("The aim of Cheesemania is to collect as", True, colour_orange)
ruleslist7_text = smallfont.render("many pieces of cheese from around the", True, colour_orange)
ruleslist8_text = smallfont.render("house as you can before the time runs out. ", True, colour_orange)
ruleslist6_text = smallfont.render("But watch out for the cats! If they catch", True, colour_orange)
ruleslist9_text = smallfont.render(" you running about they will eat you!", True, colour_orange)
ruleslist2_text = smallfont.render("Make your way around the house and then", True, colour_orange)
ruleslist10_text = smallfont.render(" exit through the other hole in the wall ", True, colour_orange)
ruleslist11_text = smallfont.render("to complete the level.", True, colour_orange)
ruleslist3_text = smallfont.render("Scores are calculated as follows:", True, colour_orange)
ruleslist4_text = smallfont.render("    When you collect a cheese score  = ", True, colour_orange)
ruleslist12_text = smallfont.render("10x (time left on timer)", True, colour_orange)
ruleslist5_text = smallfont.render("    If you exit the room with time to spare,", True, colour_orange)
ruleslist13_text = smallfont.render("score = 20x (time left on timer)", True, colour_orange)