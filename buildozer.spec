[app]

# App Information
title = Mikey Bot
package.name = mikeybot
package.domain = org.mikeybot

version = 1.0.0

# Source Code Inclusions
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt
source.exclude_dirs = tests,bin,venv,.venv,.buildozer,.git,.github
source.exclude_patterns = *.pyc,*.pyo,__pycache__/*,license,.gitignore

# Requirements (Matched exactly with requirements.txt & p4a)
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,urllib3,certifi,chardet,idna,pillow

# UI & Display
orientation = portrait
fullscreen = 0

# Android Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Target API, Min API, NDK (Stable for Kivy 2.2.1 + KivyMD 1.1.1)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# Architecture & Settings
android.accept_sdk_license = True
android.enable_androidx = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 0
