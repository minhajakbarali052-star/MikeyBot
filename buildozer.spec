[app]

# Title & Package info
title = Mikey Bot
package.name = mikeybot
package.domain = org.mikeybot

version = 1.0.0

# Source settings
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt
source.exclude_dirs = tests,bin,venv,.venv,.buildozer,.git,.github
source.exclude_patterns = *.pyc,*.pyo,__pycache__/*,license,.gitignore

# Requirements
requirements = python3==3.10.11,kivy==2.3.0

# UI & Display
orientation = portrait
fullscreen = 0

# Android Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Target API, Min API, NDK
android.api = 33
android.minapi = 21
android.ndk = 25b

# License Auto-Accept & Feature Flags
android.accept_sdk_license = True
android.enable_androidx = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 0
