#! /bin/bash
DIRECTORY_TO_OBSERVE="."

function block_for_change {
  inotifywait -r \
    -e modify,move,create,delete \
    $DIRECTORY_TO_OBSERVE
}

function build {
  py.test --feature features
}

build

while block_for_change; do
  build
done
