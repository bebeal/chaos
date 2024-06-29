#!/bin/sh

java -d64 -server -XX:+AggressiveOpts -XX:+UnlockExperimentalVMOptions -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+CMSConcurrentMTEnabled -XX:+ExplicitGCInvokesConcurrent -XX:ParallelGCThreads=4 -XX:+OptimizeStringConcat -XX:+UseStringDeduplication -XX:+UseFastAccessorMethods -XX:+DisableExplicitGC -XX:MaxGCPauseMillis=10 -XX:GCPauseIntervalMillis=50 -XX:NewSize=84m -XX:+UseAdaptiveGCBoundary -XX:NewRatio=3 -Dfml.readTimeout=90 -jar server.jar nogui
