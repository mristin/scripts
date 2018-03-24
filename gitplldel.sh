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
git checkout master && git pull && git branch -d $BRANCH
