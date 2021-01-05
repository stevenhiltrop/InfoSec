# About
Setting up a VM that has half the resources of your device has never been a favorite amongst security enthusiasts. Some have tried to make MacOS Homebrew tap's before, but this requires a lot of maintenance and eventually they have abandoned the project.

My goal for this project is to use formula's and casks directly from Homebrew so that the only maintenance is to add to the listed tools and furthermore contribute to Homebrew directly rather than his sideproject. I believe this will provide a longer lasting solution.

# Setup
## Prerequirements
    xcode-select --install
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

## Install
    brew update && brew upgrade
    brew install $(cat kali_tools.txt)

# Source
Credits go to Sidaf (https://github.com/sidaf/) for his admirable work that inspired me to do this.


# TODO:
* Pull https://http.kali.org/dists/kali-rolling/main/source/Sources.gz
* Create a cask converting linux to brew requirements as stated on (https://docs.brew.sh/Formula-Cookbook)
* Create an app with dropdown listing tools per category


