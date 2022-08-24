## Make sure you read the License (Attribution-NonCommercial-ShareAlike 4.0 International)

[![Purchase on PCBWay](/assets/purchase-on-pcbway.png)](https://www.pcbway.com/project/shareproject/MBC5_E_Ink_Flashcart_4MB_Flash_FRAM_83edab87.html)

If you want to support me for free (and get 5 USD in new user credit) you can use my PCBWay [Referral link](https://www.pcbway.com/setinvite.aspx?inviteid=388393) when signing up on PCBWay

![](https://i.imgur.com/Iy5TtAD.png)

[![PCBWay Referral](/assets/referral-link.png)](https://www.pcbway.com/setinvite.aspx?inviteid=388393)

Boards will only be available from PCBWay. Kicad or gerbers will not be provided. Unfortunately, there has been an increase in people abusing the license and the projects I publish for the community. I don't see this changing anytime soon.

**Make sure you read the License!**

https://user-images.githubusercontent.com/20230450/186256513-c9dcb02d-fbb6-43f8-9a56-36a67a7be4b6.mp4

**Flashing:**
1. [Download the latest version](https://circuitpython.org/board/raspberry_pi_pico/) of CircuitPython for the Raspberry Pi Pico.
2. Connect the cart using a USB A to C cable and drop the CircuitPython .uf2 file onto the device.
3. Once the CircuitPy device pops up, move the files that correspond to your display from "Circuitpy Files" onto your device. Choose the correct resolution matching the display installed.
4. Drop a 152x152 or 200x200 1 or 2 bit BMP onto the device to update the e-ink display image. Choose the correct resolution matching the display installed.

**BOM:**
| Reference | Description | Footprint | Part# |
|-|-|-|-|
| C1, C2, C3, C4, C7, C8, C11, C12, C13, C15, C16, C17, C20, C21, C28  | 100nF Capacitor | SMD 0402 |  |
| C5, C6, C9, C10, C19, C22, C23, C24, C25, C26, C27, C29 | 1uF Capacitor | SMD 0603 |  |
| C14, C18 | 4.7uF Capacitor | SMD 0603 |  |
| CCR1, CCR2 | 5.1KΩ Resistor | SMD 0603 |  |
| D1, D2, D3 | Diode | SMD SOD-123 | MBR0530 |
| J1 | CartBus | Custom (djedditt) |  |
| J2 | USB-C Receptacle | Custom | TYPE-C-31-M-12 |
| J3 | FPC24(0.5mm) | Hirose_FH12-24S-0.5SH_1x24-1MP_P0.50mm_Horizontal | FH12-24S-0.5SH |
| L1 | 10uH 1A  | SMD 1210 | LQH32PZ100MNCL |
| Q1 | NMOS | SMD SOT-323 | Si1308EDL |
| R1, R4 | 10kΩ Resistor | SMD 0603 |  |
| R2, R3 | 27Ω Resistor | SMD 0603 |  |
| R5 | 3Ω Resistor | SMD 0603 |  |
| R6 | 1KΩ Resistor | SMD 0603 |  |
| R7 | Optional 10KΩ Resistor (DNF) | SMD 0603 |  |
| R8 | 0.47Ω | SMD 0603 | |
| SW1 | Boot Switch | SW_SPST_B3U-1000P | B3U-1000P |
| SW2 | Screen Switch (used to switch between screen types) | SW_SPDT-K3-1296S-E1 | K3-1296S-E1 |
| U1 | 3-Input OR Gate | SMD TSOP-6 | 74LVC1G332GW,125 |
| U2 | 256Kb FRAM | SMD SOIC-28W | FM18W08-SG |
| U3 | 4MB Flash | SMD TSOP-I-40 | MBM29F033C |
| U4 | Memory Bank Controller | SMD LQFP-32 | MBC5 |
| U5 | 3.3V Voltage Regulator | SMD SOT-23-5 | RT9013-33GB |
| U6 | Micro Controller | SMD QFN-56 | RP2040 |
| U7 | 128Mb Serial Flash | SMD SOIC-8 | W25Q128JVS |
| X1 | 12MHz Crystal Oscillator | SMD 3225-4Pin | CO32H4-12.000-WPJHPSN |

**Displays:**
| Model Number | Resolution | Grayscale |
|-|-|-|
| [GDEW0154T8D](https://www.aliexpress.com/item/1005004027620986.html) | 152x152 | Yes |
| [Waveshare 1.54"](https://www.waveshare.com/product/1.54inch-e-paper.htm) | 200x200 | No |
| [GDEH0154D67](https://www.aliexpress.com/item/33044560386.html)  | 200x200 | Yes, but not currently supported |
| [GDEY0154D67](aliexpress.com/item/1005004027620986.html)  | 200x200 | Yes, but not currently supported |

* Pin compatible UC8151D & SSD1681 based displays should also work.


Makes use of [djedditt's](https://github.com/djedditt/s) [gamepak footprint](https://github.com/djedditt/kicad-gamepaks)
