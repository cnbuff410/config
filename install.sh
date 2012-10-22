echo
for dir in ./*; do
    if [ -d $dir ]
    then
        bash $dir/install.sh
    fi
done
