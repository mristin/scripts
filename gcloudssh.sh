#!/bin/bash
gcloud compute ssh devop@$1 --zone europe-west1-c "${@:2}" 

