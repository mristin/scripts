#!/bin/bash
repo=$(basename $(git rev-parse --show-toplevel))

if [[ "$repo" == "production" ]]; then
	firefox https://bitbucket.org/parqueryag/production/pull-requests/new
elif [[ "$repo" == "production_config" ]]; then
	firefox https://bitbucket.org/parqueryag/production_config/pull-requests/new
else
	echo "Unhandled repo: $repo"
	exit 1
fi
