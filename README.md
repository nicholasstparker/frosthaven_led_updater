## Addressable LED strip control for Frosthaven Assistant

**WIP**

[Video in action](https://streamable.com/2la4t8)

Made to run on a raspberry pi that controls an led strip. See [this](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview) guide for details: 

Works exclusively with the wonderful [FrosthavenAssistant](https://github.com/Tarmslitaren/FrosthavenAssistant) by Tarmslitaren 

## Current effects
Card selection phase: Light up table ends in white, show players in red. When a player selects their initiative and is ready, update their color to green.

Round phase: Light up whomever's turn it is in green. The rest will be white. When it's an enemies turn, light up the ends in red and players in white.

## Guide
- Follow [this guide](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview) to get the LED strip working on the Pi.
> [!NOTE]
> My setup needed a line level converter to convert the 3.3v data signal to 5v for the led strip. The line level converter needs to be powered by 3.3v and 5 volt power, in addition to the signal wires and ground wires. There should be 6 wires total hooked up to the line level converter.
- Clone this repository
- Create a "settings.cfg" file in the project directory, set it up according to the ["settings.cfg"](https://github.com/nicholas-st-parker/x_haven_led_updater/new/master?filename=README.md#settingscfg) header below, 
- Start a FroshavenAssistant server.
- Change ip address and port in client.py to match the FrosthavenAssistant server
- Run main.py

## Example settings.cfg
```
start_led_index: the first led index along to strip where a person is located.
end_led_index: the last led index along the strip where a person is located.
```

The below example is with a 300 led strip. However, I discovered that it lights up 3 per time, so 100 addresses total. Currently, 100 addresses is the max supported as I need to update the lighting effects.

```
[Player1]
character = Crashing Tide
start_led_index = 0
end_led_index = 15
name = John

[Player2]
character = Trapper
start_led_index = 16
end_led_index = 31
name = John

[Player3]
character = Pyroclast
start_led_index = 32
end_led_index = 47
name = John

[Player4]
character = H.I.V.E.
start_led_index = 48
end_led_index = 63
name = John
```
