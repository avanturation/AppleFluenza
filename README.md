# Siri

> A Discord bot for Apple firmwares.

## Disclaimer

This project will be suspended forever due to the shutdown of dpy.

I respect the decision that Danny made. Thank you for your dedication on dpy.

## Features

Siri can provide firmware informations of Apple Devices (iPhone, iPad, iPod .. etc)

Siri can also provide macOS Packages (Intel-based Macs, and Apple Silicon Macs)

Siri supports multi language (한국어, English).

All commands are processed by [Pyapple](https://github.com/fxrcha/Pyapple)

### Pyapple

Pyapple is Python wrapper for Apple Swscan server (swscan.apple.com) and ipsw.me API (api.ipsw.me).

All Apple firmwares are processed by this module.

```bash
python3 -m pip install pyapple
```

## Build and run

### Tested environment

* [macOS Big Sur 11.1](https://www.apple.com/macos/big-sur/)

* [Python 3.8.6 for Darwin](https://www.python.org/downloads/release/python-386/)

* [MacBookPro15,1](https://support.apple.com/kb/SP776) and [Macmini9,1](https://www.apple.com/mac-mini/) (Tested on M1)

#### Windows

```powershell
git clone https://github.com/UniqueCodeGit/Siri

cd Siri

python3 -m pip install -r requirements.txt

python3 -m Siri
```

#### macOS

```zsh
git clone https://github.com/UniqueCodeGit/Siri

cd Siri

python3 -m pip install -r requirements.txt

python3 -m Siri
```

#### Linux

```bash
git clone https://github.com/UniqueCodeGit/Siri

cd Siri

python3 -m pip install -r requirements.txt

python3 -m Siri
```

## Credits

[Apple (for providing firmwares)](https://apple.com)

[IPSW.me (for providing Firmware API)](https://ipsw.me)

[Hiyobot (for infrastructures)](https://github.com/Saebasol/Hiyobot)
