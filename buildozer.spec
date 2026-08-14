[app]

# Title & Package info
title = Mikey Bot
package.name = mikeybot
package.domain = org.mikeybot

# Source code settings
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_dirs = tests, bin, venv, .buildozer, .git, .github
source.exclude_patterns = license, .gitignore, .github/*

# Version & Requirements
version = 1.0.0
requirements = python3,kivy==2.3.0

# UI & Permissions
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,NETWORK_STATE

# Target API & MinAPI
android.api = 33
android.minapi = 21

# CRITICAL FIX: Lock NDK to stable 25b (prevents auto-downloading buggy NDK r28c)
android.ndk = 25b
android.ndk_api = 21

android.accept_sdk_license = True
android.enable_androidx = True
android.archs = arm64-v8a

[buildozer]
# Log level 1 keeps logs clean
log_level = 1
warn_on_root = 0
