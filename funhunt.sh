# asking if packages have been installed 
echo "have your packages been installed y/n?"
read -r package

# installs packages if answer is y continues if n
if [ $package = n ];
then
    printf "cool installing packages"
    python packages.py
elif [ $package = y ];
then
    continue
fi

#asks if you want to go hunting for graphic cards
echo "Would you like to go egghunting"
echo "yes or no" 
read -r question

if [ $question = no ];
then
    printf "seeya"
fi
while [ $question = yes ];
do
    echo "you sure you want to go hunting y/n?"
    read -r question2
    if [ $question2 = y ];
    then     
        python egghunt.py
    elif [ $question2 = n ];
    then
        printf "good bye" 
        question=$((question=no))
    fi
done

