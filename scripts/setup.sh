

setup() {
    # Reading the repo to be cloned
    read -p "Enter the repo link to be cloned : " link
    git clone "$link"

    # Going inside the repo and installing it
    read -p "Enter path to the Repo folder:" name
    cd "$name"
    ./configure
    make
    make install
}