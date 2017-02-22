#!/usr/bin/env python

# Set up the different libraries used in the script.
from OmegaExpansion import oledExp
import urllib2
import json

# Pull the data from Weather Underground based on location and using your own API key.
# Get your own API key from https://www.wunderground.com/weather/api
APIKey = "<your API Key>"
PWSID = "<PWS ID Needed>"
weatherdata = urllib2.urlopen("http://api.wunderground.com/api/"+APIKey+"/conditions/q/pws:"+PWSID+".json")
weatherinfo = json.loads(weatherdata.read())

# Initialize and clear the OLED screen.
oledExp.driverInit()
oledExp.setDisplayMode(1)

# Write data out to the OLED screen and then Exit.
oledExp.setCursor(0, 0)
oledExp.write(" The Weather at Home")
oledExp.setCursor(1, 0)
oledExp.write("=====================")
oledExp.setCursor(2, 0)
oledExp.write("Cond "+weatherinfo['current_observation']['weather'])
oledExp.setCursor(3, 0)
oledExp.write("Temp "+weatherinfo['current_observation']['temperature_string'])
oledExp.setCursor(4, 0)
oledExp.write("Rain "+weatherinfo['current_observation']['precip_today_string'])
oledExp.setCursor(5, 0)
oledExp.write("Wind "+weatherinfo['current_observation']['wind_string'])

exit()