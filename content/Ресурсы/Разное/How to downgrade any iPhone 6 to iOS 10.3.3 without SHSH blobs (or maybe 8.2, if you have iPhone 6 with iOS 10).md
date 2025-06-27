---
tags: 
publish: true
modified:
  - 2025-06-27T21:52:27+07:00
  - 2025-06-27T20:57:35+07:00
  - 2025-06-27T15:07:39+07:00
  - 2025-06-26T17:44:35+07:00
created: 2025-06-26T17:43:03+07:00
---
Hey! I successfully downgraded an iPhone 6 to iOS 10.3.3 using Semaphorin on a MacBook M1.  Yes, the official instructions say "Intel only," but this method **does work** on Apple Silicon too. I tested it on a MacBook Air M1 running macOS 15 Sequoia. My iPhone 6 was originally on iOS 12.5.7, and I downgraded it to iOS 10.3.3
## Requirments 
- Intel Mac with macOS Catalina or later 
- Apple Silicon Mac with macOS Big Sur or later 
- Linux PC (any distro, tested on Xubuntu by [Burhan Rana](https://www.youtube.com/watch?v=K0YBvfa44H0))
- Stable internet connection
- iPhone 5s / iPhone 6 / iPhone 6 Plus (it works with other iDevices, includes A7-A11, but I'm not sure)
## Chart of compability (source: Semaphorin latest commit before archival)
| iOS                                                      | App Store | Cydia & Tweaks | Respring | Cellular | iTunes |
| -------------------------------------------------------- | --------- | -------------- | -------- | -------- | ------ |
| 7.0.6 ‎   <br>↳ dualboot if main OS is 10.3.3 or below   | ☑         | ☑              | ☑        | ☑        | ☑      |
| 7.1.2 ‎   <br>↳ dualboot if main OS is 10.3.3 or below   | ☑         | ☑              | ☑        | ☑        | ☑      |
| 8.2-8.4.1   <br>↳ dualboot if main OS is 10.3.3 or below | ☑         | ☑              | ☑        | ☐        | ☑      |
| 9.3 ‎ ‎ ‎   <br>↳ dualboot if main OS is 10.3.3 or below | ☑         | ☑              | ☑        | ☑        | ☐      |
| 10.3.3   <br>↳ dualboot on any main OS                   | ☑         | ☑              | ☑        | ☑        | ☐      |
| 11.3 ‎ ‎   <br>↳ dualboot on any main OS                 | ☑         | ☑              | ☑        | ☑        | ☐      |
| 12.1 ‎ ‎   <br>↳ dualboot on any main OS                 | ☑         | ☑              | ☑        | ☑        | ☐      |
## Apple Silicon Mac Method
1. Open **Terminal via Rosetta 2**:
    - Right-click `Terminal.app` > **Get Info** > check "Open using Rosetta"
    - You can find `Terminal.app` in Finder > Applications > Utilities, or via Launchpad
2. **Alternative:** If you don’t want to launch Terminal via Rosetta manually, you can run:
    ```bash
    arch -x86_64 zsh
    ```
    in a normal Terminal window.
3. Confirm the architecture by typing:
    ```bash
    uname -m
    ```
    It should return `x86_64`.
4. Install git (if you don't have it) and clone the Semaphorin repo:
    ```bash
    git clone https://github.com/LukeZGD/Semaphorin.git
    ```
5. Go to the Semaphorin directory:
    ```bash
    cd Semaphorin
    ```
6. Connect your device (iPhone 5s or iPhone 6) using a **Lightning to USB-A** cable  
	1. **USB-C to USB-A** adapter if needed (if you use Type-C port)
7. Run the downgrade command:
    ```bash
    sudo ./semaphorin.sh <target iOS version> --restore
    ```
    Example:  
    ```bash
    sudo ./semaphorin.sh 10.3.3 --restore
    ```
8. When prompted:
    ```
    [*] Please enter the iOS version that is currently installed on your device.
    ```
    Enter your current iOS version (in my case, I typed `12.5.7`) and press Enter
9. The downgrade process will begin. Follow the on-screen instructions.  Your device will reboot several times and load into an SSH Ramdisk — don't worry if you see a bunch of terminal output on the screen. That’s expected :)
10. Once the script finishes and shows `done`, your iPhone should automatically boot into the downgraded iOS version
11. **Important:** If your iPhone restarts (or loses power), it will boot back into your original iOS
    To return to the downgraded iOS, run:
    ```bash
    sudo ./semaphorin.sh <version> --boot
    ```
    Example:
    ```bash
    sudo ./semaphorin.sh 10.3.3 --boot
    ```
## If Something Goes Wrong (Step 12)
12. If downgrade fails in step 10 (iPhone don't boot into the downgraded iOS version and boot to main iOS), do this:
    - Put your device into **DFU mode**
    - Restore it to the latest signed iOS version from [ipsw.me](https://ipsw.me)
    - Then repeat steps 1–10
### Important Notes!
- You **must restore** if your current iOS is 12.5.7 or another useless version
- **Do NOT restore** if you're already on iOS 10.3.3 or an iOS you want to keep **and don’t have SHSH blobs**.
- Honestly though — if you follow this guide carefully, **you probably won’t need Step 12 at all**.
## Intel Mac / Linux Method
Follow steps 4–10 from the Apple Silicon method — no Rosetta steps required.
## Troubleshooting (iPhone 6 with downgrade to iOS 10.3.3)
### Passcode 
- You can set a password, but it gets reset after a reset
- Let's say we set a password of 123456
	 - After a respring, we can enter 111111 or any other combination, and it will unlock the device
- The result is that: **the UI of the passcode works, but the UX is lost**
- ! The problem is that: we lose the overall lock (anyone can take our iPhone and access our private information).
	 - It's easy to solve: if you use your device as your daily driver, just don't store important information on it and DON'T INSERT A SIM
	 - No one is immune to phone theft or loss
### Touch ID 
- No passcode => no Touch ID
- In addition, after each reboot, a banner "Unable to activate Touch ID" will persistently pop up, which can only be responded to with "OK"
- Result: **it simply doesn't work**
- ! The problem is that: we lose a convenient way to unlock our device and a cool feature
### Connecting to password-protected Wi-Fi (encryption ≠ Open)
- We did a downgrade without SHSH blobs => got iOS without "trust certificates" 
	 - This means that our device simply cannot use encryption 
- You can enter the correct password for the WLAN2 network any times, but you will get nothing but the "Incorrect Password" banner
### iMessage + FaceTime 
- Both services freeze at the activation stage 
	 - You can enter your Apple ID, but the activation gear just freezes 
 - The result is that: **it is impossible to log in to iMessage and FaceTime**
	 - I don't know what the problem is, because the App Store logs in to your Apple ID account perfectly
### Syncing via iTunes / iFunBox / iMazing / similar programs
- The iPhone simply cannot create a "trust pair" between iOS and macOS/Windows
	 - An error will just pop up, supposedly the iPhone does not have the necessary values.
- Bottom line: **just doesn't work**
- ! What's the problem: we just can't upload music, videos, books, podcasts to our device in embedded applications (Music, Videos, iBooks, Podcasts)
### Hotspot 
- There is no encryption => and the mechanism for sharing the Internet itself breaks down 
	 - Yes, the toggle switch can be turned on, but **the password from the access point will constantly change**, and it will not be possible to connect even for a couple of seconds
- Bottom line: **UI works, but UX does not**
- ! What is the problem: from such an iPhone, we simply will not be able to share our mobile Internet to other devices
### Siri
- I don't know what the problem is, but even when you turn on the "Siri" option in the settings, it only says "Sorry. Could you repeat that?"
	 - Sometimes, when you hold down the "Home" button, Siri just freezes and doesn't say anything