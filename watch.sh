#! /bin/bash
DIRECTORY_TO_OBSERVE="."
ON_CHANGE="py.test --feature features"

function block_for_change {
  inotifywait -r \
    -e modify,move,create,delete \
    $DIRECTORY_TO_OBSERVE
}

function command_exists {
  type "$1" &> /dev/null ;
}

function build {
  eval $ON_CHANGE
}

function start_watch {
  if command_exists fswatch; then
    fswatch -o $DIRECTORY_TO_OBSERVE | xargs -n1 -I{} $ON_CHANGE
  else
    while block_for_change; do
      build
    done
  fi
}

build
start_watch
