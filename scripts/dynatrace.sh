#!/usr/bin/env bash
# -*- coding: utf-8 -*-

if [[ -z "$DYNATRACE_API_TOKEN" ]]; then
    echo "Error: Dynatrace API token not provided."
    exit 1
fi

if [[ -z "${DYNATRACE_BASE_URL}" ]]; then
    echo "Error: DYNATRACE_BASE_URL environment variable is not set."
    exit 1
fi

DEPLOYMENT_NAME="Test Application Development"
VERSION="1.0"
DEPLOYMENT_PROJECT="image-gen-hub"
CI_BACKLINK="https://github.com/ivasik-k7/image-gen-hub"

API_ENDPOINT="${DYNATRACE_BASE_URL}/events/Custom/"

PAYLOAD='{
  "eventType": "CUSTOM_DEPLOYMENT",
  "source": "My CI/CD Pipeline",
  "deploymentName": "'"${DEPLOYMENT_NAME}"'",
  "version": "'"${VERSION}"'",
  "deploymentProject": "'"${DEPLOYMENT_PROJECT}"'",
  "ciBackLink": "'"${CI_BACKLINK}"'"
}'

curl -X GET \
    -H "Authorization: Api-Token ${DYNATRACE_API_TOKEN}" \
    -H "Content-Type: application/json" \
    -d "${PAYLOAD}" \
    "${API_ENDPOINT}"

if [ $? -eq 0 ]; then
    echo "Deployment event sent successfully to Dynatrace."
else
    echo "Failed to send deployment event to Dynatrace."
    exit 1
fi
