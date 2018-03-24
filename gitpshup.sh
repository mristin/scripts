#!/bin/bash
BRANCH=$(git rev-parse --abbrev-ref HEAD)

if [ "$BRANCH" == "master" ]; then
  echo "You can not push to master branch."
  exit 1
fi

if [ -f `pwd`/precommit.sh ]; then
	`pwd`/precommit.sh
	if [ $? -ne 0 ]; then
		echo "precommit failed."
		exit 1
	fi
fi

CMD="git push --set-upstream origin $BRANCH"

echo "$CMD"
echo

TMPFILE="/tmp/gitpushup.$$.tmp"
$CMD 2>$TMPFILE

cat $TMPFILE
REJECTED=$(cat $TMPFILE|grep "[rejected]"|wc -l)
TIP=$(cat $TMPFILE|grep "hint: Updates were rejected because the tip of your current branch is behind"|wc -l)

if [[ $REJECTED > 0 && $TIP > 0 ]]; then
  echo
  CMD="git push --set-upstream origin $BRANCH --force"
  echo $CMD
  $CMD
fi

