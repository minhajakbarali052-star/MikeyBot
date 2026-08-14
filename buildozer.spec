[app]

# (str) Title of your application
title = Mikey Bot

# (str) Package name
package.name = mikeybot

# (str) Package domain (needed for android/ios packaging)
package.domain = org.mikeybot

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files / directories to exclude
source.exclude_exts = spec
source.exclude_dirs = tests, bin, venv, .buildozer, .git, .github
source.exclude_patterns = license, .gitignore, .github/*

# (string) Application versioning
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,NETWORK_STATE

# (int) Target Android API
android.api = 33

# (int) Minimum API support
android.minapi = 21

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (bool) Enable AndroidX support
android.enable_androidx = True

# (list) Target architecture
android.archs = arm64-v8a

[buildozer]

# (int) Log level
log_level = 2

# (int) Display warning if run as root
warn_on_root = 0
