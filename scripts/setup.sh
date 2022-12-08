

setup() {
    read -p "Enter the repo link to be cloned : " link
    git clone "$link"
    read -p "Enter path to the Repo folder:" name
    cd "$name"
    ./configure
    make
    make install
}