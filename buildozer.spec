[app]

# App Information
title = Mikey Bot
package.name = mikeybot
package.domain = org.mikeybot
version = 1.0.0

# Source
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt
source.exclude_dirs = tests,bin,venv,.venv,.buildozer,.git,.github
source.exclude_patterns = *.pyc,*.pyo,__pycache__/*,.gitignore,*.md

# Python / Kivy Requirements
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests

# Python-for-Android
p4a.branch = develop

# Screen
orientation = portrait
fullscreen = 0

# Android Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Android SDK / NDK
android.api = 36
android.minapi = 24
android.ndk = 29

# Architecture
android.archs = arm64-v8a

# AndroidX
android.enable_androidx = True

# SDK License
android.accept_sdk_license = True

# Debug APK
android.debug_artifact = apk


[buildozer]

log_level = 2
warn_on_root = 0
