#!/bin/bash
#!/bin/bash
BRANCH="$1"

if [ -z "$BRANCH" ]; then
    BRANCH=`git rev-parse --abbrev-ref HEAD`
fi

if [ "$BRANCH" == "master" ]; then
    echo "You are on the master branch. You can not delete the master."
    exit 1
fi

while true; do
    read -p "Are you sure you want to pull from master and delete the branch $BRANCH? (y/n)" yn
    case $yn in
        [Yy]* ) git checkout master && git pull && git branch -d $BRANCH; break;;        
	[Nn]* ) exit;;
        * ) echo "Please answer y or n";;
    esac
done

