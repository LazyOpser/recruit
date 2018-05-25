#!/usr/bin/env bash

CURRENT_DIR=`pwd`
OLD_GO_PATH="/usr/local/Cellar/go/1.10.2"
OLD_GO_BIN="/usr/local/Cellar/go/1.10.2/bin"

export GOPATH="$CURRENT_DIR" 
export GOBIN="$CURRENT_DIR/bin"

#指定并整理当前的源码路径
gofmt -w src

go install test_hello

export GOPATH="$OLD_GO_PATH"
export GOBIN="$OLD_GO_BIN"
