[app]

# App Info
title = Mikey Bot
package.name = mikeybot
package.domain = org.mikeybot

version = 1.0.0

# Source Files
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt
source.exclude_dirs = tests,bin,venv,.venv,.buildozer,.git,.github
source.exclude_patterns = *.pyc,*.pyo,__pycache__/*,license,.gitignore

# Requirements
requirements = python3,kivy==2.3.0

# Display & Orientation
orientation = portrait
fullscreen = 0

# Android Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Target API, Min API, NDK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# License Auto-Accept & Architecture
android.accept_sdk_license = True
android.enable_androidx = True
android.archs = arm64-v8a

[buildozer]
# Prevents terminal log truncation and buffer overflow
log_level = 1
warn_on_root = 0
