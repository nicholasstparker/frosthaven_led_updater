## Addressable LED strip control for Frosthaven Assistant

![Lights in Action](https://github.com/nicholas-st-parker/frosthaven_led_updater/blob/4ba176e09931a0256b2d651c34908fef847aafd1/media/table_working.gif)

**WIP**

[Video (same as above but longer and full res)](https://streamable.com/2la4t8)

Made to run on a raspberry pi that controls an led strip. See [this](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview) guide for details: 

Works with the wonderful [FrosthavenAssistant](https://github.com/Tarmslitaren/FrosthavenAssistant) by Tarmslitaren 

## Current effects
Card selection phase: Light up table end in white, show players in red. When a player selects their initiative and is ready, update their color to green.

Round phase: Light up whomever's turn it is in green. The rest will be white. When it's an enemies turn, light up the end in red and players in white.

Elements: When an element is created, light up the ends in the element color.

## Hardware
Links:
- [Raspberry Pi 3b+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/)
- [12v LED strip](https://www.amazon.com/BTF-LIGHTING-300LEDs-Addressable-Flexible-Non-waterproof/dp/B01CNL6K52?pd_rd_w=nRFHk&content-id=amzn1.sym.0c0e3277-1675-489c-a566-ea075b32087a&pf_rd_p=0c0e3277-1675-489c-a566-ea075b32087a&pf_rd_r=4ZGYHJ5A457XQB3MZMKR&pd_rd_wg=QBOrn&pd_rd_r=64e79d08-602f-4aee-b0ea-9b27f01763e5&pd_rd_i=B01CNL6K52&psc=1&ref_=pd_basp_d_rpt_ba_s_6_t)
- [Logic level converter](https://www.amazon.com/KeeYees-Channels-Converter-Bi-Directional-Shifter/dp/B07LG646VS?pd_rd_w=tlNdK&content-id=amzn1.sym.378a0f29-5acb-4c80-bc6e-087cd6806daf&pf_rd_p=378a0f29-5acb-4c80-bc6e-087cd6806daf&pf_rd_r=SAK4DYA6KJKSG28RVTH2&pd_rd_wg=5iHhp&pd_rd_r=ebded6a3-37b7-43ed-b50e-dff2204847aa&pd_rd_i=B07LG646VS&psc=1&ref_=pd_bap_d_grid_rp_0_1_ec_pr_sr_ppb_t)
- [24v Power supply](https://www.amazon.com/gp/product/B0B1CZYQF8/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- [24v to 12v 10A Step Down](https://www.amazon.com/gp/product/B09X1ZG6K8/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1)
- [5v Buck converter to power Pi](https://www.amazon.com/Adjustable-Converter-Step-Down-Regulator-Stabilizer/dp/B081N6WWJS/ref=sr_1_4?crid=BKM3NKJ34UQO&dib=eyJ2IjoiMSJ9.SOd-7SjAEiqFrIC5kk8Klvr4cwZvbwuGy7k38CwRIjGgfCH0cJyw-V4IOJw8V9os3CCWxN4zeJTYChccLOn96aQc6SKhZRSCbP1oMF3JOKFrOh093WhLg6MKsW1rYD7xrB4qgMOuyrN8M1lVwIQCYGItQaZgrdoZNOvoo3yObhFFJh212icWfTfD0_TnQhOTGESzXzbCXfUzsdtFDsYllyLqmYLfYntQ8bZpCmjbXpc36SXDHX1dCkobLKwGenh-0fuvAMPCqgDfN7zhB66rkmDn5B1Qbfm5hgvLpPa5fDs.DhpHcOSnusQ8FPHs1KDRHpcmYGaA4GEpHywDWQG36eE&dib_tag=se&keywords=5v+buck&qid=1721307067&sprefix=5v+buc%2Caps%2C126&sr=8-4)

Pictures:
![Electronics Box Setup](https://github.com/nicholas-st-parker/frosthaven_led_updater/blob/4ba176e09931a0256b2d651c34908fef847aafd1/media/electronics_setup.jpg)
![Logic Level Converter Setup](https://github.com/nicholas-st-parker/frosthaven_led_updater/blob/4ba176e09931a0256b2d651c34908fef847aafd1/media/line_level_setup.jpg)

## Guide
- Follow [this guide](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview) to get the LED strip working on the Pi.
> [!NOTE]
> My setup needed a logic level converter to convert the 3.3v data signal to 5v for the led 
> strip. The line level converter needs to be powered by 3.3v and 5 volt power, in addition to 
> the signal wires and ground wires. There should be 6 wires total hooked up to the line level 
> converter. See picture above for reference.
- Clone this repository on Pi
- Edit "settings.cfg" file in the project directory according to your settings. [See header below for details](https://github.com/nicholas-st-parker/frosthaven_led_updater/tree/master?tab=readme-ov-file#example-settingscfg)
- Start a FroshavenAssistant server.
- Change ip address and port in main.py to match the FrosthavenAssistant server IP and port.
- Run main.py

## Example settings.cfg
```
[Playerx]
character: fill in the character name you want to light up. EG: "Brute" I will have a full 
character list shortly with spoiler tags.
start_led_index: the first led index along to strip where a person is located.
end_led_index: the last led index along the strip where a person is located.
name: Does not matter. No function yet. Do not leave blank.

[DummyPlayerx]
character: Fill a random name in here.
start_led_index: led start and endindex for dummy players determine the leftover leds where no 
elements and no players are located.
end_led_index: ^
name: Does not matter. No function yet.
Do not leave blank.

[Elementx]
element = do not change these.
start_led_index = start led of the specific element.
end_led_index = end led of the specific element.
color = color of the element. colors are passed like "r,g,b", without quotes and without spaces, 
where r is red, g is green and b is blue.
```

You will need to play around with the indexes to find what works for your setup. Light up a 
couple at a time and count the leds to find the indexes.

My setup is with a 100 address strip. It's technically 300 leds, but they light up three at a time.
