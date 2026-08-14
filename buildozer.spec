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

# Target API & NDK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.enable_androidx = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 0
