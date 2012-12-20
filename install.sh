if [[ $UID != 0 ]]; then
    echo "Please run this script with sudo:"
    echo "sudo $0 $*"
    exit 1
fi

echo
for dir in ./*; do
    if [ -d $dir ]
    then
        bash $dir/install.sh
    fi
done
