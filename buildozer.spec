[app]

# Title & Package info
title = Mikey Bot
package.name = mikeybot
package.domain = org.mikeybot

# Source code settings
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_dirs = tests, bin, venv, .buildozer, .git, .github, kivy/tests
source.exclude_patterns = license, .gitignore, .github/*, */tests/*, */test/*

# Version & Requirements
version = 1.0.0
requirements = python3,kivy

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

# Blacklist unneeded test files to save compilation time & storage
android.blacklist_patterns = sqlite3/*,lib-dynload/test/*,lib-dynload/json/tests/*,*/test/*,*/tests/*,*/Lib/test/*,kivy/tests/*

[buildozer]
# Log level 1 prevents 30,000+ line log overflow crash on GitHub
log_level = 1
warn_on_root = 0
