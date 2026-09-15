# 👻 BW16 Specter — Dual-Band 2.4 / 5 GHz Pentesting & Sniffy Engine

[![Board](https://img.shields.io/badge/Hardware-Ai--Thinker%20BW16%20%28RTL8720DN%29-8b5cf6?style=for-the-badge)](https://www.ai-thinker.com/)
[![Firmware](https://img.shields.io/badge/Version-v1.5.0--Beta-22d3ee?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-4ade80?style=for-the-badge)]()

**BW16 Specter** is an advanced open-source Wi-Fi pentesting firmware for the Realtek AmebaD RTL8720DN (Ai-Thinker BW16) module. Featuring dual-band 2.4GHz & 5GHz packet injection, autonomous target tracking, real-time WPA/WPA2 4-way handshake capture, and an ST7735 cyberpunk graphical TFT interface.

---

## 🚀 Key Features

- **Dual-Band Deauth Engine**: Target 2.4GHz and 5GHz access points & client devices with raw 802.11 deauth frame injection.
- **Autonomous Sniffy Engine**: Single-scan sequential targeting mode. Scans the RF spectrum, ranks APs by RSSI, conducts deauth bursts, and captures WPA/WPA2 handshakes automatically.
- **ST7735 TFT Cyberpunk UI**: 128x160 color display driver with animated state mood bitmaps, live RF waterfall spectrum display, and zero-flicker double-buffered rendering.
- **WPA/WPA2 Handshake Validation**: Real-time EAPOL 4-way handshake verification. Handshakes saved in RAM and downloadable in standard `.pcap` format.
- **Captive Portal Phishing**: Customizable phishing portals with active DNS redirection and concurrent deauth enforcement.
- **Remote Web Dashboard & REST API**: Hosted SoftAP web server broadcasting at `http://192.168.4.1`.

---

## 🔌 Hardware Pinout & Wiring

Connect your **Ai-Thinker BW16 (RTL8720DN)** to the **ST7735 SPI TFT Display** and **3 Tactile Navigation Buttons**:

### 1. ST7735 128x160 SPI Display
| ST7735 Signal | BW16 Pin | Description |
|---|---|---|
| **CS** | `PA27` | SPI Chip Select |
| **DC** | `PA25` | Data / Command Control |
| **RST** | `PA26` | Display Reset |
| **SCLK** | `PA14` | SPI Clock |
| **MOSI** | `PA12` | SPI Data Input |
| **BLK** | `PA30` | Backlight (3.3V) |
| **VCC** | `3.3V` | Power (3.3V Power Rail) |
| **GND** | `GND` | Ground |

### 2. Navigation Buttons (Active LOW)
| Button | BW16 Pin | Action |
|---|---|---|
| **UP** | `PB1` | Move Selection UP |
| **OK / SELECT** | `PB3` | Short Press: Select / Toggle<br>**Long Press (Hold): Return to Menu / Abort** |
| **DOWN** | `PB2` | Move Selection DOWN |

> 💡 **Note:** Connect one pin of each button switch to the corresponding BW16 GPIO pin, and the opposite pin to **GND** (internal `INPUT_PULLUP` enabled).

---

## ⚡ Web Serial Flasher

You can flash BW16 Specter directly from your browser (**Chrome**, **Edge**, or **Opera**) without installing Arduino IDE or USB drivers!

### Step 1: Put BW16 in Download Mode
1. Press and **hold** the **BURN** button on the BW16 module.
2. Press and **release** the **RST** button.
3. Release the **BURN** button — the module is now in UART Download Mode.

### Step 2: Flash
1. Open [`index.html`](file:///Users/gamkers/Documents/Arduino/RTL8720dn-Deauther-master/bw16-specter-release/index.html) or host it on GitHub Pages.
2. Click **Connect Serial Device** and select your USB COM port.
3. Click **Flash Firmware to BW16**.

---

## 🌐 Web Interface & AP Access

After flashing and booting your BW16 module:
- **SoftAP SSID**: `BW16Specter`
- **SoftAP Password**: `specter16`
- **Web Dashboard**: `http://192.168.4.1`
- **Handshakes & PCAPs**: `http://192.168.4.1/sniffy`

---

## 📁 Repository Structure

```
bw16-specter-release/
├── index.html              ← Full landing page & Web Serial flasher (production)
├── index_release.html      ← Standalone flasher release file
├── flasher.html            ← Flasher mirror file
├── index_template.html      ← Clean template for generate_flasher.py
├── generate_flasher.py     ← Python build script to embed .bin into template
├── firmware/
│   ├── imgtool_flashloader_amebad.bin
│   ├── km0_boot_all.bin
│   ├── km4_boot_all.bin
│   └── km0_km4_image2.bin  (806,912 bytes - fresh compiled build)
└── README.md
```

---

*BW16 Specter created by GAMKERS COLAB WITH TIM(https://github.com/gamkers).*
